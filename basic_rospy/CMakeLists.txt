cmake_minimum_required(VERSION 2.8.3)
project(basic_rospy)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package(
CATKIN_DEPENDS rospy std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)