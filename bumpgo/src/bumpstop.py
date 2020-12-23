#! /usr/bin/env python3

import sys
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

# Declaraciones
FORWARD = 0.3
STOP = 0
UMBRAL = 1.5

class BumpStop():
    def __init__(self):
        self.sub = rospy.Subscriber("/scan", LaserScan, self.laserCallback)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.vel_msg = Twist()
        self.vel_msg.linear.x = STOP
        self.vel_msg.linear.y = STOP
        self.vel_msg.linear.z = STOP
        self.vel_msg.angular.x = STOP
        self.vel_msg.angular.y = STOP
        self.vel_msg.angular.z = STOP  # Girar
        self.bump = False

    def laserCallback(self, msg):
        if (msg.ranges[0] < UMBRAL):
            self.bump = True
        else 
            self.bump = False

    def step(self):
        if (self.bump):
            self.vel_msg.linear.x = STOP
        else:
            self.vel_msg.linear.x = FORWARD

        self.pub.publish(self.vel_msg)

def main(args=None):
    rospy.init_node("bump_stop")

    bump_stop = BumpStop()

    rate = rospy.Rate(1)

    while(not rospy.is_shutdown()):
        bump_stop.step()
        rate.sleep()

    rospy.spin()

if __name__ == "__main__":

    try:
        main(sys.argv)
    except rospy.ROSInterruptException:
        pass