#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node("simple_node_pub")

    pub = rospy.Publisher("/contador", Int32, queue_size=1)

    msg = Int32()
    msg.data = 0

    rate = rospy.Rate(2)
    while(not rospy.is_shutdown()):
        pub.publish(msg)
        msg.data += 1
        rate.sleep()

    rospy.spin()

if __name__ == "__main__":

    try:
        main()
    except rospy.ROSInterruptException:
        pass
