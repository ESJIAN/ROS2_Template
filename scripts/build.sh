#!/usr/bin/env bash
# build.sh — 编译 ROS2 工作空间
# 用法：./scripts/build.sh [--clean] [--pkg <package_name>]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
WS_DIR="${ROOT_DIR}/src"

CLEAN=false
PKG=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --clean) CLEAN=true; shift ;;
        --pkg) PKG="$2"; shift 2 ;;
        *) echo "Unknown argument: $1"; exit 1 ;;
    esac
done

# ── Source ROS2 ──────────────────────────────────────────────────
if [[ -z "${ROS_DISTRO:-}" ]]; then
    source /opt/ros/humble/setup.bash
fi

echo "═══════════════════════════════════════"
echo "  ROS2 Template — Build"
echo "═══════════════════════════════════════"

cd "${WS_DIR}"

# ── Clean ─────────────────────────────────────────────────────────
if [[ "${CLEAN}" == "true" ]]; then
    echo "[INFO] Cleaning build artifacts..."
    rm -rf build/ install/ log/
fi

# ── Build ─────────────────────────────────────────────────────────
BUILD_ARGS=(--symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release)

if [[ -n "${PKG}" ]]; then
    echo "[INFO] Building package: ${PKG}"
    colcon build "${BUILD_ARGS[@]}" --packages-select "${PKG}"
else
    echo "[INFO] Building all packages..."
    colcon build "${BUILD_ARGS[@]}"
fi

echo ""
echo "[DONE] Build complete!"
echo "       Run: source ${WS_DIR}/install/setup.bash"
