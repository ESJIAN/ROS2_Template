# web/

Web 可视化界面目录（可选）。

## 用途

提供基于浏览器的系统状态监控界面，作为 RViz 的补充，适用于：
- 无图形界面的远程环境
- 演示展示
- 多人协作监控

## 推荐实现方案

### 方案 A：Flask + rosbridge（轻量）

```
web/
├── app.py               # Flask 应用入口
├── requirements.txt     # Flask, flask-cors, etc.
├── static/
│   ├── css/style.css
│   └── js/ros_bridge.js
└── templates/
    └── index.html
```

依赖：
- `rosbridge_suite`：将 ROS2 topic 暴露为 WebSocket
- Flask：后端服务

### 方案 B：Foxglove Studio（推荐，零代码）

使用 [Foxglove Studio](https://foxglove.dev/) 直接连接 ROS2：

```bash
# 安装 foxglove_bridge
sudo apt install ros-humble-foxglove-bridge

# 启动 bridge
ros2 launch foxglove_bridge foxglove_bridge_launch.xml
# 打开浏览器访问 https://studio.foxglove.dev
```

## 开发指南

1. 在 `static/js/` 中实现 WebSocket 订阅逻辑
2. 在 `templates/index.html` 中实现可视化界面
3. 参考 `rosbridge_suite` 的 API 文档
