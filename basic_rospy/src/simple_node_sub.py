#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def contadorCallback(msg):
    rospy.loginfo("Contador: " + str(msg.data))

def main():
    rospy.init_node("simple_node_sub")

    sub = rospy.Subscriber("/contador", Int32, contadorCallback)

    rospy.spin()

if __name__ == "__main__":

    try:
        main()
    except rospy.ROSInterruptException:
        pass
