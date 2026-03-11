# Docker 使用说明

## 快速开始

```bash
cd docker

# 构建镜像
docker compose build

# 启动容器（交互式）
docker compose up -d
docker compose exec ros2 bash

# 在容器内启动演示
ros2 launch project_bringup sim_demo.launch.py
```

## 挂载说明

| 宿主机路径 | 容器路径 | 说明 |
|-----------|---------|------|
| `../ros2_ws/src` | `/workspace/ros2_ws/src` | 源代码（实时编辑） |
| `../configs` | `/workspace/configs` | 参数配置 |
| `../outputs` | `/workspace/outputs` | 实验输出 |
| `../datasets` | `/workspace/datasets` | 数据集 |

## GUI 显示（X11）

Linux 下需要允许 Docker 访问 X11：

```bash
xhost +local:docker
docker compose up
```

## 常用命令

```bash
# 进入容器
docker compose exec ros2 bash

# 在容器内重新编译
cd /workspace/ros2_ws && colcon build --symlink-install

# 停止容器
docker compose down
```
