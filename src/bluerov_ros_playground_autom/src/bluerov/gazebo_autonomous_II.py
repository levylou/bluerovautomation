#!/usr/bin/env python

import rospy
import time
import math as m
try:
    import pubs
    import subs
except:
    import bluerov.pubs as pubs
    import bluerov.subs as subs

from tkinter import *
from geometry_msgs.msg import TwistStamped, Twist, Pose
from gazebo_msgs.msg import ModelStates
from mavros_msgs.srv import CommandBool
from sensor_msgs.msg import JointState, Joy
from std_msgs.msg import Float32
from bluerov_ros_playground.msg import Custom 

def Angle(des, curr):
    x = 3.14 - abs(des) + 3.14 - abs(curr)
    if abs(des - curr) > x:
        if(des - curr) > 0:
            return -x
        else:
            return x
    else:
        return des - curr

def Val(old, curr, des):
    if ((old > 0 and curr < 0) or (old < 0 and curr > 0)):
        if (abs(old-des) > 2):
            x = 3.14 - abs(old - des) + 3.14 - abs(curr - des)
            return x
        else:
            return curr - old
    else:
        return curr - old

def error(er):
    if (abs(er > 20)):
        er = 20 * er / abs(er)
    return er

class GazeboAuto(object):

    """Class to handle with gazebo teleop

    Attributes:
        pub (TYPE): ROS publisher
        sub (TYPE): ROS subscriber
    """

    def enforce_limit(self, value):
        if (value < -1.0):
            value = -1.0
        elif (value > 1.0):
            value = 1.0
        return value

    def __init__(self):
        super(GazeboAuto, self).__init__()

        self.sub = subs.Subs()
        self.pub = pubs.Pubs()

        self.sub.subscribe_topic('/gazebo/model_states', ModelStates)
        self.sub.subscribe_topic('/desiredposition', Custom)

        self.pub.subscribe_topic('/autoI', Custom)
        self.pub.subscribe_topic('/autoII', Custom)

    def get_position_I(self):
        model = self.sub.get_data()['gazebo']['model_states']['name']
        for i in range(3):
            state = self.sub.get_data()['gazebo']['model_states']['pose'][i]['position']
            if model[i] == 'BlueRov2':
                x1 = state['x']
                y1 = state['y']
                z1 = state['z']
        pos = [x1, y1, z1]
        return pos

    def get_position_II(self):
        model = self.sub.get_data()['gazebo']['model_states']['name']
        for i in range(3):
            state = self.sub.get_data()['gazebo']['model_states']['pose'][i]['position']
            if model[i] == 'BlueRov2II':
                x1 = state['x']
                y1 = state['y']
                z1 = state['z']
        pos = [x1, y1, z1]
        return pos

    def get_orientation_I(self):
        model = self.sub.get_data()['gazebo']['model_states']['name']
        for i in range(3):
            state = self.sub.get_data()['gazebo']['model_states']['pose'][i]['orientation']
            if model[i] == 'BlueRov2':
                ob = state['x']
                oc = state['y']
                od = state['z']
                oa = state['w']

        siny_cosp = 2 * (ob * oc + oa * od)
        cosy_cosp = oa ** 2 + ob ** 2 - oc ** 2 - od ** 2
        yaw = m.atan2(siny_cosp, cosy_cosp)
        return yaw

    def get_orientation_II(self):
        model = self.sub.get_data()['gazebo']['model_states']['name']
        for i in range(3):
            state = self.sub.get_data()['gazebo']['model_states']['pose'][i]['orientation']
            if model[i] == 'BlueRov2II':
                ob = state['x']
                oc = state['y']
                od = state['z']
                oa = state['w']

        siny_cosp = 2 * (ob * oc + oa * od)
        cosy_cosp = oa ** 2 + ob ** 2 - oc ** 2 - od ** 2
        yaw = m.atan2(siny_cosp, cosy_cosp)
        return yaw

    def run(self):
        """ Run Gazebo Teleop
        """
        """Run user code
        """

        #pid variables rotational
        Pr = 0
        Ir = 0
        Dr = 0
        k_pr = 250
        k_ir = 1
        k_dr = 50
        oldr = 0
        er = 0

        #pid variables translational
        P = [0 for u in range(3)]
        I = [0 for u in range(3)]
        D = [0 for u in range(3)]
        k_p = [390, 300, 170] 
        k_i = [20, 20, 50]
        k_d = [690, 590, 500]
        e = [0 for u in range(3)]
        old = [0 for u in range(3)]

        while not rospy.is_shutdown():
      	    time.sleep(0.1)

            try:
                a = self.sub.get_data()['desiredposition']['data']
            except:
                a = [4, 2, -1, -1.5708]

            d = [a[0], a[1], a[2]]
            dr = a[3]

            # Try to get ROV positions
            try:
                

                posI = self.get_position_I()
                posII = self.get_position_II()
                xm = (posI[0] + posII[0]) / 2
                ym = (posI[1] + posII[1]) / 2
                zm = (posI[2] + posII[2]) / 2
                pos = [xm, ym, zm]

                dist = m.sqrt((posI[0] - posII[0]) ** 2 + (posI[1] - posII[1]) ** 2 + (posI[2] - posII[2]) **2)
                if abs(posII[0]) > abs(posI[0]):
                    yaw = m.asin((abs(posII[0]) - abs(posI[0])) / dist)
                else:
                    yaw = -m.asin((abs(posI[0]) - abs(posII[0])) / dist)
                #if abs(zII) > abs(zI):
                #    roll = m.asin((abs(zII) - abs(zI)) / dist)
                #else:
                #    roll = -m.asin((abs(zI) - abs(zII)) / dist)
                posr = yaw

            except Exception as error:
                print('get ROV positions error', error)            

            # PID calculation

            try:
                # translational
                for i in range(3):
                    P[i] = (d[i] - pos[i]) * k_p[i]
                    I[i] += (d[i] - pos[i]) * k_i[i] * 0.11
                    D[i] = ((-old[i] + d[i] - pos[i]) / 0.11) * k_d[i]
                    if I[i] > 150 or I[i] < -150:
                        I[i] = 150 * I[i] / abs(I[i])
                    e[i] = P[i] + I[i] + D[i]
                    old[i] = d[i] - pos[i]

                # rotational
                val1 = Angle(dr, posr)
                Pr = val1 * k_pr
                Ir += val1 * k_ir * 0.11
                Dr = -(abs(Val(oldr, val1, dr)) / 0.11) * k_dr * (Pr / abs(Pr))
                er = Pr + Dr + Ir
                oldr = val1

            except Exception as error:
                print('PID error:', error)

            try:
                # limits of error
                if (abs(e[0]) > 1000):
                    e[0] = 1000 * e[0] / abs(e[0])
                if (abs(e[1]) > 1000):
                    e[1] = 1000 * e[1] / abs(e[1])
                if (abs(e[2]) > 1000):
                    e[2] = 1000 * e[2] / abs(e[2])
                if (abs(er) > 650):
                    er = 650 * er / abs(er)

            except Exception as error:
                print('limit e[], er error:', error)

            # Try to send forces to topics
            try:
                forces = [0 for u in range(6)]
                forces_I = [0 for u in range(6)]
                forces_II = [0 for u in range(6)]

                forces[0] = -(e[0] * m.sin(-yaw) + e[1] * m.cos(-yaw)) / 1000 #Surge
                forces[1] = (e[0] * m.cos(-yaw) - e[1] * m.sin(-yaw)) / 1000 #Sway
                forces[2] = 0 #e[2] / 1000 #Heave
                forces[3] = 0 #Roll
                forces[4] = 0 #Pitch
                forces[5] = er / 650 #Yaw
                f = forces

                #forces_I[0] = +f[0] -f[1] +f[5]
                #forces_I[1] = +f[0] +f[1] +f[5]
                #forces_I[2] = -f[0] +f[1] -f[5]
                #forces_I[3] = -f[0] -f[1] -f[5]
                #forces_I[4] = +f[2]
                #forces_I[5] = +f[2]

                #forces_II[0] = +f[0] -f[1] -f[5]
                #forces_II[1] = +f[0] +f[1] -f[5]
                #forces_II[2] = -f[0] +f[1] +f[5]
                #forces_II[3] = -f[0] -f[1] +f[5]
                #forces_II[4] = +f[2]
                #forces_II[5] = +f[2]

                forces_I[0] = +f[0] +f[1] +f[5]
                forces_I[1] = +f[0] -f[1] -f[5]
                forces_I[2] = -f[0] -f[1] +f[5]
                forces_I[3] = -f[0] +f[1] -f[5]
                forces_I[4] = +f[2]
                forces_I[5] = +f[2]

                forces_II[0] = +f[0] +f[1] +f[5]
                forces_II[1] = +f[0] -f[1] -f[5]
                forces_II[2] = -f[0] -f[1] +f[5]
                forces_II[3] = -f[0] +f[1] -f[5]
                forces_II[4] = +f[2]
                forces_II[5] = +f[2]

                data = Custom()
		data.id = "autonomous"
		data.data = forces_I
		self.pub.set_data('/autoI', data)

                data = Custom()
		data.id = "autonomous"
		data.data = forces_II
		self.pub.set_data('/autoII', data)

            except Exception as error:
                print('forces error', error)  

if __name__ == "__main__":
    try:
        rospy.init_node('gazebo_autonomous_II', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    gazebo_teleop = GazeboAuto()
    gazebo_teleop.run()
