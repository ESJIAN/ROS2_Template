# project_interfaces

## 简介

本包定义项目所有 ROS2 自定义消息、服务和动作类型，是各功能包之间通信的**唯一数据契约**。

## 消息类型

| 类型 | 文件 | 说明 |
|------|------|------|
| msg | `SensorData.msg` | 通用传感器数据 |
| msg | `InferenceResult.msg` | 推理/分类结果 |
| msg | `ControlCommand.msg` | 控制命令 |
| msg | `SystemStatus.msg` | 系统状态 |
| srv | `ResetSession.srv` | 重置会话服务 |
| srv | `SetMode.srv` | 设置运行模式服务 |
| action | `ExecuteCommand.action` | 执行命令动作 |

## 使用方法

### 在其他功能包中依赖

在 `package.xml` 中添加：
```xml
<depend>project_interfaces</depend>
```

在 `CMakeLists.txt` 中添加：
```cmake
find_package(project_interfaces REQUIRED)
```

### Python 中使用

```python
from project_interfaces.msg import SensorData, InferenceResult, ControlCommand
from project_interfaces.srv import ResetSession, SetMode
from project_interfaces.action import ExecuteCommand
```

## Topic 规划

| Topic | 消息类型 | 说明 |
|-------|---------|------|
| `/sensor/raw` | `SensorData` | 原始传感器数据 |
| `/sensor/processed` | `SensorData` | 处理后数据 |
| `/result/inference` | `InferenceResult` | 推理结果 |
| `/command/control` | `ControlCommand` | 控制命令 |
| `/system/status` | `SystemStatus` | 系统状态 |
