#!/usr/bin/env python3
"""
data_source_node.py — 真实设备数据桥接节点（占位符）

职责：
  - 对接真实传感器设备（串口/USB/TCP/SDK）
  - 将设备数据转换为统一的 ROS2 消息格式
  - 发布到 /sensor/raw

注意：此节点为模板，需根据实际硬件进行实现。

输出：
  - /sensor/raw  (project_interfaces/SensorData)
"""

import rclpy
from rclpy.node import Node

from project_interfaces.msg import SensorData


class DataSourceNode(Node):
    """真实设备数据桥接节点（模板）。"""

    def __init__(self):
        super().__init__("data_source_node")

        self.declare_parameter("topic_out", "/sensor/raw")
        self.declare_parameter("device_port", "/dev/ttyUSB0")
        self.declare_parameter("baud_rate", 115200)

        topic_out = self.get_parameter("topic_out").value
        self._pub = self.create_publisher(SensorData, topic_out, 10)

        self.get_logger().warn(
            "DataSourceNode: This is a template. "
            "Implement actual device communication here."
        )

    # TODO: 实现设备连接与数据读取逻辑


def main(args=None):
    rclpy.init(args=args)
    node = DataSourceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
