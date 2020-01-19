#!/usr/bin/env python

from __future__ import print_function
# ROS module
import rospy
# Mavlink ROS messages
from mavros_msgs.msg import Mavlink
from std_msgs.msg import Float32
# pack and unpack functions to deal with the bytearray
from struct import pack, unpack
import requests
import argparse
import time
import logging


log = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
pub = rospy.Publisher('depth', Float32)

# Topic callback
def callback(data):

    # Check if message id is valid
    if data.msgid == 137:
        #rospy.loginfo(rospy.get_caller_id() + " Package: %s", data)
        # Transform the payload in a python string
        p = pack("QQ", *data.payload64)
        # Transform the string in valid values
        # https://docs.python.org/2/library/struct.html
        time_boot_ms, press_abs, press_diff, temperature = unpack("Iffhxx", p)
        # print(time_boot_ms, press_abs, press_diff, temperature)
        # temp usually shows a value around 4000. needs to be converted somehow

        depth = (1013 - press_abs) / 98.0665
        print('depth:', depth, 'm')
	pub.publish(depth)
        temp = temperature
	temp = 20.0
        url = 'http://192.168.2.94/api/v1/external/depth' #'http://demo.waterlinked.com/api/v1/external/depth'

        payload = dict(depth=float(depth), temp=float(temp))
        r = requests.put(url, json=payload, timeout=10)
	#print(r.status_code)
        if r.status_code != 200:
        	log.error("Error setting depth: {} {}".format(r.status_code, r.text))
        	#print("Error setting depth: {} {}".format(r.status_code, r.text))

    
def listener():  

    rospy.init_node("send_depth_node", anonymous=True)
    rospy.Subscriber("/mavlink/from", Mavlink, callback)
    rospy.spin()

if __name__ == '__main__':

    listener()
