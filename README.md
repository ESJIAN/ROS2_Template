# 🤖 ROS2 Project Template

> **通用 ROS2 工程模板** — 作为所有 ROS2 项目的统一起点，融合工程最佳实践与个人开发习惯。

[![ROS2](https://img.shields.io/badge/ROS2-Humble%20%7C%20Iron%20%7C%20Jazzy-blue)](https://docs.ros.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](https://www.python.org/)

---

## 📑 目录

- [项目简介](#项目简介)
- [顶层目录结构](#顶层目录结构)
- [ROS2 功能包总览](#ros2-功能包总览)
- [快速开始](#快速开始)
- [文档导航](#文档导航)
- [推荐阅读顺序](#推荐阅读顺序)

---

## 项目简介

本仓库是一个**高质量通用 ROS2 项目模板**，特点：

| 特性 | 说明 |
|------|------|
| 五层架构清晰 | support / function / decision / execution / application 分层明确 |
| 接口优先 | `src/support/` 层集中定义所有 msg / srv / action |
| 参数外置 | 所有关键参数放入 `configs/*.yaml`，不写死在代码中 |
| 脚本统一管理 | `scripts/` 目录提供 setup / build / run / record / check 全套脚本 |
| 实验可复现 | `outputs/` 目录支持 Bag 录制、回放与评估报告生成 |
| 文档完善 | 12 大文档子目录，从系统概述到电气设计全覆盖 |

---

## 顶层目录结构

```text
ROS2_Template/
├── README.md               # 本文件 — 项目导航入口
├── LICENSE
├── .gitignore
│
├── docs/                   # 📚 全部文档（见下方文档导航）
├── scripts/                # 🛠  辅助脚本（setup / build / run / check）
├── configs/                # ⚙️  集中参数管理（全局 YAML 配置）
├── assets/                 # 🖼  项目资源文件（图片等）
├── datasets/               # 📦 数据集目录（raw / processed / models）
├── outputs/                # 📁 产出目录（bags / logs / reports / figures）
├── web/                    # 🌐 Web 可视化界面（可选）
├── docker/                 # 🐳 Docker 环境（Dockerfile + compose）
├── tests/                  # 🧪 测试用例
├── temp/                   # 🗂  临时文件目录
└── src/                    # 🤖 ROS2 功能包源码
    ├── support/            # 支撑层（接口定义、驱动、工具库）
    ├── function/           # 功能层（传感器处理、算法模块）
    ├── decision/           # 决策层（行为决策、任务规划）
    ├── execution/          # 执行层（运动控制、机构执行）
    └── application/        # 应用层（系统启动、可视化、实验工具）
```

---

## ROS2 功能包总览

| 层级 | 目录 | 职责说明 |
|------|------|---------|
| 支撑层 | `src/support/` | 接口定义（msg/srv/action）、硬件驱动、公共工具库 |
| 功能层 | `src/function/` | 传感器数据处理、特征提取、算法推理模块 |
| 决策层 | `src/decision/` | 行为决策、任务规划、状态机管理 |
| 执行层 | `src/execution/` | 运动控制、机构执行、安全门控 |
| 应用层 | `src/application/` | 系统启动编排、可视化界面、实验工具 |

---

## 快速开始

### 1. 环境配置

```bash
# 克隆仓库
git clone <your-repo-url>
cd ROS2_Template

# 安装依赖（见 docs/01_environment/setup.md）
./scripts/setup_env.sh
```

### 2. 编译工作空间

```bash
./scripts/build.sh
# 或手动：
cd src && colcon build --symlink-install
source install/setup.bash
```

### 3. 启动系统

```bash
# 一键启动演示
./scripts/run_demo.sh

# 录制 Bag 数据
./scripts/record.sh
```

### 4. 使用 Docker（可选）

```bash
cd docker
docker compose up
```

---

## 文档导航

| 目录 | 内容 |
|------|------|
| [`docs/00_overview/`](docs/00_overview/) | 项目概述、架构图、系统框图 |
| [`docs/01_environment/`](docs/01_environment/) | 环境配置、依赖安装、Docker 使用 |
| [`docs/02_system_design/`](docs/02_system_design/) | 系统设计、模块划分、Topic/Message 设计 |
| [`docs/03_algorithm/`](docs/03_algorithm/) | 核心算法说明、实现原理 |
| [`docs/04_user_guide/`](docs/04_user_guide/) | 用户使用指南、操作说明 |
| [`docs/05_experiments/`](docs/05_experiments/) | 实验方案、评估指标、结果记录 |
| [`docs/06_demo/`](docs/06_demo/) | 演示视频脚本、Demo 运行指南 |
| [`docs/07_dev_log/`](docs/07_dev_log/) | 开发日志、变更记录、里程碑、Issue 跟踪 |
| [`docs/08_meetings/`](docs/08_meetings/) | 会议纪要、重要决策记录 |
| [`docs/09_manuals/`](docs/09_manuals/) | 硬件手册、设备说明书 |
| [`docs/10_3Dmodels/`](docs/10_3Dmodels/) | 三维模型文件（URDF/SRDF/STL 等） |
| [`docs/11_elec_design/`](docs/11_elec_design/) | 电路/电气设计资料 |

---

## 推荐阅读顺序

> 新加入者或首次使用者，建议按以下顺序阅读：

1. 📌 **本文件**（项目导航）
2. 📖 [`docs/00_overview/README.md`](docs/00_overview/README.md)（项目概述）
3. 🔧 [`docs/01_environment/setup.md`](docs/01_environment/setup.md)（环境配置）
4. 🏗 [`docs/02_system_design/architecture.md`](docs/02_system_design/architecture.md)（系统架构）
5. 🧠 [`docs/03_algorithm/README.md`](docs/03_algorithm/README.md)（核心算法）
6. 🚀 [`docs/04_user_guide/quickstart.md`](docs/04_user_guide/quickstart.md)（快速上手）
7. 🧪 [`docs/05_experiments/protocol.md`](docs/05_experiments/protocol.md)（实验方案）
8. 🎬 [`docs/06_demo/demo_script.md`](docs/06_demo/demo_script.md)（演示脚本）

---

## 贡献 & 开发规范

- 分支命名：`feature/<功能名>`、`fix/<问题描述>`、`exp/<实验名>`
- 每次新功能/修复请在 [`docs/07_dev_log/`](docs/07_dev_log/) 中记录变更
- 重要决策请在 [`docs/08_meetings/`](docs/08_meetings/) 中存档

---

## License

MIT License — © 谢承旭
