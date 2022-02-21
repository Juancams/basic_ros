cmake_minimum_required(VERSION 2.8.3)
project(basic_roscpp)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package(
CATKIN_DEPENDS roscpp std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(simple_node src/simple_node.cpp)
add_executable(simple_node_pub src/simple_node_pub.cpp)
add_executable(simple_node_sub src/simple_node_sub.cpp)
add_executable(simple_node_pub_obj src/simple_node_pub_obj.cpp)
add_executable(simple_node_sub_obj src/simple_node_sub_obj.cpp)

target_link_libraries(simple_node ${catkin_LIBRARIES})
target_link_libraries(simple_node_pub ${catkin_LIBRARIES})
target_link_libraries(simple_node_sub ${catkin_LIBRARIES})
target_link_libraries(simple_node_pub_obj ${catkin_LIBRARIES})
target_link_libraries(simple_node_sub_obj ${catkin_LIBRARIES})

roslint_cpp(
 src/bumpgo_node.cpp
 src/bumpgo_roscpp/bumpgo.cpp
 include/bumpgo_roscpp/bumpgo.h
)
