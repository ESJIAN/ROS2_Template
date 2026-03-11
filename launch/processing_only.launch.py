"""
processing_only.launch.py — 仅启动处理模块

适用场景：外部已有 /sensor/raw 数据源（真实传感器或其他节点），
只需启动数据处理流程。

启动的节点：preprocessor_node → inference_node → controller_node

参数来源：configs/global_params.yaml

用法：
  ros2 launch project_bringup processing_only.launch.py
  ros2 launch project_bringup processing_only.launch.py use_sim_time:=false
"""

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # ── 参数声明 ──────────────────────────────────────────────────────
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="false",
        description="使用仿真时钟",
    )
    global_config_arg = DeclareLaunchArgument(
        "global_config",
        default_value=os.path.join(
            os.path.dirname(__file__), "..", "configs", "global_params.yaml"
        ),
        description="全局参数配置文件路径",
    )

    use_sim_time = LaunchConfiguration("use_sim_time")
    global_config = LaunchConfiguration("global_config")

    # ── 节点定义 ──────────────────────────────────────────────────────
    preprocessor_node = Node(
        package="project_processor",
        executable="preprocessor_node",
        name="preprocessor",
        parameters=[global_config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    inference_node = Node(
        package="project_processor",
        executable="inference_node",
        name="inference",
        parameters=[global_config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    controller_node = Node(
        package="project_controller",
        executable="controller_node",
        name="controller",
        parameters=[global_config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    return LaunchDescription(
        [
            use_sim_time_arg,
            global_config_arg,
            preprocessor_node,
            inference_node,
            controller_node,
        ]
    )
