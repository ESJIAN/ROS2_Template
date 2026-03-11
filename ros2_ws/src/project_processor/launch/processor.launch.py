"""
processor.launch.py — 启动数据处理与推理节点

用法：
  ros2 launch project_processor processor.launch.py
"""

from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_share = FindPackageShare("project_processor")

    preprocessor_node = Node(
        package="project_processor",
        executable="preprocessor_node.py",
        name="preprocessor_node",
        parameters=[
            PathJoinSubstitution([pkg_share, "config", "preprocess.yaml"])
        ],
        output="screen",
    )

    inference_node = Node(
        package="project_processor",
        executable="inference_node.py",
        name="inference_node",
        parameters=[
            PathJoinSubstitution([pkg_share, "config", "inference.yaml"])
        ],
        output="screen",
    )

    return LaunchDescription([preprocessor_node, inference_node])
