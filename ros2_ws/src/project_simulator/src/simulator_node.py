#!/usr/bin/env python3
"""
simulator_node.py — 仿真数据生成节点

职责：
  - 生成符合项目格式的模拟传感器数据
  - 以可配置的采样率发布到 /sensor/raw
  - 支持多种仿真信号模式（正弦波、噪声、复合信号）

输入：
  - 参数：simulator.yaml

输出：
  - /sensor/raw  (project_interfaces/SensorData)

用法：
  ros2 run project_simulator simulator_node.py
"""

import math
import random

import rclpy
from rclpy.node import Node

from project_interfaces.msg import SensorData


class SimulatorNode(Node):
    """生成模拟传感器数据并发布。"""

    def __init__(self):
        super().__init__("simulator_node")

        # ── 参数声明 ────────────────────────────────────────────────────
        self.declare_parameter("sample_rate", 100.0)        # Hz
        self.declare_parameter("channel_count", 8)
        self.declare_parameter("noise_amplitude", 0.1)
        self.declare_parameter("signal_amplitude", 1.0)
        self.declare_parameter("signal_frequency", 1.0)     # Hz
        self.declare_parameter("random_seed", 42)
        self.declare_parameter("topic_out", "/sensor/raw")

        # ── 读取参数 ────────────────────────────────────────────────────
        self._rate = self.get_parameter("sample_rate").value
        self._channels = self.get_parameter("channel_count").value
        self._noise_amp = self.get_parameter("noise_amplitude").value
        self._sig_amp = self.get_parameter("signal_amplitude").value
        self._sig_freq = self.get_parameter("signal_frequency").value
        topic_out = self.get_parameter("topic_out").value

        seed = self.get_parameter("random_seed").value
        random.seed(seed)

        self._sample_index = 0

        # ── Publisher ──────────────────────────────────────────────────
        self._pub = self.create_publisher(SensorData, topic_out, 10)
        timer_period = 1.0 / self._rate
        self._timer = self.create_timer(timer_period, self._publish_sample)

        self.get_logger().info(
            f"SimulatorNode started: {self._channels}ch @ {self._rate}Hz → {topic_out}"
        )

    def _publish_sample(self):
        """生成并发布一个采样点。"""
        msg = SensorData()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "simulator"
        msg.sample_index = self._sample_index
        msg.source = "simulator"

        t = self._sample_index / self._rate
        msg.data = [
            self._sig_amp * math.sin(2.0 * math.pi * self._sig_freq * t)
            + self._noise_amp * (random.random() * 2.0 - 1.0)
            for _ in range(self._channels)
        ]

        self._pub.publish(msg)
        self._sample_index += 1


def main(args=None):
    rclpy.init(args=args)
    node = SimulatorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
