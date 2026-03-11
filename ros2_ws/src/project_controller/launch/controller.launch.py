"""
controller.launch.py — 启动控制执行节点

用法：
  ros2 launch project_controller controller.launch.py
"""

from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_share = FindPackageShare("project_controller")

    safety_gate_node = Node(
        package="project_controller",
        executable="safety_gate_node.py",
        name="safety_gate_node",
        parameters=[
            PathJoinSubstitution([pkg_share, "config", "safety.yaml"])
        ],
        output="screen",
    )

    controller_node = Node(
        package="project_controller",
        executable="controller_node.py",
        name="controller_node",
        parameters=[
            PathJoinSubstitution([pkg_share, "config", "controller.yaml"])
        ],
        output="screen",
    )

    return LaunchDescription([safety_gate_node, controller_node])
