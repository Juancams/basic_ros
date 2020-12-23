#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

FORWARD = 0.3
STOP = 0

class Publisher():
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.msg = Twist()
        self.msg.linear.x = FORWARD # Avanzar / Retroceder
        self.msg.linear.y = STOP
        self.msg.linear.z = STOP
        self.msg.angular.x = STOP
        self.msg.angular.y = STOP
        self.msg.angular.z = STOP  # Girar

    def step(self):
        self.pub.publish(self.msg)

def main():
    rospy.init_node("robot_forward")

    pub = Publisher()

    rate = rospy.Rate(2)
    while(not rospy.is_shutdown()):
        pub.step()
        rate.sleep()

if __name__ == "__main__":

    try:
        main()
    except rospy.ROSInterruptException:
        pass