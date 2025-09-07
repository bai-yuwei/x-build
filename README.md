# x-build
嵌入式跨平台构建框架

## 目录结构
```
├─build                -- 成果物路径
├─code                 -- 源码仓
│  └─WindowsDemo       -- windows类型示例工程
│     └─user.yaml     -- 局部编译/链接指令/选项配置文件
├─config               -- 配置仓
│  ├─windows           -- windows类型编译配置（示例）
│  ├─config.cmake      -- 通用配置cmake
│  └─config.yaml       -- 编译器本地路径配置
├─docker               -- Dockerfile
├─repo                 -- repo仓
├─build.exe            -- 构建入口脚本
└─config.exe           -- 配置入口脚本
```
## 使用说明（单工程）
1. 编辑`config/config.yaml`，配置编译器本地路径
2. 编辑`code/project/*.yaml`，配置工程编译/链接指令/选项（按需）
3. 运行`config.exe <project> <*.yaml>`，配置工程
4. 运行`build.exe <project>`，执行编译
## 使用说明（多工程）
1. 编辑`config/config.yaml`，配置编译器本地路径
2. 编辑`code/project/*.yaml`，配置工程编译/链接指令/选项（按需）
3. 运行`config.exe <project1> <*.yaml>`，配置工程1
4. 运行`config.exe <project2> <*.yaml>`，配置工程2
5. 重复步骤3、4，配置其他工程
6. 运行`build.exe <project1> <project2> ...`执行编译或运行`build.exe all`编译所有`code`下的工程
## 开发说明
1. `config/platform`中的`cmake`文件为平台相关的通用`cmake`配置，一般包含编译器/通用编译/链接选项等
2. `code/project`中的主`CmakeLists.txt`文件需要`include` `config`中对应的`cmake`文件
3. `code/project`中的主`CmakeLists.txt`文件需要读取对应`build/project`目录下基于`code/project/*.yaml`生成的`Compilation.txt`和`Link.txt`