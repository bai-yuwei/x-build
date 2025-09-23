cmake_minimum_required(VERSION 3.10)

include("${CMAKE_CURRENT_LIST_DIR}/../config.cmake")


set(CROSS_PREFIX "arm-none-eabi-")
set(CROSS_SUFFIX "")

# 固定编译器路径，请根据实际安装路径修改，避免配置全局变量
set(C_COMPILER_PATH "D:/buildTool/gcc-arm-none-eabi-10.3-2021.10/bin")
set(CXX_COMPILER_PATH "D:/buildTool/gcc-arm-none-eabi-10.3-2021.10/bin")
set(ASM_COMPILER_PATH "D:/buildTool/gcc-arm-none-eabi-10.3-2021.10/bin")

set(CMAKE_C_COMPILER "${C_COMPILER_PATH}/${CROSS_PREFIX}gcc${CROSS_SUFFIX}.exe")
set(CMAKE_CXX_COMPILER "${CXX_COMPILER_PATH}/${CROSS_PREFIX}g++${CROSS_SUFFIX}.exe")
set(CMAKE_ASM_COMPILER "${ASM_COMPILER_PATH}/${CROSS_PREFIX}as${CROSS_SUFFIX}.exe")

set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)


set(
    CFLAGS
    -nostdlib
    -nostdinc
    -fno-builtin
    -fno-stack-protector
    -no-pie
    -fno-pic
)

set(
    LFLAGS
)

set(
    AFLAGS
)