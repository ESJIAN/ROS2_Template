# 系统架构设计

## 1. 总体设计思路

系统按照职责分层，分为以下几层：

1. **接口层**：统一定义所有 ROS2 消息、服务、动作（`project_interfaces`）
2. **数据/仿真层**：数据源、仿真器（`project_simulator`）
3. **处理/算法层**：数据预处理、特征提取、算法推理（`project_processor`）
4. **执行/控制层**：命令执行、安全门控（`project_controller`）
5. **观测/可视化层**：实时显示、诊断（`project_visualizer`）
6. **实验/工具层**：录制、回放、评估（`experiment_tools`）

## 2. 模块划分

```
┌─────────────────────────────────────────────────────────────┐
│                    project_bringup (启动管理)                 │
└─────────────────────────────────────────────────────────────┘
         │              │              │              │
┌────────▼──────┐ ┌─────▼───────┐ ┌───▼──────────┐ ┌▼──────────────┐
│project_simulator│ │project_     │ │project_      │ │project_       │
│(数据/仿真层)    │ │processor    │ │controller    │ │visualizer     │
│                 │ │(处理/算法层)│ │(执行/控制层) │ │(可视化层)     │
└─────────────────┘ └─────────────┘ └──────────────┘ └───────────────┘
         │              │              │              │
┌─────────────────────────────────────────────────────────────┐
│               project_interfaces (消息/接口层)                │
└─────────────────────────────────────────────────────────────┘
```

## 3. Topic / Message 设计

| Topic | 消息类型 | Publisher | Subscriber | 频率(Hz) |
|-------|---------|-----------|------------|---------|
| `/sensor/raw` | `project_interfaces/SensorData` | simulator_node | preprocessor_node | 100 |
| `/sensor/processed` | `project_interfaces/SensorData` | preprocessor_node | inference_node | 100 |
| `/result/inference` | `project_interfaces/InferenceResult` | inference_node | controller_node | 10 |
| `/command/control` | `project_interfaces/ControlCommand` | controller_node | — | 10 |
| `/system/status` | `project_interfaces/SystemStatus` | — | — | 1 |

> **注意**：此表为模板，请根据实际项目修改。

## 4. 节点数据流

```
simulator_node
    → /sensor/raw

preprocessor_node
    → /sensor/processed

inference_node
    → /result/inference

safety_gate_node (可选)
    → /command/safe

controller_node
    → /command/control
```

## 5. 参数管理策略

- 所有可调参数存放在各包 `config/*.yaml` 中
- 全局共享参数存放在 `configs/` 顶层目录
- Launch 文件通过 `parameters` 字段加载 YAML 参数
- 禁止在 Python/C++ 代码中硬编码关键参数

## 6. QoS 策略

| 数据类型 | Reliability | Durability | 说明 |
|---------|------------|------------|------|
| 传感器数据 | BestEffort | Volatile | 高频，允许丢包 |
| 控制命令 | Reliable | Volatile | 关键，不允许丢包 |
| 状态信息 | Reliable | TransientLocal | 新订阅者可收到最新值 |
