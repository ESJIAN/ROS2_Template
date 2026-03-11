# robot_description

## 简介

机器人描述包，包含 URDF/SRDF 模型、网格文件和 MoveIt 配置资源。

## 目录结构

```
robot_description/
├── urdf/
│   └── robot.urdf.xacro    # 机器人 URDF 模型（Xacro 格式）
├── meshes/                  # 3D 网格文件（.stl / .dae）
├── config/                  # MoveIt / SRDF 配置
└── launch/
    └── display.launch.py    # RViz 显示启动文件
```

## 使用方法

### 在 RViz 中显示机器人模型

```bash
ros2 launch robot_description display.launch.py
```

### 在其他包中引用

```python
# 在 launch 文件中获取 URDF 路径
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

urdf_path = PathJoinSubstitution(
    [FindPackageShare("robot_description"), "urdf", "robot.urdf.xacro"]
)
```

## 自定义机器人

1. 编辑 `urdf/robot.urdf.xacro` 添加关节和链接
2. 将 3D 网格文件放入 `meshes/`
3. 在 URDF 中引用网格：
   ```xml
   <mesh filename="package://robot_description/meshes/link.stl"/>
   ```

## MoveIt 配置（可选）

如使用 MoveIt，在 `config/` 中添加：
- `robot.srdf`：语义机器人描述（碰撞组、末端执行器等）
- `joint_limits.yaml`：关节限位配置
- `kinematics.yaml`：运动学求解器配置
