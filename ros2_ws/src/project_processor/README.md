# project_processor

## 简介

数据处理与算法推理层，负责对原始传感器数据进行预处理并执行模型推理。

## 节点

### `preprocessor_node`

| 项目 | 说明 |
|------|------|
| **功能** | 数据滤波、归一化等预处理 |
| **输入** | `/sensor/raw` (`SensorData`) |
| **输出** | `/sensor/processed` (`SensorData`) |
| **配置** | `config/preprocess.yaml` |

### `inference_node`

| 项目 | 说明 |
|------|------|
| **功能** | 特征提取 + 模型推理 |
| **输入** | `/sensor/processed` (`SensorData`) |
| **输出** | `/result/inference` (`InferenceResult`) |
| **配置** | `config/inference.yaml` |

## 启动

```bash
ros2 launch project_processor processor.launch.py
```

## 配置参数

### preprocess.yaml

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `normalize` | `true` | 是否归一化 |
| `buffer_size` | `100` | 数据缓冲大小 |

### inference.yaml

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `model_name` | `threshold` | 使用的模型类型 |
| `confidence_threshold` | `0.5` | 置信度阈值 |
| `model_path` | `""` | 模型文件路径 |

## 扩展指南

### 添加新的预处理步骤
在 `preprocessor_node.py` 的 `_callback` 方法中添加处理逻辑。

### 替换推理模型
1. 修改 `inference_node.py` 的 `_infer` 方法
2. 更新 `config/inference.yaml` 中的 `model_name` 和 `model_path`
3. 将模型文件放入 `datasets/models/`
