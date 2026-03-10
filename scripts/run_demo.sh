#!/usr/bin/env bash
# run_demo.sh — 一键启动演示系统
# 用法：./scripts/run_demo.sh [--no-rviz]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
WS_DIR="${ROOT_DIR}/ros2_ws"

USE_RVIZ=true

while [[ $# -gt 0 ]]; do
    case "$1" in
        --no-rviz) USE_RVIZ=false; shift ;;
        *) echo "Unknown argument: $1"; exit 1 ;;
    esac
done

# ── Source workspace ─────────────────────────────────────────────
if [[ -z "${ROS_DISTRO:-}" ]]; then
    source /opt/ros/humble/setup.bash
fi

if [[ -f "${WS_DIR}/install/setup.bash" ]]; then
    # shellcheck source=/dev/null
    source "${WS_DIR}/install/setup.bash"
else
    echo "[ERROR] Workspace not built. Run './scripts/build.sh' first."
    exit 1
fi

echo "═══════════════════════════════════════"
echo "  ROS2 Template — Demo Launch"
echo "═══════════════════════════════════════"

ros2 launch project_bringup sim_demo.launch.py use_rviz:="${USE_RVIZ}"
