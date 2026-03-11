# 快速上手指南

## 前提条件

- 已完成环境配置（见 [`../01_environment/setup.md`](../01_environment/setup.md)）
- 已克隆仓库并进入项目目录

## 第一步：编译工作空间

```bash
./scripts/build.sh
# 或手动：
cd src && colcon build --symlink-install
source install/setup.bash
```

## 第二步：启动演示

```bash
./scripts/run_demo.sh
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
# 启动 RViz（如已配置）
# ros2 launch <bringup_package> rviz.launch.py

# 或启动 Web 仪表盘
# 见 web/README.md
```

## 常用操作速查

| 操作 | 命令 |
|------|------|
| 编译 | `./scripts/build.sh` |
| 启动演示 | `./scripts/run_demo.sh` |
| 录制 Bag | `./scripts/record.sh` |
| 检查环境 | `./scripts/check_env.sh` |

## 常见问题

### 找不到功能包
```bash
source src/install/setup.bash
```

### 节点启动失败
检查日志：
```bash
# 检查 outputs/logs/ 目录
ls outputs/logs/
```
