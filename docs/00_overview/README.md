# 项目概述

## 项目背景

> 在此填写项目背景、研究动机、应用场景。

## 系统目标

- **目标一**：（填写）
- **目标二**：（填写）
- **目标三**：（填写）

## 核心特性

| 特性 | 说明 |
|------|------|
| 五层模块化架构 | 各功能层职责单一，可独立替换 |
| 接口统一 | 所有消息/服务/动作在 `src/support/` 支撑层中集中定义 |
| 参数外置 | 所有可调参数通过 `configs/` YAML 配置文件管理 |
| 实验可复现 | 支持 ROS2 Bag 录制、回放与自动评估 |

## 系统架构概览

```
[支撑层]   src/support/    → 接口定义、驱动、工具库
    ↓
[功能层]   src/function/   → 传感器处理、算法模块
    ↓
[决策层]   src/decision/   → 行为决策、任务规划
    ↓
[执行层]   src/execution/  → 运动控制、机构执行
    ↓
[应用层]   src/application/ → 系统启动、可视化、实验工具
```

> 详细架构图见 [`../02_system_design/architecture.md`](../02_system_design/architecture.md)

## 相关资源

- [系统架构文档](../02_system_design/architecture.md)
- [环境配置指南](../01_environment/setup.md)
- [快速上手指南](../04_user_guide/quickstart.md)
