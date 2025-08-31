cmake_minimum_required(VERSION 3.10)

set(CROSS_PREFIX "")
set(CROSS_SUFFIX "")

set(CMAKE_C_COMPILER "${CROSS_PREFIX}gcc${CROSS_SUFFIX}")
set(CMAKE_CXX_COMPILER "${CROSS_PREFIX}g++${CROSS_SUFFIX}")
set(CMAKE_ASM_COMPILER "${CROSS_PREFIX}nasm${CROSS_SUFFIX}")

set(
    CFLAGS
    -m32
    -nostdilib
    -nostdinc
    -fno-builtin
    -fno-stack-protector
    -no-pie
    -fno-pic
)

set(
    LFLAGS
    -m elf_i386
)

set(
    AFLAGS
)