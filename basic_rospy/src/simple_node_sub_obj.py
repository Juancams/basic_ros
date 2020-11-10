#! /usr/bin/env python3

import sys
import rospy
from std_msgs.msg import Int32

class Subscriber():
    def __init__(self):
        self.sub = rospy.Subscriber("/contador", Int32, self.contadorCallback)

    def contadorCallback(self, msg):
        rospy.loginfo("Contador: " + str(msg.data))

def main(args=None):
    rospy.init_node("simple_node_sub_obj")

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