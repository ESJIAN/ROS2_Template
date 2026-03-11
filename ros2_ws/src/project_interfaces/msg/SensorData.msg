# 通用传感器数据消息
std_msgs/Header header
uint32 sample_index        # 采样序号（用于检测丢包）
float32[] data             # 原始数据数组（长度由通道数决定）
string source              # 数据来源标识（simulator / device）
