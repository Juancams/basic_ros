// Copyright 2020 Juan Carlos Manzanares Serrano

#include "ros/ros.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "simple_node");
    ros::NodeHandle n;

    ros::spin();

    return 0;
}