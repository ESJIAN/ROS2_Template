cmake_minimum_required(VERSION 3.22)
project(robot_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  urdf
  meshes
  config
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
