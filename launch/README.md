# launch/ — 系统启动文件目录

本目录存放项目的所有顶层 ROS2 Launch 文件，用于一键启动完整系统或特定子系统。

---

## 文件列表

| 文件 | 用途 | 加载配置 |
|------|------|---------|
| [`sim_demo.launch.py`](sim_demo.launch.py) | 完整仿真演示（模拟器 + 处理 + 控制 + 可视化） | `configs/demo.yaml` + `configs/global_params.yaml` |
| [`processing_only.launch.py`](processing_only.launch.py) | 仅处理模块（适用于真实传感器或外部数据源） | `configs/global_params.yaml` |
| [`replay_bag.launch.py`](replay_bag.launch.py) | 历史 Bag 数据回放 + 离线处理分析 | `configs/global_params.yaml` |

---

## 快速使用

```bash
# 编译工作空间
./scripts/build.sh
# 或
cd ros2_ws && colcon build --symlink-install && source install/setup.bash

# 完整仿真演示
ros2 launch project_bringup sim_demo.launch.py

# 仅启动处理模块（需要外部 /sensor/raw 数据源）
ros2 launch project_bringup processing_only.launch.py

# 回放历史数据
ros2 launch project_bringup replay_bag.launch.py bag_path:=/path/to/bag

# 循环回放
ros2 launch project_bringup replay_bag.launch.py bag_path:=outputs/bags/exp_01 loop:=true
```

---

## Launch 参数说明

### `sim_demo.launch.py`

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_sim_time` | `false` | 是否使用仿真时钟 |
| `config` | `configs/demo.yaml` | 演示场景参数文件 |
| `global_config` | `configs/global_params.yaml` | 全局共享参数文件 |

### `processing_only.launch.py`

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_sim_time` | `false` | 是否使用仿真时钟 |
| `global_config` | `configs/global_params.yaml` | 全局共享参数文件 |

### `replay_bag.launch.py`

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `bag_path` | **必填** | ROS2 Bag 文件路径 |
| `loop` | `false` | 是否循环回放 |
| `use_sim_time` | `true` | 是否使用仿真时钟（回放时建议开启） |
| `global_config` | `configs/global_params.yaml` | 全局共享参数文件 |

---

## 系统数据流

```
[simulator_node] ──/sensor/raw──► [preprocessor_node] ──/sensor/processed──►
  [inference_node] ──/result/inference──► [controller_node] ──/command/control──►
    [safety_gate_node] ──/command/safe──► 执行器
                                          ▲
                                    [visualizer_node]（订阅所有主要话题）
```

---

## 注意事项

- 所有参数均从 `configs/` 目录下的 YAML 文件加载，**不在 launch 文件中硬编码参数值**。
- 回放模式下，建议开启 `use_sim_time:=true` 以使用 Bag 中的时间戳。
- 如需添加新的 launch 文件，请同步更新本 README 的文件列表。
