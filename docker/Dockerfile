# syntax=docker/dockerfile:1
# =============================================================
# Dockerfile — ROS2 Project Template Development Image
# =============================================================

ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}-ros-base

LABEL maintainer="your@email.com"
LABEL description="ROS2 Project Template development environment"

# ── System dependencies ──────────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    ros-${ROS_DISTRO}-rviz2 \
    ros-${ROS_DISTRO}-robot-state-publisher \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    ros-${ROS_DISTRO}-xacro \
    git \
    vim \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# ── Python dependencies ──────────────────────────────────────────
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# ── Workspace setup ──────────────────────────────────────────────
WORKDIR /workspace

COPY ros2_ws/src /workspace/ros2_ws/src

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    cd /workspace/ros2_ws && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build --symlink-install \
      --cmake-args -DCMAKE_BUILD_TYPE=Release

# ── Environment setup ────────────────────────────────────────────
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc && \
    echo "source /workspace/ros2_ws/install/setup.bash" >> ~/.bashrc && \
    echo "export ROS_DOMAIN_ID=0" >> ~/.bashrc

COPY . /workspace

CMD ["/bin/bash"]
