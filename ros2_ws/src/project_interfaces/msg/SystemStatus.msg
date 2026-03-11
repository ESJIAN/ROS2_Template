# 系统状态消息
std_msgs/Header header
bool healthy               # 系统整体是否健康
string active_mode         # 当前运行模式
string[] active_nodes      # 当前活跃节点列表
float32 cpu_usage          # CPU 使用率（可选）
float32 mem_usage          # 内存使用率（可选）
string message             # 状态描述（用于调试）
