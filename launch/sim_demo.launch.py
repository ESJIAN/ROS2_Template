"""
sim_demo.launch.py — 完整仿真演示启动文件

启动顺序：
  simulator_node → preprocessor_node → inference_node → controller_node → visualizer_node

参数来源：configs/demo.yaml 和 configs/global_params.yaml

用法：
  ros2 launch project_bringup sim_demo.launch.py
  ros2 launch project_bringup sim_demo.launch.py use_sim_time:=true
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
    config_arg = DeclareLaunchArgument(
        "config",
        default_value=os.path.join(
            os.path.dirname(__file__), "..", "configs", "demo.yaml"
        ),
        description="演示参数配置文件路径",
    )
    global_config_arg = DeclareLaunchArgument(
        "global_config",
        default_value=os.path.join(
            os.path.dirname(__file__), "..", "configs", "global_params.yaml"
        ),
        description="全局参数配置文件路径",
    )

    use_sim_time = LaunchConfiguration("use_sim_time")
    config = LaunchConfiguration("config")
    global_config = LaunchConfiguration("global_config")

    # ── 节点定义 ──────────────────────────────────────────────────────
    simulator_node = Node(
        package="project_simulator",
        executable="simulator_node",
        name="simulator",
        parameters=[global_config, config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    preprocessor_node = Node(
        package="project_processor",
        executable="preprocessor_node",
        name="preprocessor",
        parameters=[global_config, config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    inference_node = Node(
        package="project_processor",
        executable="inference_node",
        name="inference",
        parameters=[global_config, config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    controller_node = Node(
        package="project_controller",
        executable="controller_node",
        name="controller",
        parameters=[global_config, config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    visualizer_node = Node(
        package="project_visualizer",
        executable="visualizer_node",
        name="visualizer",
        parameters=[global_config, config, {"use_sim_time": use_sim_time}],
        output="screen",
    )

    return LaunchDescription(
        [
            use_sim_time_arg,
            config_arg,
            global_config_arg,
            simulator_node,
            preprocessor_node,
            inference_node,
            controller_node,
            visualizer_node,
        ]
    )
