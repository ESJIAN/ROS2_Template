"""
replay_bag.launch.py — 回放 ROS2 Bag 文件

用法：
  ros2 launch project_bringup replay_bag.launch.py bag_path:=/path/to/bag
  ros2 launch project_bringup replay_bag.launch.py bag_path:=/path/to/bag rate:=0.5
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    bag_path_arg = DeclareLaunchArgument(
        "bag_path",
        description="Path to the ROS2 bag file or directory",
    )
    rate_arg = DeclareLaunchArgument(
        "rate",
        default_value="1.0",
        description="Playback rate multiplier (1.0 = real-time)",
    )

    play_bag = ExecuteProcess(
        cmd=[
            "ros2",
            "bag",
            "play",
            LaunchConfiguration("bag_path"),
            "--rate",
            LaunchConfiguration("rate"),
        ],
        output="screen",
    )

    return LaunchDescription([bag_path_arg, rate_arg, play_bag])
