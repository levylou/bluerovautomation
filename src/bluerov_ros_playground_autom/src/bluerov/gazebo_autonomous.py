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

from geometry_msgs.msg import TwistStamped, Twist, Pose
from gazebo_msgs.msg import ModelStates
from mavros_msgs.srv import CommandBool
from sensor_msgs.msg import JointState
from std_msgs.msg import Float32
from bluerov_ros_playground.msg import Custom 

def Angle(des, curr):
    x = 3.14 - abs(des) + 3.14-abs(curr)
    if abs(des-curr) > x:
        if(des-curr) > 0:
            return -x
        else:
            return x
    else:
        return des-curr

def Val(old, curr, des):
    if((old > 0 and curr < 0) or (old < 0 and curr > 0)):
        if(abs(old - des) > 2):
            x = 3.14 - abs(old - des) + 3.14 - abs(curr - des)
            return x
        else:
            return curr - old
    else:
        return curr - old

def error(er):
    if(abs(er > 20)):
        er = 20 * er / abs(er)
    return er


class GazeboAuto(object):

    """Class to handle with gazebo teleop

    Attributes:
        pub (TYPE): ROS publisher
        sub (TYPE): ROS subscriber
    """

    curr_pitch_setting = 0.0
    curr_roll_setting = 0.0

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

        self.pub.subscribe_topic('/auto', Custom)
        self.pub.subscribe_topic('/next_pos', Custom)


    def get_position(self):
        state = self.sub.get_data()['gazebo']['model_states']
        for i in range(2):
            if state['name'][i] == 'BlueRov2':
                x1 = state['pose'][i]['position']['x']
                y1 = state['pose'][i]['position']['y']
                z1 = state['pose'][i]['position']['z']
        pos = [x1, y1, z1]
        return pos

    def get_orientation(self):
        state = self.sub.get_data()['gazebo']['model_states']
        for i in range(2):
            if state['name'][i] == 'BlueRov2':
                ob = state['pose'][i]['orientation']['x']
                oc = state['pose'][i]['orientation']['y']
                od = state['pose'][i]['orientation']['z']
                oa = state['pose'][i]['orientation']['w']
        siny_cosp = 2 * (ob * oc + oa * od)
        cosy_cosp = oa ** 2 + ob ** 2 - oc ** 2 - od ** 2
        yaw = m.atan2(siny_cosp, cosy_cosp)
        return yaw

    def run(self):
        """ Run Gazebo Teleop
        """
        """Run user code
        """
        #dr = 1.5708
        Pr = 0
        Ir = 0
        Dr = 0
        k_py = 250
        k_iy = 1
        k_dy = 50
        oldr = 0
        er = 0

        #d = [2, 7, -11]
        P =[0 for u in range(3)]
        I = [0 for u in range(3)]
        D = [0 for u in range(3)]
        k_p = [390, 300, 170] 
        k_i = [20, 20, 50]
        k_d = [690, 590, 500]
        old = [0 for u in range(3)]
        e = [0 for u in range(3)]

        while not rospy.is_shutdown():
      	    time.sleep(0.1)
            # Try to get data

            try:
                # Get ROV position
                pos = self.get_position()
                yaw = self.get_orientation()

            except Exception as error:
                print ('Get data error model_states:', error)

            try:
                a = self.sub.get_data()['desiredposition']['data']
            except:
                a = [2, 7, -11, 1.5708]

            d =[a[0], a[1], a[2]]
            dr = a[3]

            try:
                dist = abs(m.sqrt((pos[0] - d[0]) ** 2 + (pos[1] - d[1]) ** 2 + (pos[2] - d[2]) ** 2))
                if (dist < 0.2):
                    next_pos = [1]
                else:
                    next_pos = [0]
            
                data = Custom()
                data.id = "fetch"
                data.data = next_pos
                self.pub.set_data('/next_pos', data)

            except Exception as error:
                print ('next_pos error:', error)

            try:
                # calculate yaw towards destination
                if (pos[0] < d[0]):
                    if (pos[1] > d[1]):
                        dir1 = m.atan(abs(d[0] - pos[0]) / abs(d[1] - pos[1]))
                    else:
                        dir1 = m.pi / 2 + m.atan(abs(d[1] - pos[1]) / abs(d[0] - pos[0]))
                else:
                    if (pos[1] < d[1]):
                        dir1 = -m.pi - m.atan(abs(d[0] - pos[0]) / abs(d[1] - pos[1]))
                    else:
                        dir1 = -m.pi / 2 - m.atan(abs(d[1] - pos[1]) / abs(d[0] - pos[0]))

                dist = abs(m.sqrt((pos[0] - d[0]) ** 2 + (pos[1] - d[1]) ** 2 + (pos[2] - d[2]) ** 2))
                if (dist > 2):
                    val1 = Angle(dir1, yaw)
                else:
                    val1 = Angle(dr, yaw)
                Pr = val1 * k_py
                Ir += val1 * k_iy * 0.11
                Dr = -(abs(Val(oldr, val1, dr)) / 0.11) * k_dy * (Pr / abs(Pr))
                er = Pr + Dr + Ir
                oldr = val1

                print val1
                if (val1 < 0.2):
                    for i in range(3):
                        P[i] = (d[i] - pos[i]) * k_p[i]
                        I[i] += (d[i] - pos[i]) * k_i[i] * 0.11
                        D[i] = ((-old[i] + d[i] - pos[i]) / 0.11) * k_d[i]
                        if I[i] > 150 or I[i] < -150:
                            I[i] = 150 * I[i] / abs(I[i])
                        e[i] = P[i] + I[i] + D[i]
                        old[i] = d[i] - pos[i]


                if (abs(e[0]) > 1000):
                    e[0] = 1000 * e[0] / abs(e[0])
                if (abs(e[1]) > 1000):
                    e[1] = 1000 * e[1] / abs(e[1])
                if (abs(e[2]) > 1000):
                    e[2] = 1000 * e[2] / abs(e[2])
                if (abs(er) > 650):
                    er = 650 * er / abs(er)

                forces = [0 for u in range(6)]

                forces[0] = -(e[0] * m.sin(-yaw) + e[1] * m.cos(-yaw)) / 1000 #Surge
                forces[1] = (e[0] * m.cos(-yaw) - e[1] * m.sin(-yaw)) / 1000 #Sway
                forces[2] = e[2] / 1000 #Heave
                forces[3] = 0 #Roll
                forces[4] = 0 #Pitch
                forces[5] = er / 650 #Yaw

                data = Custom()
                data.id = "autonomous"
                data.data = forces
                self.pub.set_data('/auto', data)

            except Exception as error:
                print('set_data "/auto" error:', error)

if __name__ == "__main__":
    try:
        rospy.init_node('gazebo_autonomous', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    gazebo_teleop = GazeboAuto()
    gazebo_teleop.run()
