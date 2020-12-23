cmake_minimum_required(VERSION 2.8.3)
project(bumpgo)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  geometry_msgs
)

catkin_package(
CATKIN_DEPENDS rospy sensor_msgs geometry_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
