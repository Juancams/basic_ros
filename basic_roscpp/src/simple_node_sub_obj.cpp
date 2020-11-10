// Copyright 2020 Juan Carlos Manzanares Serrano

#include "ros/ros.h"
#include "std_msgs/Int64.h"

class Suscriptor
{
public:
    Suscriptor()
    {
        sub = n.subscribe("/contador", 1, &Suscriptor::contadorCallback, this);
    }

    void contadorCallback(const std_msgs::Int64::ConstPtr& msg)
    {
        ROS_INFO("Contador: [%ld]", msg->data);
    }

private:
    ros::NodeHandle n;

    ros::Subscriber sub;
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "simple_node_sub_obj");

    Suscriptor sub;

    ros::spin();

    return 0;
}