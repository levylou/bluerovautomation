#!/usr/bin/env python

import cv2
import rospy
import time
import math as m
try:
    import pubs
    import subs
    import video
except:
    import bluerov.pubs as pubs
    import bluerov.subs as subs
    import bluerov.video as video

from mavros_msgs.srv import CommandBool
from sensor_msgs.msg import Joy
from nav_msgs.msg import Odometry
from mavros_msgs.msg import OverrideRCIn , RCIn, RCOut
from std_msgs.msg import Float32
from bluerov_ros_playground.msg import Custom
from geometry_msgs.msg import PointStamped, TwistStamped

def Angle(des, curr):
    #calculating the angle between desired and current yaw
    x = m.pi - abs(des) + m.pi - abs(curr)
    if abs(des - curr) > x:
        if (des-curr)>0:
            return x
        else:
            return -x
    else:
        return curr-des

def Val(old, curr, des):
    if ((old > 0 and curr < 0) or (old < 0 and curr > 0)):
        if (abs(old - des) > 2):
            x = m.pi - abs(old - des) + m.pi - abs(curr - des)
            return x
        else:
            return curr - old
    else:
        return curr - old

def error(er):
    if (abs(er > 20)):
        er = 20 * er / abs(er)
    return er

class Auto(object):

    """Class to provide user access

    Attributes:
        cam (Video): Video object, get video stream
        pub (Pub): Pub object, do topics publication
        sub (Sub): Sub object, subscribe in topics
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
        super(Auto, self).__init__()

        self.sub = subs.Subs()
        self.pub = pubs.Pubs()

	self.pub.subscribe_topic('/auto', Custom)
        self.pub.subscribe_topic('/next_pos', Custom)

        self.sub.subscribe_topic('/joy', Joy)
	self.sub.subscribe_topic('/odom', Odometry)
	self.sub.subscribe_topic('/odometry/filtered', Odometry)
	self.sub.subscribe_topic('/waterlinked/acoustic_position/filtered', PointStamped)
        self.sub.subscribe_topic('/mavros/local_position/velocity_body', TwistStamped)
        self.sub.subscribe_topic('/desiredposition', Custom)
        self.sub.subscribe_topic('/depth', Float32)

    def send_forces(self, su, sw, he, ro, pi, ya, yaw):

        if (abs(su) > 0.4):
            su = 0.4 * su / abs(su)
        if (abs(sw) > 0.4):
            sw = 0.4 * sw / abs(sw)
        if (abs(he) > 0.4):
            he = 0.4 * he / abs(he)
        if (abs(ya) > 0.5):
            ya = 0.5 * ya / abs(ya)

        forces = [0 for u in range(6)]

        forces[0] = (su * m.sin(-yaw) + sw * m.cos(-yaw)) #/ 1000  #sw / (1300) * (1 - ya / 950) #Surge
        forces[1] = -(su * m.cos(-yaw) - sw * m.sin(-yaw)) #/ 1000 #(1 - ya / 950) * su / 1300 #Sway
        forces[2] = he #/ 2000 #Heave
        forces[3] = ro #Roll
        forces[4] = pi #Pitch
        forces[5] = -ya #Yaw

        data = Custom()
        data.id = "autonomous"
        data.data = forces
        self.pub.set_data('/auto', data)

    def run(self):
        """Run user code
        """

        #pid variables rotational
	Pr = 0
	Ir = 0
	Dr = 0
	#k_py = 250
	#k_iy = 1
	#k_dy = 50
	k_py = 0.14 # evaluated while Integral and derivative part where disabled
	k_iy = 0.001
	k_dy = 0.001
	er = 0
	oldr = 0

        #pid variables translational
	P =[0 for u in range(3)]
	I = [0 for u in range(3)]
	D = [0 for u in range(3)]
	#k_p = [390, 300, 170] 
	#k_i = [20, 20, 50]
	#k_d = [690, 590, 500]
	#k_p = [0.4, 0.4, 0.25] 
	#k_i = [0.0001, 0.0001, 0.0015]
	#k_d = [0.1, 0.1, 0.2]
	k_p = [0.35, 0.3, 0.3] 
	k_i = [0, 0, 0.0018]
	k_d = [5, 5, 0.04]
        I_lim = [0.15, 0.15, 0.1]
	e = [0 for u in range(3)]
	old = [0 for u in range(3)]

        while not rospy.is_shutdown():
            time.sleep(0.1)

            # Try to get data
            try:
                a = self.sub.get_data()['desiredposition']['data']
            except:
                a = [-2, 2, -1.5, 0]

            d = [a[0], a[1], a[2]]
            dr = a[3]

            try:
                # Get joystick data
                joy = self.sub.get_data()['joy']['axes']
                but = self.sub.get_data()['joy']['buttons']
                # Get ROV odometry and twist
                pos1 = self.sub.get_data()['waterlinked']['acoustic_position']['filtered']['point']
                pos2 = self.sub.get_data()['odometry']['filtered']['pose']['pose']['position']
                q = self.sub.get_data()['odometry']['filtered']['pose']['pose']['orientation']
                vel = self.sub.get_data()['mavros']['local_position']['velocity_body']['twist']['linear']
                z = self.sub.get_data()['depth']['data']

                # decide wether pose info taken from ekf or waterlinked directly. due to bad imu data when vehicle moves slow, ekf only functions properly at higher velocities
                v = m.sqrt(vel['x'] ** 2 + vel['y'] ** 2 + vel['z'] ** 2)
                dist = abs(m.sqrt((pos1['x'] - d[0]) ** 2 + (pos1['y'] - d[1]) ** 2 + (z - d[2]) ** 2))
                if (dist > 2 and v >1 ):
                    pos = [-pos2['y'], pos2['x'], z]
                else:
                    pos = [pos1['x'], pos1['y'], z]

                # Converting button presses to roll and pitch setting modification
                self.curr_pitch_setting = self.enforce_limit(self.curr_pitch_setting - joy[7] * 0.1)
                self.curr_roll_setting = self.enforce_limit(self.curr_roll_setting - joy[6] * 0.1)
                if (but[4] == 1):
                    self.curr_pitch_setting = 0.0
                if (but[5] == 1):
                    self.curr_roll_setting = 0.0
                roll = self.curr_roll_setting
                pitch = self.curr_pitch_setting

                siny_cosp = +2.0 * (q['w'] * q['z'] + q['x'] * q['y'])
                cosy_cosp = +1.0 - 2.0 * (q['y'] * q['y'] + q['z'] * q['z'])  
                posr = m.atan2(siny_cosp, cosy_cosp)
                print posr

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

                val1 = Angle(dr, posr)
                Pr = val1 * k_py
                Ir += val1 * k_iy
                Dr = -abs(Val(oldr, val1, dr)) * k_dy * (Pr / abs(Pr))
                if abs(Ir) > 0.1:
                    Ir = 0.1 * Ir / abs(Ir)
                if val1 > 0.5:
                    Ir = 0
                er = Pr + Ir + Dr 
                oldr = val1

                for i in range(3):
                    P[i] = (d[i] - pos[i]) * k_p[i]
                    I[i] += (d[i] - pos[i]) * k_i[i]
                    D[i] = (d[i] - pos[i] -old[i]) * k_d[i]
                    if abs(I[i]) > I_lim[i]:
                        I[i] = I_lim[i] * I[i] / abs(I[i])
                    e[i] = P[i] + I[i] + D[i]
                    old[i] = d[i] - pos[i]

                self.send_forces(e[0], e[1], e[2], roll, pitch, er, posr)

                if (abs(m.sqrt((d[0] - pos[0]) ** 2 + (d[1] - pos[1]) ** 2)) < 0.2):
                    next = [1]
                else:
                    next = [0]

                data = Custom()
                data.id = "fetch"
                data.data = next
                self.pub.set_data('/next_pos', data)

            except Exception as error:
                print('send data /auto error:', error)

if __name__ == "__main__":
    try:
        rospy.init_node('auto_node', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    code = Auto()
    code.run()

