#! /usr/bin/env python3

import sys
import rospy
from sensor_msgs.msg import LaserScan

class Subscriber():
    def __init__(self):
        self.sub = rospy.Subscriber("/scan", LaserScan, self.laserCallback)

    def laserCallback(self, msg):
        rospy.loginfo("Medida del laser: " + str(msg.ranges[180]))

def main(args=None):
    rospy.init_node("laser_node")

    sub = Subscriber()

    rate = rospy.Rate(1)

    while(not rospy.is_shutdown()):
        rate.sleep()

    rospy.spin()

if __name__ == "__main__":

    try:
        main(sys.argv)
    except rospy.ROSInterruptException:
        pass