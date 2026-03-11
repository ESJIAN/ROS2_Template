#!/usr/bin/env python3
"""
dashboard_node.py — 系统状态仪表盘节点

职责：
  - 订阅系统状态、推理结果、控制命令
  - 在终端输出结构化状态摘要
  - 为 Web UI 提供数据接口（可选扩展）

输入：
  - /result/inference  (project_interfaces/InferenceResult)
  - /system/status     (project_interfaces/SystemStatus)
  - /command/control   (project_interfaces/ControlCommand)
"""

import rclpy
from rclpy.node import Node

from project_interfaces.msg import ControlCommand, InferenceResult, SystemStatus


class DashboardNode(Node):
    """系统状态监控仪表盘。"""

    def __init__(self):
        super().__init__("dashboard_node")

        self.declare_parameter("print_rate_hz", 1.0)

        self._latest_inference: InferenceResult | None = None
        self._latest_status: SystemStatus | None = None
        self._latest_command: ControlCommand | None = None
        self._command_count = 0

        self.create_subscription(
            InferenceResult, "/result/inference", self._inference_cb, 10
        )
        self.create_subscription(
            SystemStatus, "/system/status", self._status_cb, 10
        )
        self.create_subscription(
            ControlCommand, "/command/control", self._command_cb, 10
        )

        rate = self.get_parameter("print_rate_hz").value
        self.create_timer(1.0 / rate, self._print_status)
        self.get_logger().info("DashboardNode started")

    def _inference_cb(self, msg: InferenceResult):
        self._latest_inference = msg

    def _status_cb(self, msg: SystemStatus):
        self._latest_status = msg

    def _command_cb(self, msg: ControlCommand):
        self._latest_command = msg
        self._command_count += 1

    def _print_status(self):
        lines = ["=" * 50, "  SYSTEM DASHBOARD"]
        if self._latest_inference:
            m = self._latest_inference
            lines.append(
                f"  Inference : {m.label:<12} conf={m.confidence:.2f}  "
                f"latency={m.latency_ms:.1f}ms"
            )
        if self._latest_command:
            lines.append(
                f"  Command   : {self._latest_command.command_type:<12} "
                f"(total={self._command_count})"
            )
        if self._latest_status:
            s = self._latest_status
            lines.append(
                f"  Status    : {'OK' if s.healthy else 'ERROR'}  "
                f"mode={s.active_mode}"
            )
        lines.append("=" * 50)
        self.get_logger().info("\n".join(lines))


def main(args=None):
    rclpy.init(args=args)
    node = DashboardNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
