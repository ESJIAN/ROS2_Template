"""
display.launch.py — 在 RViz 中显示机器人 URDF 模型

用法：
  ros2 launch robot_description display.launch.py
"""

from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    urdf_file = PathJoinSubstitution(
        [FindPackageShare("robot_description"), "urdf", "robot.urdf.xacro"]
    )

    robot_description = ParameterValue(
        Command(["xacro ", urdf_file]),
        value_type=str,
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}],
        output="screen",
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
    )

    return LaunchDescription(
        [robot_state_publisher, joint_state_publisher_gui, rviz_node]
    )
