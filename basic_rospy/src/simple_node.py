#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def main():
    rospy.init_node("simple_node")

    rospy.spin()

if __name__ == "__main__":

    try:
        main()
    except rospy.ROSInterruptException:
        pass
