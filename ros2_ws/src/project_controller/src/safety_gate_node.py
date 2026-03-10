#!/usr/bin/env python3
"""
safety_gate_node.py — 安全门控节点

职责：
  - 订阅推理结果
  - 根据置信度、频率限制等条件过滤不安全的命令
  - 发布通过安全检查的控制命令

输入：
  - /result/inference  (project_interfaces/InferenceResult)

输出：
  - /command/safe  (project_interfaces/ControlCommand)

配置：
  - config/safety.yaml
"""

import time

import rclpy
from rclpy.node import Node

from project_interfaces.msg import ControlCommand, InferenceResult


class SafetyGateNode(Node):
    """对推理结果进行安全过滤，输出安全命令。"""

    def __init__(self):
        super().__init__("safety_gate_node")

        # ── 参数声明 ────────────────────────────────────────────────────
        self.declare_parameter("topic_in", "/result/inference")
        self.declare_parameter("topic_out", "/command/safe")
        self.declare_parameter("min_confidence", 0.6)
        self.declare_parameter("min_command_interval_sec", 0.5)
        self.declare_parameter("suppress_repeated_commands", True)

        topic_in = self.get_parameter("topic_in").value
        topic_out = self.get_parameter("topic_out").value
        self._min_conf = self.get_parameter("min_confidence").value
        self._min_interval = self.get_parameter("min_command_interval_sec").value
        self._suppress_repeat = self.get_parameter(
            "suppress_repeated_commands"
        ).value

        self._last_command_time = 0.0
        self._last_label = ""

        self._sub = self.create_subscription(
            InferenceResult, topic_in, self._callback, 10
        )
        self._pub = self.create_publisher(ControlCommand, topic_out, 10)

        self.get_logger().info(
            f"SafetyGateNode: min_conf={self._min_conf}, "
            f"min_interval={self._min_interval}s"
        )

    def _callback(self, msg: InferenceResult):
        """过滤推理结果，仅放行安全的命令。"""
        now = time.monotonic()

        # 置信度门控
        if msg.confidence < self._min_conf:
            self.get_logger().debug(
                f"Blocked: confidence {msg.confidence:.2f} < {self._min_conf}"
            )
            return

        # 频率门控
        if (now - self._last_command_time) < self._min_interval:
            return

        # 重复命令抑制
        if self._suppress_repeat and msg.label == self._last_label:
            return

        self._last_command_time = now
        self._last_label = msg.label

        cmd = ControlCommand()
        cmd.header.stamp = self.get_clock().now().to_msg()
        cmd.header.frame_id = "safety_gate"
        cmd.command_type = msg.label
        cmd.confidence = msg.confidence
        cmd.is_safe = True
        self._pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = SafetyGateNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
