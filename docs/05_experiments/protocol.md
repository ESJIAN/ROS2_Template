# 实验方案与评估协议

## 实验目标

> 在此描述实验要验证的假设和目标。

## 实验设计

### 实验一：基线性能验证

**目的**：验证系统基础功能正常运行。

**步骤**：
1. 启动仿真演示：`ros2 launch project_bringup sim_demo.launch.py`
2. 录制 Bag 文件：`./scripts/record.sh`
3. 计算指标：`python ros2_ws/src/experiment_tools/scripts/compute_metrics.py`

**评估指标**：
- 处理延迟（ms）
- 吞吐量（msg/s）
- （项目特定指标）

### 实验二：算法对比

**目的**：比较不同算法在相同数据上的性能。

**步骤**：
1. （填写）

## 数据管理

| 数据类型 | 存放位置 | 备注 |
|---------|---------|------|
| 原始数据 | `datasets/raw/` | 不提交到 git |
| 处理后数据 | `datasets/processed/` | 不提交到 git |
| 训练模型 | `datasets/models/` | 不提交到 git |
| 实验报告 | `outputs/reports/` | 可提交 |

## 结果记录模板

```markdown
## 实验记录

- **日期**：YYYY-MM-DD
- **实验名称**：
- **数据集**：
- **参数配置**：见 `configs/experiment_XX.yaml`
- **结果**：
  - 指标一：
  - 指标二：
- **结论**：
- **下一步**：
```

## 复现步骤

1. 确保环境一致（见 `docs/01_environment/setup.md`）
2. 使用固定随机种子
3. 使用相同的 `configs/experiment_XX.yaml`
4. 回放相同的 Bag 文件
