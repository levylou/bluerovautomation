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
        self.sub.subscribe_topic('/autoI', Custom)
        self.sub.subscribe_topic('/autoII', Custom)
	self.sub.subscribe_topic('/joy', Joy)
        self.sub.subscribe_topic('/gazebo/model_states', ModelStates)

        self.pub.subscribe_topic('/BlueRov2/thruster_command', JointState)
        self.pub.subscribe_topic('/BlueRov2II/thruster_command', JointState)

    def run(self):
        """Sends control input to Gazebo by setting appropriate levels of PWM
           in the /BlueRov2/thruster_command and /BlueRov2II/thruster_command
           Inputs: -1.0...1.0 for each of the force and yaw axis
                    (it corresponds to the desired velocity level)
                    (the unit is arbitrary)
        """
	state = False
	state_a = False #autonomous oder joystick
        state_b = False #beide ROVs oder ein ROV
        state_c = False #falls einzeln welches ROV
        qa = [0 for u in range(2)]
        qb = [0 for u in range(2)]
        qc = [0 for u in range(2)]
        qd = [0 for u in range(2)]
        vxg = [0 for u in range(2)]
        vyg = [0 for u in range(2)]
        vzg = [0 for u in range(2)]
        rxg = [0 for u in range(2)]
        ryg = [0 for u in range(2)]
        rzg = [0 for u in range(2)]
        z1 = [0 for u in range(2)]
        R11 = [0 for u in range(2)]
        R12 = [0 for u in range(2)]
        R13 = [0 for u in range(2)]
        R21 = [0 for u in range(2)]
        R22 = [0 for u in range(2)]
        R23 = [0 for u in range(2)]
        R31 = [0 for u in range(2)]
        R32 = [0 for u in range(2)]
        R33 = [0 for u in range(2)]
        vx = [0 for u in range(2)]
        vy = [0 for u in range(2)]
        vz = [0 for u in range(2)]
        rx = [0 for u in range(2)]
        ry = [0 for u in range(2)]
        rz = [0 for u in range(2)]
        forcesI = [0 for u in range(6)]
        forcesII = [0 for u in range(6)]
        thrust = [0 for u in range(6)]
        thrustI = [0 for u in range(6)]
        thrustII = [0 for u in range(6)]

	while not rospy.is_shutdown():
	    time.sleep(0.1)	
			
	    try:
                # gegenkraft aufbringen
                model = self.sub.get_data()['gazebo']['model_states']['name']
                for i in range(3):
                    state_tw = self.sub.get_data()['gazebo']['model_states']['twist'][i]
                    state_po = self.sub.get_data()['gazebo']['model_states']['pose'][i]
                    if model[i] == 'BlueRov2':
                        vxg[0] = state_tw['linear']['x']
                        vyg[0] = state_tw['linear']['y']
                        vzg[0] = state_tw['linear']['z']
                        rxg[0] = state_tw['angular']['x']
                        ryg[0] = state_tw['angular']['y']
                        rzg[0] = state_tw['angular']['z']
                        qb[0] = state_po['orientation']['x']
                        qc[0] = state_po['orientation']['y']
                        qd[0] = state_po['orientation']['z']
                        qa[0] = state_po['orientation']['w']

                    if model[i] == 'BlueRov2II':
                        vxg[1] = state_tw['linear']['x']
                        vyg[1] = state_tw['linear']['y']
                        vzg[1] = state_tw['linear']['z']
                        rxg[1] = state_tw['angular']['x']
                        ryg[1] = state_tw['angular']['y']
                        rzg[1] = state_tw['angular']['z']
                        qb[1] = state_po['orientation']['x']
                        qc[1] = state_po['orientation']['y']
                        qd[1] = state_po['orientation']['z']
                        qa[1] = state_po['orientation']['w']

                for i in range(2):
                    # Einheitsquaternion
                    z1[i] = m.sqrt(qa[i] ** 2 + qb[i] ** 2 + qc[i] ** 2 + qd[i] ** 2)
                    qa[i] = qa[i] / z1[i]
                    qb[i] = qb[i] / z1[i]
                    qc[i] = qc[i] / z1[i]
                    qd[i] = qd[i] / z1[i]

                    # Rotationsmatrix aus Quaternionen
                    R11[i] = qa[i] ** 2 + qb[i] ** 2 - qc[i] ** 2 - qd[i] ** 2
                    R12[i] = 2 * (qb[i] * qc[i] - qa[i] * qd[i])
                    R13[i] = 2 * (qb[i] * qd[i] + qa[i] * qc[i])

                    R21[i] = 2 * (qb[i] * qc[i] + qa[i] * qd[i])
                    R22[i] = qa[i] ** 2 - qb[i] ** 2 + qc[i] ** 2 - qd[i] ** 2
                    R23[i] = 2 * (qc[i] * qd[i] - qa[i] * qb[i])

                    R31[i] = 2 * (qb[i] * qd[i] - qa[i] * qc[i])
                    R32[i] = 2 * (qc[i] * qd[i] + qa[i] * qb[i])
                    R33[i] = qa[i] ** 2 - qb[i] ** 2 - qc[i] ** 2 + qd[i] ** 2

                    vy[i] = vxg[i] * R11[i] + vyg[i] * R12[i] + vzg[i] * R13[i]
                    vx[i] = vxg[i] * R21[i] + vyg[i] * R22[i] + vzg[i] * R23[i]
                    vz[i] = -(vxg[i] * R31[i] + vyg[i] * R32[i] + vzg[i] * R33[i])

                    ry[i] = rxg[i] * R11[i] + ryg[i] * R12[i] + rzg[i] * R13[i]
                    rx[i] = rxg[i] * R21[i] + ryg[i] * R22[i] + rzg[i] * R23[i]
                    rz[i] = -(rxg[i] * R31[i] + ryg[i] * R32[i] + rzg[i] * R33[i])

                twistI = [vx[0], vy[0], vz[0], rx[0], ry[0], rz[0]]
                twistII = [vx[1], vy[1], vz[1], rx[1], ry[1], rz[1]]
                dI = [0 for u in range(6)]
                dII = [0 for u in range(6)]
                k = 0.2

                for i in range(6):
                    dI[i] = k * 0.5 * 997 * twistI[i] ** 2 * 0.34 * 0.25
                    dII[i] = k * 0.5 * 997 * twistII[i] ** 2 * 0.34 * 0.25
                    if twistI[i] < 0:
                        dI[i] = dI[i] * -1
                    if twistII[i] < 0:
                        dII[i] = dII[i] * -1

                dragI = [0 for u in range(6)]
                dragII = [0 for u in range(6)]

                dragI[0] = +dI[0] +dI[5] +dI[1]
                dragI[1] = +dI[0] -dI[5] -dI[1]
                dragI[2] = -dI[0] -dI[5] +dI[1]
                dragI[3] = -dI[0] +dI[5] -dI[1]
                dragI[4] = +dI[2] +dI[3]
                dragI[5] = +dI[2] -dI[3]

                dragII[0] = +dII[0] +dII[5] +dII[1]
                dragII[1] = +dII[0] -dII[5] -dII[1]
                dragII[2] = -dII[0] -dII[5] +dII[1]
                dragII[3] = -dII[0] +dII[5] -dII[1]
                dragII[4] = +dII[2] +dII[3]
                dragII[5] = +dII[2] -dII[3]

                #receive data from /auto or /act
	        but = self.sub.get_data()['joy']['buttons']	
		if (but[0] == 1):
		    state_a = not state_a
                    print ("auto oder joy")

		if (state != state_a):
                    print ("autonomous")
		    if (self.sub.get_data()['autoI']['id']=="autonomous"):
		        thrustI = self.sub.get_data()['autoI']['data']

                    for i in range(6):
                        forcesI[i] = thrustI[i] - dragI[i]
                    jointI = JointState()
                    jointI.name = ["thr{}".format(u + 1) for u in range(6)]
                    jointI.position = [pwm for pwm in forcesI]

                    if(self.sub.get_data()['autoII']['id']=="autonomous"):
                        thrustII = self.sub.get_data()['autoII']['data']

                    for i in range(6):
                        forcesII[i] = thrustII[i] - dragII[i]
                    jointII = JointState()
                    jointII.name = ["thr{}".format(u + 1) for u in range(6)]
                    jointII.position = [pwm for pwm in forcesII]

                    self.pub.set_data('/BlueRov2/thruster_command', jointI)
                    self.pub.set_data('/BlueRov2II/thruster_command', jointII)

		else:
                    print ("joystick")
		    but = self.sub.get_data()['joy']['buttons']
                    if (but[1] == 1):
                        state_b = not state_b
                        print ("beide oder eins")
                    but = self.sub.get_data()['joy']['buttons']
                    if (but[2] == 1):
                        state_c = not state_c
                        print ("I oder II")
                    if (self.sub.get_data()['act']['id']=="joystick"):
			a = self.sub.get_data()['act']['data']
		
                    thrust[0] = +a[0] +a[5] +a[1]
                    thrust[1] = +a[0] -a[5] -a[1]
                    thrust[2] = -a[0] -a[5] +a[1]
                    thrust[3] = -a[0] +a[5] -a[1]
                    thrust[4] = +a[2] +a[3]
                    thrust[5] = +a[2] -a[3]

                    if(state != state_b):
                        if(state != state_c):
                            print("ROV1")

                            for i in range(6):
                                forcesI[i] = thrust[i] - dragI[i]
                            joint = JointState()
                            joint.name = ["thr{}".format(u + 1) for u in range(6)]
                            joint.position = [pwm for pwm in forcesI]
                            self.pub.set_data('/BlueRov2/thruster_command', joint)

                        else:
                            print("ROV2")

                            for i in range(6):
                                forcesII[i] = thrust[i] - dragII[i]
                            joint = JointState()
                            joint.name = ["thr{}".format(u + 1) for u in range(6)]
                            joint.position = [pwm for pwm in forcesII]
                            self.pub.set_data('/BlueRov2II/thruster_command', joint)

                    else:
                        print("ROV1 + ROV2")
                        model = self.sub.get_data()['gazebo']['model_states']['name']
                        for i in range(3):
                            pos = self.sub.get_data()['gazebo']['model_states']['pose'][i]['position']
                            if model[i] == 'BlueRov2':
                                xI = pos['x']
                                yI = pos['y']
                                zI = pos['z']
                            if model[i] == 'BlueRov2II':
                                xII = pos['x']
                                yII = pos['y']
                                zII = pos['z']                            

                        thrustI[0] = +a[0] +a[5] +a[1]
                        thrustI[1] = +a[0] -a[5] -a[1]
                        thrustI[2] = -a[0] -a[5] +a[1]
                        thrustI[3] = -a[0] +a[5] -a[1]
                        thrustI[4] = +a[2] +a[3]
                        thrustI[5] = +a[2] -a[3]

                        thrustII[0] = +a[0] +a[5] +a[1]
                        thrustII[1] = +a[0] -a[5] -a[1]
                        thrustII[2] = -a[0] -a[5] +a[1]
                        thrustII[3] = -a[0] +a[5] -a[1]
                        thrustII[4] = +a[2] +a[3]
                        thrustII[5] = +a[2] -a[3]

                        #dist = m.sqrt((xI-xII) ** 2 + (yI-yII) ** 2)
                        #if dist >= 4:
                        #    thrustI[0]= thrustI[0] + a[5] * 0.31415
                        #    thrustI[1]= thrustI[1] - a[5] * 0.31415
                        #    thrustI[2]= thrustI[2] - a[5] * 0.31415
                        #    thrustI[3]= thrustI[3] + a[5] * 0.31415
                        #    thrustII[0]= thrustII[0] + a[5] * 0.31415
                        #    thrustII[1]= thrustII[1] - a[5] * 0.31415
                        #    thrustII[2]= thrustII[2] - a[5] * 0.31415
                        #    thrustII[3]= thrustII[3] + a[5] * 0.31415

                        for i in range(6):
                            forcesI[i] = thrustI[i] - dragI[i]
                            forcesII[i] = thrustII[i] - dragII[i]

                        jointI = JointState()
                        jointI.name = ["thr{}".format(u + 1) for u in range(6)]
                        jointI.position = [pwm for pwm in forcesI]

                        jointII = JointState()
                        jointII.name = ["thr{}".format(u + 1) for u in range(6)]
                        jointII.position = [pwm for pwm in forcesII]

		        self.pub.set_data('/BlueRov2/thruster_command', jointI)
                        self.pub.set_data('/BlueRov2II/thruster_command', jointII)

	    except Exception as error:	
                print('joy error:', error)

if __name__ == "__main__":
    try:
        rospy.init_node('gazebo_control_II', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    code = Control()
    code.run()
