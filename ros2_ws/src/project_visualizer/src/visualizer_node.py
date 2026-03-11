#!/usr/bin/env python3
"""
visualizer_node.py — 数据可视化节点

职责：
  - 订阅传感器数据和推理结果
  - 使用 matplotlib 实时绘制波形和结果
  - 提供可诊断的多面板显示

输入：
  - /sensor/raw        (project_interfaces/SensorData)
  - /sensor/processed  (project_interfaces/SensorData)
  - /result/inference  (project_interfaces/InferenceResult)

配置：
  - config/visualizer.yaml

注意：此节点需要显示环境（X11/Wayland）。
      在无头环境中使用 dashboard_node.py 的 Web 界面替代。
"""

import threading
from collections import deque

import rclpy
from rclpy.node import Node

from project_interfaces.msg import InferenceResult, SensorData


class VisualizerNode(Node):
    """实时可视化传感器数据和推理结果。"""

    def __init__(self):
        super().__init__("visualizer_node")

        self.declare_parameter("topic_raw", "/sensor/raw")
        self.declare_parameter("topic_processed", "/sensor/processed")
        self.declare_parameter("topic_inference", "/result/inference")
        self.declare_parameter("buffer_size", 500)
        self.declare_parameter("update_rate_hz", 10.0)

        topic_raw = self.get_parameter("topic_raw").value
        topic_processed = self.get_parameter("topic_processed").value
        topic_inference = self.get_parameter("topic_inference").value
        buf_size = self.get_parameter("buffer_size").value

        self._raw_buffer: deque = deque(maxlen=buf_size)
        self._processed_buffer: deque = deque(maxlen=buf_size)
        self._inference_labels: deque = deque(maxlen=50)
        self._lock = threading.Lock()

        self.create_subscription(SensorData, topic_raw, self._raw_cb, 10)
        self.create_subscription(
            SensorData, topic_processed, self._processed_cb, 10
        )
        self.create_subscription(
            InferenceResult, topic_inference, self._inference_cb, 10
        )

        self.get_logger().info("VisualizerNode started")

    def _raw_cb(self, msg: SensorData):
        with self._lock:
            if msg.data:
                self._raw_buffer.append(msg.data[0])

    def _processed_cb(self, msg: SensorData):
        with self._lock:
            if msg.data:
                self._processed_buffer.append(msg.data[0])

    def _inference_cb(self, msg: InferenceResult):
        with self._lock:
            self._inference_labels.append(
                f"{msg.label} ({msg.confidence:.2f})"
            )


def main(args=None):
    rclpy.init(args=args)
    node = VisualizerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
