"""
simulator.launch.py — 启动仿真数据生成节点

用法：
  ros2 launch project_simulator simulator.launch.py
  ros2 launch project_simulator simulator.launch.py use_device:=true
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_device_arg = DeclareLaunchArgument(
        "use_device",
        default_value="false",
        description="Use real device (true) or simulator (false)",
    )

    config_file = PathJoinSubstitution(
        [FindPackageShare("project_simulator"), "config", "simulator.yaml"]
    )

    simulator_node = Node(
        package="project_simulator",
        executable="simulator_node.py",
        name="simulator_node",
        parameters=[config_file],
        output="screen",
        condition=UnlessCondition(LaunchConfiguration("use_device")),
    )

    data_source_node = Node(
        package="project_simulator",
        executable="data_source_node.py",
        name="data_source_node",
        parameters=[config_file],
        output="screen",
        condition=IfCondition(LaunchConfiguration("use_device")),
    )

    return LaunchDescription([use_device_arg, simulator_node, data_source_node])
