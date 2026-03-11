# project_bringup

## 简介

系统总启动包，提供统一的 launch 入口和全局配置管理。

## 启动模式

| 启动文件 | 命令 | 说明 |
|---------|------|------|
| `sim_demo.launch.py` | `ros2 launch project_bringup sim_demo.launch.py` | 完整仿真演示 |
| `processing_only.launch.py` | `ros2 launch project_bringup processing_only.launch.py` | 仅处理模块 |
| `replay_bag.launch.py` | `ros2 launch project_bringup replay_bag.launch.py bag_path:=<path>` | 回放 Bag 文件 |

## 启动参数

### sim_demo.launch.py

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_rviz` | `true` | 是否启动 RViz |
| `config` | `config/system.yaml` | 系统配置文件路径 |

### replay_bag.launch.py

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `bag_path` | 必填 | Bag 文件路径 |
| `rate` | `1.0` | 回放速率 |

## 配置文件

- `config/system.yaml`：系统全局配置（模式、日志级别、Topic 名称、QoS）

## 依赖关系

本包依赖以下功能包的 launch 文件：
- `project_simulator`
- `project_processor`
- `project_controller`
- `project_visualizer`
