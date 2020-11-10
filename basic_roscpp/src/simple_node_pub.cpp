// Copyright 2020 Juan Carlos Manzanares Serrano

#include "ros/ros.h"
#include "std_msgs/Int64.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "simple_node_pub");
    ros::NodeHandle n;

    ros::Publisher pub = n.advertise<std_msgs::Int64>("/contador", 1);

    ros::Rate loop_rate(10);

    int count = 0;

    while (ros::ok())
    {
        std_msgs::Int64 msg;
        msg.data = count++;

        pub.publish(msg);

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}