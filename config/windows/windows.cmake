cmake_minimum_required(VERSION 3.10)

set(CROSS_PREFIX "")
set(CROSS_SUFFIX "")

set(C_COMPILER_PATH "D:/buildTool/mingw64/bin")
set(CXX_COMPILER_PATH "D:/buildTool/mingw64/bin")
set(ASM_COMPILER_PATH "D:/buildTool/mingw64/bin")

set(CMAKE_C_COMPILER "${CROSS_PREFIX}gcc${CROSS_SUFFIX}")
set(CMAKE_CXX_COMPILER "${CROSS_PREFIX}g++${CROSS_SUFFIX}")
set(CMAKE_ASM_COMPILER "${CROSS_PREFIX}as${CROSS_SUFFIX}")

set(
    CFLAGS
    -m32
    -nostdlib
    -nostdinc
    -fno-builtin
    -fno-stack-protector
    -no-pie
    -fno-pic
)

set(
    LFLAGS
    -m32
)

set(
    AFLAGS
)