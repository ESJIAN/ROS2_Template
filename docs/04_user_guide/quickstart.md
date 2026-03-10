# 快速上手指南

## 前提条件

- 已完成环境配置（见 [`../01_environment/setup.md`](../01_environment/setup.md)）
- 已克隆仓库并进入项目目录

## 第一步：编译工作空间

```bash
cd ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## 第二步：启动仿真演示

```bash
ros2 launch project_bringup sim_demo.launch.py
```

## 第三步：查看运行状态

```bash
# 查看所有话题
ros2 topic list

# 查看节点状态
ros2 node list

# 查看某个话题的消息
ros2 topic echo /sensor/raw
```

## 第四步：启动可视化界面

```bash
# 启动 RViz
ros2 launch project_visualizer rviz.launch.py

# 或启动 Web 仪表盘（如已实现）
# 见 web_ui/README.md
```

## 常用操作速查

| 操作 | 命令 |
|------|------|
| 编译 | `./scripts/build.sh` |
| 启动仿真 | `ros2 launch project_bringup sim_demo.launch.py` |
| 录制 Bag | `./scripts/record.sh` |
| 回放 Bag | `ros2 launch project_bringup replay_bag.launch.py bag_path:=<path>` |
| 检查环境 | `./scripts/check_env.sh` |

## 常见问题

### 找不到功能包
```bash
source ros2_ws/install/setup.bash
```

### 节点启动失败
查看日志：
```bash
ros2 launch project_bringup sim_demo.launch.py --show-args
# 检查 outputs/logs/ 目录
```
