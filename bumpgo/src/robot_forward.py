#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class Publisher():
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.msg = Twist()
        self.msg.linear.x = 0.3 # Avanzar / Retroceder
        self.msg.linear.y = 0
        self.msg.linear.z = 0
        self.msg.angular.x = 0
        self.msg.angular.y = 0
        self.msg.angular.z = 0  # Girar

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