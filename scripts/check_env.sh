#!/usr/bin/env bash
# check_env.sh — 检查开发环境是否满足要求
set -euo pipefail

echo "═══════════════════════════════════════"
echo "  ROS2 Template — Environment Check"
echo "═══════════════════════════════════════"

PASS=0
FAIL=0

check() {
    local name="$1"
    local cmd="$2"
    if eval "$cmd" &>/dev/null; then
        echo "  [✓] ${name}"
        ((PASS++)) || true
    else
        echo "  [✗] ${name}"
        ((FAIL++)) || true
    fi
}

# ROS2
check "ROS2 installed" "command -v ros2"
check "ROS_DISTRO set" "[[ -n \${ROS_DISTRO:-} ]]"
check "colcon installed" "command -v colcon"

# Python
check "Python 3.10+" "python3 -c 'import sys; assert sys.version_info >= (3,10)'"
check "pip installed" "command -v pip3"

# Workspace
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
check "Workspace built" "[[ -d '${ROOT_DIR}/ros2_ws/install' ]]"

echo ""
echo "Result: ${PASS} passed, ${FAIL} failed"

if [[ $FAIL -gt 0 ]]; then
    echo "[WARN] Some checks failed. See docs/01_environment/setup.md"
    exit 1
fi
echo "[DONE] All checks passed!"
