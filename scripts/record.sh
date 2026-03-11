#!/usr/bin/env bash
# record.sh — 启动 Bag 录制
# 用法：./scripts/record.sh [output_name]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

OUTPUT_NAME="${1:-session_$(date +%Y%m%d_%H%M%S)}"
OUTPUT_PATH="${ROOT_DIR}/outputs/bags/${OUTPUT_NAME}"

echo "[INFO] Recording to: ${OUTPUT_PATH}"
echo "       Press Ctrl+C to stop."

# ROS2 Bag 录制：录制所有话题到指定目录
ros2 bag record -o "${OUTPUT_PATH}" -a
