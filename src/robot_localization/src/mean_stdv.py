#! /usr/bin/env python

import rospy
import math
import time
from nav_msgs.msg import Odometry

vx = []
vy = []
vz = []
a = 0
sumx = 0
sumy = 0
sumz = 0
sumvarx = 0
sumvary = 0
sumvarz = 0

def mean_stdv(msg):
        global a, vx, vy, vz, sumx, sumy, sumz, sumvarx, sumvary, sumvarz
        

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z

        if a < 5:
            sumx += x
            sumy += y
            sumz += z
            vx.append(x)
            vy.append(y)
            vz.append(z)
            a += 1
            print a
   
        if a >= 5:
            sumx = sumx - vx[0] + x
            sumy = sumy - vy[0] + y
            sumz = sumz - vz[0] + z
            vx.pop(0)
            vy.pop(0)
            vz.pop(0)
            vx.append(x)
            vy.append(y)
            vz.append(z)
       
            meanx = sumx / len(vx)
            meany = sumy / len(vy)
            meanz = sumz / len(vz)

            for i in vx:
                sumvarx += (meanx - i) * (meanx - i)
            for i in vy:
                sumvary += (meany - i) * (meany - i)
            for i in vz:
                sumvarz += (meanz - i) * (meanz - i)
        
            stdx = math.sqrt(sumvarx / len(vx))
            stdy = math.sqrt(sumvary / len(vy))
            stdz = math.sqrt(sumvarz / len(vz))

            #print('meanx =', meanx, 'meany =', meany, 'meanz =', meanz)
            #print('stdx =', stdx, 'stdy =', stdy, 'stdz =', stdz) 
            #print('')
            
            sumvarx = 0
            sumvary = 0
            sumvarz = 0

def subscriber():

    rospy.init_node("accuracy_check")

    rospy.Subscriber("/odometry/filtered", Odometry, mean_stdv)

    rospy.spin()

if __name__ == '__main__':
    subscriber()
