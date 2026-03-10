# project_controller

## 简介

执行控制层，负责将推理结果经安全过滤后转换为执行器可接受的控制命令。

## 节点

### `safety_gate_node`

| 项目 | 说明 |
|------|------|
| **功能** | 置信度门控、频率限制、重复命令抑制 |
| **输入** | `/result/inference` (`InferenceResult`) |
| **输出** | `/command/safe` (`ControlCommand`) |
| **配置** | `config/safety.yaml` |

### `controller_node`

| 项目 | 说明 |
|------|------|
| **功能** | 将安全命令映射为执行器控制命令 |
| **输入** | `/command/safe` (`ControlCommand`) |
| **输出** | `/command/control` (`ControlCommand`) |
| **配置** | `config/controller.yaml` |

## 启动

```bash
ros2 launch project_controller controller.launch.py
```

## 配置参数

### safety.yaml

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `min_confidence` | `0.6` | 最低置信度门控 |
| `min_command_interval_sec` | `0.5` | 最小命令间隔（秒） |
| `suppress_repeated_commands` | `true` | 是否抑制重复命令 |

### controller.yaml

| 参数 | 类型 | 说明 |
|------|------|------|
| `command_map` | dict | 命令类型映射表 |

## 安全设计原则

1. **置信度门控**：低置信度的推理结果不会触发执行
2. **频率限制**：防止执行器被过于频繁的命令冲击
3. **重复抑制**：相同命令连续发出时只执行一次
4. **安全标志**：所有从此层输出的命令均带有 `is_safe=true` 标志
