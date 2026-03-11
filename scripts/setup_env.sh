#!/usr/bin/env bash
# setup_env.sh — 初始化开发环境
# 用法：./scripts/setup_env.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "═══════════════════════════════════════"
echo "  ROS2 Template — Environment Setup"
echo "═══════════════════════════════════════"

# ── 检查 ROS2 ────────────────────────────────────────────────────
if [[ -z "${ROS_DISTRO:-}" ]]; then
    echo "[WARN] ROS2 not sourced. Trying /opt/ros/humble/setup.bash..."
    if [[ -f /opt/ros/humble/setup.bash ]]; then
        # shellcheck source=/dev/null
        source /opt/ros/humble/setup.bash
        echo "[OK] Sourced ROS2 Humble"
    else
        echo "[ERROR] ROS2 not found. Please install ROS2 first."
        echo "        See docs/01_environment/setup.md"
        exit 1
    fi
fi

echo "[OK] ROS_DISTRO=${ROS_DISTRO}"

# ── 安装 ROS2 包依赖 ─────────────────────────────────────────────
echo "[INFO] Installing ROS2 package dependencies..."
cd "${ROOT_DIR}/ros2_ws"
rosdep install --from-paths src --ignore-src -r -y

# ── 安装 Python 依赖 ─────────────────────────────────────────────
if [[ -f "${ROOT_DIR}/requirements.txt" ]]; then
    echo "[INFO] Installing Python dependencies..."
    pip install -r "${ROOT_DIR}/requirements.txt"
fi

echo ""
echo "[DONE] Environment setup complete!"
echo "       Run './scripts/build.sh' to build the workspace."
