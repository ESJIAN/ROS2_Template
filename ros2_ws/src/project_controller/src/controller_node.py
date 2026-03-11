#!/usr/bin/env python3
"""
controller_node.py — 执行控制节点

职责：
  - 订阅经安全门控的控制命令
  - 将高层命令映射为执行器动作
  - 发布最终控制命令到执行器

输入：
  - /command/safe  (project_interfaces/ControlCommand)

输出：
  - /command/control  (project_interfaces/ControlCommand)

配置：
  - config/controller.yaml
"""

import rclpy
from rclpy.node import Node

from project_interfaces.msg import ControlCommand


class ControllerNode(Node):
    """将安全命令映射为执行器控制命令。"""

    def __init__(self):
        super().__init__("controller_node")

        # ── 参数声明 ────────────────────────────────────────────────────
        self.declare_parameter("topic_in", "/command/safe")
        self.declare_parameter("topic_out", "/command/control")

        topic_in = self.get_parameter("topic_in").value
        topic_out = self.get_parameter("topic_out").value

        # 命令映射表（可从 YAML 加载）
        self._command_map: dict[str, str] = {
            "class_a": "action_a",
            "class_b": "action_b",
        }

        self._sub = self.create_subscription(
            ControlCommand, topic_in, self._callback, 10
        )
        self._pub = self.create_publisher(ControlCommand, topic_out, 10)

        self.get_logger().info(f"ControllerNode: {topic_in} → {topic_out}")

    def _callback(self, msg: ControlCommand):
        """将命令映射并转发。"""
        mapped_type = self._command_map.get(msg.command_type, msg.command_type)

        out_cmd = ControlCommand()
        out_cmd.header = msg.header
        out_cmd.command_type = mapped_type
        out_cmd.target_name = msg.target_name
        out_cmd.target_pose = msg.target_pose
        out_cmd.confidence = msg.confidence
        out_cmd.is_safe = msg.is_safe

        self._pub.publish(out_cmd)
        self.get_logger().info(
            f"Command: {msg.command_type} → {mapped_type} "
            f"(conf={msg.confidence:.2f})"
        )


def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
