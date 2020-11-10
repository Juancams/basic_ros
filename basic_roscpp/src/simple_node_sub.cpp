// Copyright 2020 Juan Carlos Manzanares Serrano

#include "ros/ros.h"
#include "std_msgs/Int64.h"

void contadorCallback(const std_msgs::Int64::ConstPtr& msg)
{
  ROS_INFO("Contador: [%ld]", msg->data);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "simple_node_sub");
    ros::NodeHandle n;

    ros::Subscriber sub = n.subscribe("/contador", 1, contadorCallback);

    ros::Rate loop_rate(10);
    
    while (ros::ok())
    {
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}