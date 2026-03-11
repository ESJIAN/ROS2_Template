"""
visualizer.launch.py — 启动可视化节点

用法：
  ros2 launch project_visualizer visualizer.launch.py
  ros2 launch project_visualizer visualizer.launch.py use_dashboard:=true
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_dashboard_arg = DeclareLaunchArgument(
        "use_dashboard",
        default_value="true",
        description="Whether to launch the terminal dashboard",
    )

    pkg_share = FindPackageShare("project_visualizer")
    config_file = PathJoinSubstitution([pkg_share, "config", "visualizer.yaml"])

    visualizer_node = Node(
        package="project_visualizer",
        executable="visualizer_node.py",
        name="visualizer_node",
        parameters=[config_file],
        output="screen",
    )

    dashboard_node = Node(
        package="project_visualizer",
        executable="dashboard_node.py",
        name="dashboard_node",
        parameters=[config_file],
        output="screen",
        condition=IfCondition(LaunchConfiguration("use_dashboard")),
    )

    return LaunchDescription([use_dashboard_arg, visualizer_node, dashboard_node])
