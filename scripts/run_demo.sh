#!/usr/bin/env bash
# run_demo.sh — 一键启动演示系统
# 用法：./scripts/run_demo.sh [--no-rviz]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
WS_DIR="${ROOT_DIR}/src"

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

# 启动应用层（src/application/）中的演示 launch 文件
# 请根据实际应用层包名修改以下命令：
# ros2 launch <application_package> sim_demo.launch.py use_rviz:="${USE_RVIZ}"
echo "[INFO] Please configure the launch command in this script."
echo "       Edit: scripts/run_demo.sh"
