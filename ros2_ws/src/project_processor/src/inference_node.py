#!/usr/bin/env python3
"""
inference_node.py — 算法推理节点

职责：
  - 订阅处理后的传感器数据
  - 执行特征提取和模型推理
  - 发布推理结果

输入：
  - /sensor/processed  (project_interfaces/SensorData)

输出：
  - /result/inference  (project_interfaces/InferenceResult)

配置：
  - config/inference.yaml
"""

import time

import rclpy
from rclpy.node import Node

from project_interfaces.msg import InferenceResult, SensorData


class InferenceNode(Node):
    """对预处理数据执行推理，输出分类/预测结果。"""

    def __init__(self):
        super().__init__("inference_node")

        # ── 参数声明 ────────────────────────────────────────────────────
        self.declare_parameter("topic_in", "/sensor/processed")
        self.declare_parameter("topic_out", "/result/inference")
        self.declare_parameter("model_name", "threshold")
        self.declare_parameter("confidence_threshold", 0.5)
        self.declare_parameter("model_path", "")

        topic_in = self.get_parameter("topic_in").value
        topic_out = self.get_parameter("topic_out").value
        self._model_name = self.get_parameter("model_name").value
        self._conf_thresh = self.get_parameter("confidence_threshold").value

        # ── Subscriber & Publisher ──────────────────────────────────────
        self._sub = self.create_subscription(
            SensorData, topic_in, self._callback, 10
        )
        self._pub = self.create_publisher(InferenceResult, topic_out, 10)

        self.get_logger().info(
            f"InferenceNode: model={self._model_name}, "
            f"conf_thresh={self._conf_thresh}"
        )

    def _callback(self, msg: SensorData):
        """执行推理并发布结果。"""
        t_start = time.monotonic()

        # TODO: 在此实现特征提取和模型推理逻辑
        label, class_id, confidence = self._infer(msg.data)

        latency_ms = (time.monotonic() - t_start) * 1000.0

        result = InferenceResult()
        result.header.stamp = self.get_clock().now().to_msg()
        result.header.frame_id = "inference"
        result.label = label
        result.class_id = class_id
        result.confidence = confidence
        result.model_name = self._model_name
        result.latency_ms = float(latency_ms)

        self._pub.publish(result)

    def _infer(self, data: list) -> tuple[str, int, float]:
        """
        执行推理逻辑（模板实现）。

        Returns:
            (label, class_id, confidence)
        """
        # TODO: 替换为真实模型推理逻辑
        mean_val = sum(data) / len(data) if data else 0.0
        if mean_val > self._conf_thresh:
            return "class_a", 0, min(abs(mean_val), 1.0)
        return "class_b", 1, min(1.0 - abs(mean_val), 1.0)


def main(args=None):
    rclpy.init(args=args)
    node = InferenceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
