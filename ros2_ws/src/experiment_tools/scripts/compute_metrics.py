#!/usr/bin/env python3
"""
compute_metrics.py — 计算实验性能指标

从 ROS2 bag 中读取推理结果和真实标签，计算分类性能指标。

用法：
  python compute_metrics.py --bag outputs/bags/exp_001 --output outputs/reports/metrics_001.json
"""

import argparse
import json
import sys
from pathlib import Path


def compute_accuracy(predictions: list, ground_truth: list) -> float:
    """计算分类准确率。"""
    if not ground_truth:
        return 0.0
    correct = sum(p == g for p, g in zip(predictions, ground_truth))
    return correct / len(ground_truth)


def compute_confusion_matrix(
    predictions: list, ground_truth: list, labels: list
) -> dict:
    """计算混淆矩阵。"""
    matrix: dict[str, dict[str, int]] = {
        true: {pred: 0 for pred in labels} for true in labels
    }
    for pred, true in zip(predictions, ground_truth):
        if true in matrix and pred in matrix[true]:
            matrix[true][pred] += 1
    return matrix


def main():
    parser = argparse.ArgumentParser(description="Compute experiment metrics from bag")
    parser.add_argument("--bag", required=True, help="Path to ROS2 bag")
    parser.add_argument(
        "--output",
        default="outputs/reports/metrics.json",
        help="Output metrics JSON file",
    )
    args = parser.parse_args()

    bag_path = Path(args.bag)
    if not bag_path.exists():
        print(f"ERROR: Bag not found: {bag_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # TODO: 实现从 bag 文件中读取 /result/inference 和 /intention/ground_truth
    # 以下为示例输出结构
    metrics = {
        "bag": str(bag_path),
        "accuracy": None,
        "confusion_matrix": None,
        "avg_latency_ms": None,
        "total_samples": 0,
        "note": "TODO: implement bag parsing logic",
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    print(f"[compute_metrics] Metrics saved to: {output_path}")


if __name__ == "__main__":
    main()
