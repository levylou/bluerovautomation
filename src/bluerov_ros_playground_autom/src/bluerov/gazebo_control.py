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
from bluerov_ros_playground.msg import Custom
from mavros_msgs.srv import CommandBool
from sensor_msgs.msg import Joy, JointState
from std_msgs.msg import Float32
from gazebo_msgs.msg import ModelStates
 
class Control(object):
    def __init__(self):
        super(Control, self).__init__()

        # Do what is necessary to start the process
        # and to leave gloriously

        self.sub = subs.Subs()
        self.pub = pubs.Pubs()

	self.sub.subscribe_topic('/act', Custom)
    	self.sub.subscribe_topic('/auto', Custom)
	self.sub.subscribe_topic('/joy', Joy)
        self.sub.subscribe_topic('/gazebo/model_states', ModelStates)

        self.pub.subscribe_topic('/BlueRov2/thruster_command', JointState)

    def run(self):
        """Sends control input to Gazebo by setting appropriate levels of PWM
           in the /BlueRov2/thruster_comand
           Inputs: -1.0...1.0 for each of the force and yaw axis
                    (it corresponds to the desired velocity level)
                    (the unit is arbitrary)
        """
        state = False
        state_a = False
        while not rospy.is_shutdown():
            time.sleep(0.1)	

            try:    
                #receive data from /auto or /act
                but = self.sub.get_data()['joy']['buttons']	
                if (but[0] == 1):
                    state_a = not state_a
                    print ("auto oder joy")

                if (state != state_a):
                    #print ("autonomous")
                    if (self.sub.get_data()['auto']['id'] == "autonomous"):
                        a = self.sub.get_data()['auto']['data']

                else:
                    print ("joystick")
                    if (self.sub.get_data()['act']['id'] == "joystick"):
                        a = self.sub.get_data()['act']['data']

                # gegenkraft aufbringen
                model = self.sub.get_data()['gazebo']['model_states']['name']
                for i in range(2):
                    state_tw = self.sub.get_data()['gazebo']['model_states']['twist'][i]
                    state_po = self.sub.get_data()['gazebo']['model_states']['pose'][i]
                    if model[i] == 'BlueRov2':
                        vxg = state_tw['linear']['x']
                        vyg = state_tw['linear']['y']
                        vzg = state_tw['linear']['z']
                        rxg = state_tw['angular']['x']
                        ryg = state_tw['angular']['y']
                        rzg = state_tw['angular']['z']
                        qb = state_po['orientation']['x']
                        qc = state_po['orientation']['y']
                        qd = state_po['orientation']['z']
                        qa = state_po['orientation']['w']

                # Einheitsquaternion
                z = m.sqrt(qa ** 2 + qb ** 2 + qc ** 2 + qd ** 2)
                qa = qa / z
                qb = qb / z
                qc = qc / z
                qd = qd / z

                # Rotationsmatrix aus Quaternionen
                R11 = qa ** 2 + qb ** 2 - qc ** 2 - qd ** 2
                R12 = 2 * (qb * qc - qa * qd)
                R13 = 2 * (qb * qd + qa * qc)

                R21 = 2 * (qb * qc + qa * qd)
                R22 = qa ** 2 - qb ** 2 + qc ** 2 - qd ** 2
                R23 = 2 * (qc * qd - qa * qb)

                R31 = 2 * (qb * qd - qa * qc)
                R32 = 2 * (qc * qd + qa * qb)
                R33 = qa ** 2 - qb ** 2 - qc ** 2 + qd ** 2

                vy = vxg * R11 + vyg * R12 + vzg * R13
                vx = vxg * R21 + vyg * R22 + vzg * R23
                vz = -(vxg * R31 + vyg * R32 + vzg * R33)

                ry = rxg * R11 + ryg * R12 + rzg * R13
                rx = rxg * R21 + ryg * R22 + rzg * R23
                rz = -(rxg * R31 + ryg * R32 + rzg * R33)

                d = [0 for u in range(6)]
                twist = [vx, vy, vz, rx, ry, rz]
                k = 0.4

                for i in range(6):
                    d[i] = k * 0.5 * 997 * twist[i] ** 2 * 0.34 * 0.25
                    if twist[i] < 0:
                        d[i] = d[i] * -1
                
                drag = [0 for u in range(6)]

                drag[0] = +d[0] +d[5] +d[1]
                drag[1] = +d[0] -d[5] -d[1]
                drag[2] = -d[0] -d[5] +d[1]
                drag[3] = -d[0] +d[5] -d[1]
                drag[4] = +d[2] +d[3]
                drag[5] = +d[2] -d[3]

                thrust = [0 for u in range(6)]

                thrust[0] = +a[0] +a[5] +a[1]
                thrust[1] = +a[0] -a[5] -a[1]
                thrust[2] = -a[0] -a[5] +a[1]
                thrust[3] = -a[0] +a[5] -a[1]
                thrust[4] = +a[2] +a[3]
                thrust[5] = +a[2] -a[3]

                forces = [0 for u in range(6)]

                for i in range(6):
                    forces[i] = thrust[i] - drag[i]

                joint = JointState()
                joint.name = ["thr{}".format(u + 1) for u in range(6)]
                joint.position = [pwm for pwm in forces]

		self.pub.set_data('/BlueRov2/thruster_command', joint)
	    except Exception as error:	
                print('send forces error:', error)

if __name__ == "__main__":
    try:
        rospy.init_node('gazebo_control', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    code = Control()
    code.run()
