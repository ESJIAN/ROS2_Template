# 环境配置指南

## 系统要求

| 组件 | 版本 | 备注 |
|------|------|------|
| Ubuntu | 22.04 LTS | 推荐 |
| ROS2 | Humble / Iron / Jazzy | 根据需求选择 |
| Python | 3.10+ | |
| CMake | 3.22+ | |

## ROS2 安装

参考官方文档：https://docs.ros.org/en/humble/Installation.html

```bash
# 以 Humble 为例（Ubuntu 22.04）
sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install -y curl
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
  http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
  | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt upgrade -y
sudo apt install -y ros-humble-desktop ros-dev-tools
source /opt/ros/humble/setup.bash
```

## Python 依赖

```bash
pip install -r requirements.txt
# 或使用项目脚本
./scripts/setup_env.sh
```

## 工作空间依赖

```bash
# 在项目根目录下运行
rosdep install --from-paths src --ignore-src -r -y
```

## Docker 使用（推荐隔离开发）

```bash
cd docker
docker compose build
docker compose up -d
docker compose exec ros2 bash
```

详见 [`../../docker/README.md`](../../docker/README.md)

## 环境验证

```bash
./scripts/check_env.sh
```

## 常见问题

### Q: 找不到 ROS2 命令
确保 source 了 ROS2 环境：
```bash
source /opt/ros/humble/setup.bash
# 建议写入 ~/.bashrc
```

### Q: 依赖包缺失
```bash
# 在项目根目录下运行
rosdep install --from-paths src --ignore-src -r -y
```
