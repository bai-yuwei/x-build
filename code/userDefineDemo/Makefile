# 定义编译器，例如 gcc
CC = gcc
# 定义编译选项，-Wall 是开启大部分警告，-g 是添加调试信息
CFLAGS = -Wall -g

# 最终生成的可执行文件的名字
TARGET = main

# 默认目标，输入 make 默认就会执行这个目标
all: $(TARGET)

# 链接规则：告诉 make 如何从 .o 文件链接成可执行文件
# main: main.o 这样写也可以，make 知道如何生成 main.o
$(TARGET): main.o
	$(CC) -o $@ $^

# 编译规则：告诉 make 如何从 .c 文件编译成 .o 文件
# 这是一个模式规则，% 是一个通配符
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# 清理规则：删除编译过程中生成的 .o 文件和最终的可执行文件
.PHONY: clean
clean:
	rm -f *.o $(TARGET)