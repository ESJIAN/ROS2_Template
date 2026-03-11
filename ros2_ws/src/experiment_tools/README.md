# experiment_tools

## 简介

实验管理工具包，提供 ROS2 Bag 录制、性能指标计算和报告生成等功能。

## 脚本

### `record_demo.py` — 录制演示数据

```bash
python ros2_ws/src/experiment_tools/scripts/record_demo.py \
  --output outputs/bags/demo_001 \
  --duration 60
```

| 参数 | 说明 |
|------|------|
| `--output` | 输出 bag 路径 |
| `--duration` | 录制时长（秒），不填则持续录制 |
| `--topics` | 指定录制的话题列表 |

### `compute_metrics.py` — 计算性能指标

```bash
python ros2_ws/src/experiment_tools/scripts/compute_metrics.py \
  --bag outputs/bags/exp_001 \
  --output outputs/reports/metrics_001.json
```

### `generate_report.py` — 生成实验报告

```bash
python ros2_ws/src/experiment_tools/scripts/generate_report.py \
  --metrics outputs/reports/metrics_001.json \
  --output outputs/reports/report_001.md
```

## 完整实验流程

```bash
# 1. 启动系统并录制
ros2 launch project_bringup sim_demo.launch.py &
python scripts/record_demo.py --output outputs/bags/exp_001 --duration 120

# 2. 计算指标
python ros2_ws/src/experiment_tools/scripts/compute_metrics.py \
  --bag outputs/bags/exp_001

# 3. 生成报告
python ros2_ws/src/experiment_tools/scripts/generate_report.py \
  --metrics outputs/reports/metrics.json \
  --output outputs/reports/report.md
```

## 配置

见 `config/rosbag.yaml`：录制话题列表、输出目录、压缩格式等。
