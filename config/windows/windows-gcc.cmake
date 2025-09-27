cmake_minimum_required(VERSION 3.10)

include("${CMAKE_CURRENT_LIST_DIR}/../config.cmake")


set(CROSS_PREFIX "")
set(CROSS_SUFFIX "")

# 固定编译器路径，请根据实际安装路径修改，避免配置全局变量
set(C_COMPILER_PATH "D:/buildTool/mingw64/bin")
set(CXX_COMPILER_PATH "D:/buildTool/mingw64/bin")
set(ASM_COMPILER_PATH "D:/buildTool/mingw64/bin")

set(CMAKE_C_COMPILER "${C_COMPILER_PATH}/${CROSS_PREFIX}gcc${CROSS_SUFFIX}.exe")
set(CMAKE_CXX_COMPILER "${CXX_COMPILER_PATH}/${CROSS_PREFIX}g++${CROSS_SUFFIX}.exe")



set(
    CFLAGS
    -m64
)

set(
    LFLAGS
)

set(
    AFLAGS
)