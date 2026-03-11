"""
sim_demo.launch.py — 完整仿真演示启动文件

启动顺序：
  1. project_simulator  (数据/环境仿真)
  2. project_processor  (数据处理/算法推理)
  3. project_controller (执行控制)
  4. project_visualizer (可视化)

用法：
  ros2 launch project_bringup sim_demo.launch.py
  ros2 launch project_bringup sim_demo.launch.py use_rviz:=false
"""

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    TimerAction,
)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # ── Launch arguments ──────────────────────────────────────────────────
    use_rviz_arg = DeclareLaunchArgument(
        "use_rviz",
        default_value="true",
        description="Whether to launch RViz",
    )
    config_arg = DeclareLaunchArgument(
        "config",
        default_value=PathJoinSubstitution(
            [FindPackageShare("project_bringup"), "config", "system.yaml"]
        ),
        description="Path to system config YAML",
    )

    # ── Sub-launch includes ───────────────────────────────────────────────
    simulator_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare("project_simulator"), "launch", "simulator.launch.py"]
            )
        ),
    )

    processor_launch = TimerAction(
        period=2.0,
        actions=[
            IncludeLaunchDescription(
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
        ],
    )

    controller_launch = TimerAction(
        period=4.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    PathJoinSubstitution(
                        [
                            FindPackageShare("project_controller"),
                            "launch",
                            "controller.launch.py",
                        ]
                    )
                ),
            )
        ],
    )

    visualizer_launch = TimerAction(
        period=5.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    PathJoinSubstitution(
                        [
                            FindPackageShare("project_visualizer"),
                            "launch",
                            "visualizer.launch.py",
                        ]
                    )
                ),
                condition=IfCondition(LaunchConfiguration("use_rviz")),
            )
        ],
    )

    return LaunchDescription(
        [
            use_rviz_arg,
            config_arg,
            simulator_launch,
            processor_launch,
            controller_launch,
            visualizer_launch,
        ]
    )
