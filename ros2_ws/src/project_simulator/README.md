# project_simulator

## 简介

数据源与仿真层，负责生成模拟传感器数据，支持在无真实硬件时测试完整 pipeline。

## 节点

### `simulator_node`

| 项目 | 说明 |
|------|------|
| **功能** | 生成模拟传感器数据流（正弦波 + 噪声） |
| **输出** | `/sensor/raw` (`SensorData`) |
| **配置** | `config/simulator.yaml` |
| **启动** | `ros2 run project_simulator simulator_node.py` |

### `data_source_node`

| 项目 | 说明 |
|------|------|
| **功能** | 真实硬件设备数据桥接（模板，需实现） |
| **输出** | `/sensor/raw` (`SensorData`) |
| **配置** | `config/simulator.yaml` |
| **启动** | `ros2 run project_simulator data_source_node.py` |

## 启动

```bash
# 使用仿真器（默认）
ros2 launch project_simulator simulator.launch.py

# 使用真实设备
ros2 launch project_simulator simulator.launch.py use_device:=true
```

## 配置参数

见 `config/simulator.yaml`：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `sample_rate` | `100.0` | 采样率（Hz） |
| `channel_count` | `8` | 通道数 |
| `signal_amplitude` | `1.0` | 信号幅值 |
| `signal_frequency` | `1.0` | 信号频率（Hz） |
| `noise_amplitude` | `0.1` | 噪声幅值 |
| `random_seed` | `42` | 随机种子 |

## 扩展指南

1. 修改 `simulator_node.py` 中的信号生成逻辑
2. 实现 `data_source_node.py` 中的硬件通信代码
3. 在 `config/simulator.yaml` 中调整参数
