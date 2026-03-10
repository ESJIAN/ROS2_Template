# project_visualizer

## 简介

实时可视化与诊断层，提供数据波形显示、推理结果仪表盘和系统状态监控。

## 节点

### `visualizer_node`

| 项目 | 说明 |
|------|------|
| **功能** | 实时绘制传感器波形和推理结果 |
| **输入** | `/sensor/raw`, `/sensor/processed`, `/result/inference` |
| **配置** | `config/visualizer.yaml` |

### `dashboard_node`

| 项目 | 说明 |
|------|------|
| **功能** | 终端结构化状态仪表盘 |
| **输入** | `/result/inference`, `/system/status`, `/command/control` |
| **配置** | `config/visualizer.yaml` |

## 启动

```bash
# 启动所有可视化（默认）
ros2 launch project_visualizer visualizer.launch.py

# 仅启动仪表盘
ros2 launch project_visualizer visualizer.launch.py use_dashboard:=true
```

## 可视化面板

| 面板 | 数据来源 | 说明 |
|------|---------|------|
| 原始数据波形 | `/sensor/raw` | 原始传感器信号 |
| 处理后波形 | `/sensor/processed` | 预处理后信号 |
| 推理结果 | `/result/inference` | 实时分类标签 + 置信度 |
| 控制命令 | `/command/control` | 已执行命令统计 |
| 系统状态 | `/system/status` | 节点健康状态 |

## Web UI 扩展

如需 Web 仪表盘，参考 `web_ui/` 目录中的 Flask/FastAPI 示例。
