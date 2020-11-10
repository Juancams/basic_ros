#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

class Publisher():
    def __init__(self):
        self.pub = rospy.Publisher("/contador", Int32, queue_size=1)
        self.msg = Int32()

    def doWork(self):
        self.pub.publish(self.msg)
        self.msg.data += 1

def main():
    rospy.init_node("simple_node_pub_obj")

    pub = Publisher()

    rate = rospy.Rate(2)
    while(not rospy.is_shutdown()):
        pub.doWork()
        rate.sleep()

if __name__ == "__main__":

    try:
        main()
    except rospy.ROSInterruptException:
        pass