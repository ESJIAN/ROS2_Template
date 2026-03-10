cmake_minimum_required(VERSION 3.22)
project(experiment_tools)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

install(PROGRAMS
  scripts/record_demo.py
  scripts/compute_metrics.py
  scripts/generate_report.py
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
