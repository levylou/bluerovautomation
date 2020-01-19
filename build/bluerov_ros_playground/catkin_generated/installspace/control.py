#!/usr/bin/env python2

import rospy
import time
import math as m

try:
    import pubs
    import subs
except:
    import bluerov.pubs as pubs
    import bluerov.subs as subs

from mavros_msgs.msg import OverrideRCIn
from bluerov_ros_playground.msg import Custom
from sensor_msgs.msg import Joy
from mavros_msgs.srv import CommandBool


class Control(object):

    def __init__(self):
        super(Control, self).__init__()

        # Do what is necessary to start the process
        # and to leave gloriously

        self.arm()

        self.sub = subs.Subs()
        self.pub = pubs.Pubs()

        self.pub.subscribe_topic('/mavros/rc/override', OverrideRCIn)

        self.sub.subscribe_topic('/auto', Custom)
        self.sub.subscribe_topic('/act', Custom)
        self.sub.subscribe_topic('/joy', Joy)
        self.sub.subscribe_topic('/mavros/battery', BatteryState)
        self.sub.subscribe_topic('/mavros/rc/in', RCIn)
        self.sub.subscribe_topic('/mavros/rc/out', RCOut)
        self.sub.subscribe_topic('/mavros/imu/static_pressure', FluidPressure)
        self.sub.subscribe_topic('/mavros/imu/diff_pressure', FluidPressure)

        self.cam = None

        try:
            video_udp_port = rospy.get_param("/user_node/video_udp_port")
            rospy.loginfo("video_udp_port: {}".format(video_udp_port))
            self.cam = video.Video(video_udp_port)
        except Exception as error:
            rospy.loginfo(error)
            self.cam = video.Video()

    def arm(self):
        """ Arm the vehicle and trigger the disarm
        """
        rospy.wait_for_service('/mavros/cmd/arming')

        self.arm_service = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        self.arm_service(True)

        # Disarm is necessary when shutting down
        rospy.on_shutdown(self.disarm)

    def disarm(self):
        self.arm_service(False)

    def run(self):
        """Sends control input to the robot by setting appropriate levels of PWM
           in the /mavros/rc/override
           Inputs: -1.0...1.0 for each of the force and torque axis
                    (it corresponds to the desired velocity level)
                    (the unit is arbitrary)
                    camupdown is in the same range, deciding if the camera should be
                    pitched a step down or a step up
        """
        state = False
        state_a = False
        while not rospy.is_shutdown():
            time.sleep(0.1)

            # Try to get data
            try:
                rospy.loginfo(self.sub.get_data()['mavros']['battery']['voltage'])
                rospy.loginfo("Static pressure: %f"%self.sub.get_data()['mavros']['imu']['static_pressure']['fluid_pressure'])
                rospy.loginfo("Diff pressure: %f"%self.sub.get_data()['mavros']['imu']['diff_pressure']['fluid_pressure'])
            except Exception as error:
                print('Get data error:', error)

            try:
                #receive data from /auto or /act
                but = self.sub.get_data()['joy']['buttons']	
                if (but[0] == 1):
                    state_a = not state_a
                if(state != state_a):
                    print ("autonomous")
                    if (self.sub.get_data()['auto']['id'] == "autonomous"):
                        a = self.sub.get_data()['auto']['data']
                else:
                    print ("joystick")
                    if (self.sub.get_data()['act']['id'] == "joystick"):
                        a = self.sub.get_data()['act']['data']	
                # rc run between 1100 and 2000, a joy command is between -1.0 and 1.0
                # Correction SK:  1100 and 1900
                #override = [int(val*400 + 1500) for val in joy]
                #for _ in range(len(override), 8):
                #override.append(0)

                # Not implemented in MAVLink apparently:
                override = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
                # Surge = Channel 5	
                override[4] = int(a[0] * 400 + 1500)
                # Sway = Channel 6
                override[5] = int(a[1] * 400 + 1500)
                # Heave = Channel 3
                override[2] = int(a[2] * 400 + 1500)
                # Roll = Channel 2
                override[1] = int(a[3] * 400 + 1500)
                # Pitch = Channel 1
                override[0] = int(a[4] * 400 + 1500)
                # Yaw = Channel 4
                override[3] = int(a[5] * 400 + 1500)
                # Cam up = Channel 8
                #override[7] = int(a[6] * 400 + 1500)

                # Unused:
                # Ch 1 = Pitch
                # Ch 2 = Roll
                # Ch 7 = ?
                # Not implemented in MAVLink apparently:
                # Lights 1 & 2
                #override[8] = int(joy[6]*400 + 1500)
                #override[9] = int(joy[6]*400 + 1500)
                # Send joystick data as rc output into rc override topic
                # (fake radio controller)

                self.pub.set_data('/mavros/rc/override', override)

            except Exception as error:
                print('joy error:', error)

            try:
                if not self.cam.frame_available():
                    continue
                # Show video output
                frame = self.cam.frame()
                # Added code SK
                height, width, depth = frame.shape
                newframe = cv2.resize(frame,(int(width*0.65),int(height*0.65)))
                cv2.imshow('frame', newframe)
                #cv2.imshow('frame', frame)
                cv2.waitKey(1)
            except Exception as error:
                print('imshow error:', error)
        
if __name__ == "__main__":
    try:
        rospy.init_node('control_node', log_level=rospy.DEBUG)
    except rospy.ROSInterruptException as error:
        print('pubs error with ROS: ', error)
        exit(1)
    code = Control()
    code.run()
