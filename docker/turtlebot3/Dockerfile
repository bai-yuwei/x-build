# 使用ROS2 Humble + Gazebo的基础镜像
FROM osrf/ros:humble-desktop

# 设置工作目录
WORKDIR /workspace

# 避免交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 安装必要的工具和TurtleBot3包
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-pip \
    python3-colcon-common-extensions \
    ros-humble-turtlebot3* \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-rviz2 \
    ros-humble-nav2-bringup \
    ros-humble-slam-toolbox \
    git \
    wget \
    dumb-init \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# 创建Gazebo模型目录并预下载模型（避免黑屏问题）
RUN mkdir -p /root/.gazebo/models && \
    cd /root/.gazebo/models && \
    wget -q https://github.com/osrf/gazebo_models/archive/refs/heads/master.tar.gz -O gazebo_models.tar.gz && \
    tar -xzf gazebo_models.tar.gz --strip-components=1 && \
    rm gazebo_models.tar.gz

ENV DISPLAY=host.docker.internal:0
ENV QT_X11_NO_MITSHM=1


# # 复制源码到容器工作空间
# COPY ./src /workspace/src

# # 编译工作空间
# RUN bash -c "cd /workspace && source /opt/ros/humble/setup.bash && colcon build"

# # 设置环境变量
# ENV TURTLEBOT3_MODEL=burger

# # 设置启动时自动source环境
# RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
# RUN echo "source /workspace/install/setup.bash" >> ~/.bashrc

# # 复制启动脚本
# COPY start_simulation.sh /workspace/start_simulation.sh
# RUN chmod +x /workspace/start_simulation.sh

# 设置容器启动命令
# CMD ["/bin/bash", "-c", "source ~/.bashrc && /workspace/start_simulation.sh"]
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["echo", "容器已启动，DISPLAY 设置为 host.docker.internal:0"]