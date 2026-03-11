"""
processing_only.launch.py — 仅启动处理/算法模块

适用场景：
  - 使用已有 Bag 文件测试算法
  - 只需要数据处理节点时

用法：
  ros2 launch project_bringup processing_only.launch.py
"""

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    processor_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("project_processor"),
                    "launch",
                    "processor.launch.py",
                ]
            )
        ),
    )

    return LaunchDescription([processor_launch])
