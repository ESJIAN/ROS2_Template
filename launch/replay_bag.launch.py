"""
replay_bag.launch.py — 历史数据回放启动文件

适用场景：回放 ROS2 Bag 录制的历史数据，
并通过处理流程进行离线分析。

启动的节点：ros2 bag play（bag_path）→ preprocessor_node → inference_node → controller_node

参数来源：configs/global_params.yaml

用法：
  ros2 launch project_bringup replay_bag.launch.py bag_path:=/path/to/bag
  ros2 launch project_bringup replay_bag.launch.py bag_path:=outputs/bags/exp_01 loop:=true
"""

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # ── 参数声明 ──────────────────────────────────────────────────────
    bag_path_arg = DeclareLaunchArgument(
        "bag_path",
        description="ROS2 Bag 文件路径（必填）",
    )
    loop_arg = DeclareLaunchArgument(
        "loop",
        default_value="false",
        description="是否循环回放",
    )
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="true",
        description="使用仿真时钟（回放时建议开启）",
    )
    global_config_arg = DeclareLaunchArgument(
        "global_config",
        default_value=os.path.join(
            os.path.dirname(__file__), "..", "configs", "global_params.yaml"
        ),
        description="全局参数配置文件路径",
    )

    bag_path = LaunchConfiguration("bag_path")
    loop = LaunchConfiguration("loop")
    use_sim_time = LaunchConfiguration("use_sim_time")
    global_config = LaunchConfiguration("global_config")

    # ── Bag 回放进程 ──────────────────────────────────────────────────
    # --loop 是布尔开关，不接受值，因此根据参数分别定义两个进程
    bag_play_loop = ExecuteProcess(
        cmd=["ros2", "bag", "play", bag_path, "--loop"],
        output="screen",
        condition=IfCondition(loop),
    )
    bag_play_once = ExecuteProcess(
        cmd=["ros2", "bag", "play", bag_path],
        output="screen",
        condition=UnlessCondition(loop),
    )

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
            bag_path_arg,
            loop_arg,
            use_sim_time_arg,
            global_config_arg,
            bag_play_loop,
            bag_play_once,
            preprocessor_node,
            inference_node,
            controller_node,
        ]
    )
