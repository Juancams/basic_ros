// Copyright 2020 Juan Carlos Manzanares Serrano

#include "ros/ros.h"
#include "std_msgs/Int64.h"

class Publicador
{
public:
    Publicador()
    {
        pub = n.advertise<std_msgs::Int64>("/contador", 1);
    }

    void do_work()
    {
        std_msgs::Int64 msg;

        msg.data = count++;

        pub.publish(msg);
    }

private:
    ros::NodeHandle n;

    int count = 0;

    ros::Publisher pub;
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "simple_node_pub_obj");

    Publicador pub;

    ros::Rate loop_rate(20);

    while (ros::ok())
    {
        pub.do_work();

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}