#!/usr/bin/env python3
"""
generate_report.py — 自动生成实验报告

读取 metrics JSON 文件，生成 Markdown 格式的实验报告。

用法：
  python generate_report.py --metrics outputs/reports/metrics.json --output outputs/reports/report.md
"""

import argparse
import json
from datetime import datetime
from pathlib import Path


REPORT_TEMPLATE = """\
# 实验报告

**生成时间**: {timestamp}  
**Bag 文件**: {bag}  

## 性能指标

| 指标 | 值 |
|------|-----|
| 准确率 | {accuracy} |
| 平均延迟 | {avg_latency_ms} ms |
| 样本总数 | {total_samples} |

## 混淆矩阵

{confusion_matrix}

## 备注

{note}
"""


def format_confusion_matrix(matrix) -> str:
    if not matrix:
        return "_暂无数据_"
    labels = list(matrix.keys())
    header = "| 真实\\预测 | " + " | ".join(labels) + " |"
    sep = "| " + " | ".join(["---"] * (len(labels) + 1)) + " |"
    rows = [header, sep]
    for true_label, preds in matrix.items():
        row = f"| {true_label} | " + " | ".join(str(preds.get(p, 0)) for p in labels) + " |"
        rows.append(row)
    return "\n".join(rows)


def main():
    parser = argparse.ArgumentParser(description="Generate experiment report")
    parser.add_argument(
        "--metrics",
        default="outputs/reports/metrics.json",
        help="Path to metrics JSON",
    )
    parser.add_argument(
        "--output",
        default="outputs/reports/report.md",
        help="Output Markdown report path",
    )
    args = parser.parse_args()

    metrics_path = Path(args.metrics)
    if not metrics_path.exists():
        print(f"ERROR: Metrics file not found: {metrics_path}")
        return

    with open(metrics_path, encoding="utf-8") as f:
        metrics = json.load(f)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = REPORT_TEMPLATE.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        bag=metrics.get("bag", "N/A"),
        accuracy=f"{metrics['accuracy']:.4f}" if metrics.get("accuracy") is not None else "N/A",
        avg_latency_ms=f"{metrics['avg_latency_ms']:.2f}" if metrics.get("avg_latency_ms") is not None else "N/A",
        total_samples=metrics.get("total_samples", 0),
        confusion_matrix=format_confusion_matrix(metrics.get("confusion_matrix")),
        note=metrics.get("note", ""),
    )

    output_path.write_text(report, encoding="utf-8")
    print(f"[generate_report] Report saved to: {output_path}")


if __name__ == "__main__":
    main()
