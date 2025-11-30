# 第一阶段：命名构建阶段为 builder
FROM ubuntu:22.04 AS builder

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# 使用LABEL设置维护者信息
LABEL maintainer="yw_bai@outlook.com"

# 将环境变量设置与apt命令放在同一行，限制其作用域
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y \
    build-essential \
    curl \
    wget \
    git \
    vim \
    nano \
    net-tools \
    iputils-ping \
    ca-certificates \
    software-properties-common \
    lsb-release \
    gnupg2 \
    apt-transport-https \
    unzip \
    zip \
    jq \
    file \
    findutils \
    sed \
    perl \
    coreutils \
    binutils \
    dos2unix \
    pip \
    python3 \
    bc \
    dumb-init \
    # ... 其他您确实需要的工具，考虑移除如vim/nano等非必需项 \
    && pip install docker==6.0.0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# COPY ./code  ./code
COPY ./docker/ubuntu/tools ./tools
RUN ls -la ./tools/ && pwd
# 安装工具链
RUN chmod +x ./tools/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.1.15-2.1.0_20241230.sh && \
    printf "\nY\n" | ./tools/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.1.15-2.1.0_20241230.sh

    # 根据实际需求设置CMD。如果仅为交互式环境，则保留bash
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["echo", "容器已启动，等待构建命令..."]
# # 编译代码：确保在 builder 阶段内加载环境变量并编译
# WORKDIR /workspace/code
# RUN chmod +x ./build.sh && \
#     bash -c " \
#     source /opt/fsl-imx-x11/4.1.15-2.1.0/environment-setup-cortexa7hf-neon-poky-linux-gnueabi && \
#     echo '=== 环境变量已加载，开始编译 ===' && \
#     ./build.sh \
#     "
# RUN ls -la /workspace/code/tmp/

# # 第二阶段：专门用于产出成果物的阶段
# FROM scratch AS artifact
# # 从 builder 阶段复制编译产物到当前阶段的根目录
# # 请根据实际编译输出路径调整下面的源路径
# COPY --from=builder /workspace/code/tmp/* /