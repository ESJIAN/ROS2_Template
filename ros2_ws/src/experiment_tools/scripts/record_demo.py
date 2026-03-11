#!/usr/bin/env python3
"""
record_demo.py — 自动录制演示数据

用法：
  python record_demo.py --output outputs/bags/demo_001 --duration 60
  python record_demo.py --output outputs/bags/exp_01 --topics /sensor/raw /result/inference
"""

import argparse
import subprocess
import sys
from pathlib import Path

DEFAULT_TOPICS = [
    "/sensor/raw",
    "/sensor/processed",
    "/result/inference",
    "/command/safe",
    "/command/control",
    "/system/status",
]


def main():
    parser = argparse.ArgumentParser(description="Record a ROS2 bag for demo/experiment")
    parser.add_argument(
        "--output",
        required=True,
        help="Output bag path (e.g. outputs/bags/demo_001)",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=None,
        help="Recording duration in seconds (omit for unlimited)",
    )
    parser.add_argument(
        "--topics",
        nargs="+",
        default=DEFAULT_TOPICS,
        help="Topics to record",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = ["ros2", "bag", "record", "-o", str(output_path)] + args.topics
    if args.duration:
        cmd += ["--duration", str(args.duration)]

    print(f"[record_demo] Recording to: {output_path}")
    print(f"[record_demo] Topics: {args.topics}")
    if args.duration:
        print(f"[record_demo] Duration: {args.duration}s")
    print(f"[record_demo] Command: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n[record_demo] Recording stopped.")
    except subprocess.CalledProcessError as e:
        print(f"[record_demo] ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
