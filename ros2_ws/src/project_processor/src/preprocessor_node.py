#!/usr/bin/env python3
"""
preprocessor_node.py — 数据预处理节点

职责：
  - 订阅原始传感器数据
  - 执行滤波、归一化等预处理操作
  - 发布处理后的数据供推理节点使用

输入：
  - /sensor/raw  (project_interfaces/SensorData)

输出：
  - /sensor/processed  (project_interfaces/SensorData)

配置：
  - config/preprocess.yaml
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy

from project_interfaces.msg import SensorData


class PreprocessorNode(Node):
    """对原始传感器数据执行预处理。"""

    def __init__(self):
        super().__init__("preprocessor_node")

        # ── 参数声明 ────────────────────────────────────────────────────
        self.declare_parameter("topic_in", "/sensor/raw")
        self.declare_parameter("topic_out", "/sensor/processed")
        self.declare_parameter("normalize", True)
        self.declare_parameter("buffer_size", 100)

        topic_in = self.get_parameter("topic_in").value
        topic_out = self.get_parameter("topic_out").value
        self._normalize = self.get_parameter("normalize").value

        # ── QoS ────────────────────────────────────────────────────────
        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            depth=10,
        )

        # ── Subscriber & Publisher ──────────────────────────────────────
        self._sub = self.create_subscription(
            SensorData, topic_in, self._callback, sensor_qos
        )
        self._pub = self.create_publisher(SensorData, topic_out, 10)

        self.get_logger().info(
            f"PreprocessorNode: {topic_in} → {topic_out}"
        )

    def _callback(self, msg: SensorData):
        """处理接收到的传感器数据。"""
        processed = SensorData()
        processed.header = msg.header
        processed.sample_index = msg.sample_index
        processed.source = msg.source

        # TODO: 在此实现具体预处理逻辑（滤波、去噪等）
        data = list(msg.data)

        if self._normalize and data:
            max_val = max(abs(v) for v in data) or 1.0
            data = [v / max_val for v in data]

        processed.data = data
        self._pub.publish(processed)


def main(args=None):
    rclpy.init(args=args)
    node = PreprocessorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
