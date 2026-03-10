# 推理/分类结果消息
std_msgs/Header header
string label               # 预测类别标签
uint32 class_id            # 类别 ID
float32 confidence         # 置信度 [0.0, 1.0]
string model_name          # 使用的模型名称
float32 latency_ms         # 推理耗时（毫秒）
