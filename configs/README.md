# configs/

集中参数管理目录，存放全局共享配置文件。

## 文件说明

| 文件 | 说明 |
|------|------|
| `global_params.yaml` | 全局共享参数（Topic 名称、传感器设置、安全参数） |
| `demo.yaml` | 演示/答辩用固定参数配置 |
| `experiment_01.yaml` | 实验参数配置模板 |

## 使用原则

1. **全局参数**放 `global_params.yaml`，各包 launch 文件均可加载
2. **实验参数**按实验编号建立独立文件（`experiment_XX.yaml`）
3. **包级参数**放在对应功能包的 `config/` 目录下
4. 禁止在 Python/C++ 代码中硬编码关键参数

## 在 Launch 文件中加载全局参数

```python
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

global_config = "/path/to/configs/global_params.yaml"

node = Node(
    package="...",
    executable="...",
    parameters=[global_config],
)
```
