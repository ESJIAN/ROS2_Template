# 控制命令消息
std_msgs/Header header
string command_type        # 命令类型（e.g. "move", "stop", "reset"）
string target_name         # 目标名称（可选）
geometry_msgs/Pose target_pose  # 目标位姿（可选）
float32 confidence         # 来源置信度（用于安全门控）
bool is_safe               # 是否通过安全检查
