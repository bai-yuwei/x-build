# x-build
嵌入式跨平台构建框架

## 目录结构
```
├─build                -- 成果物路径
├─code                 -- 源码仓
│  ├─WindowsDemo       -- windows编译示例工程
│  ├─WinArmDemo        -- windows交叉编译示例工程
│  └─ubootDemo         -- uboot示例工程（docker构建）
├─config               -- 配置仓
│  ├─winArm            -- windows交叉编译配置（示例）
│  ├─windows           -- windows编译配置（示例）
│  └─config.cmake      -- 通用配置cmake
├─docker               -- Dockerfile
├─repo                 -- repo仓
├─x-build-source       -- x-build源码（https://github.com/bai-yuwei/x-build-source）
└─build.py             -- 构建入口脚本
```
## 使用说明
### 单平台编译
1. 编辑`buildConfig,json`，配置要编译的工程
2. 编辑`config`下的`cmake`文件，配置编译器本地路径
3. 运行`build.exe`，执行编译
4. 查看`build`目录，查看编译成果
5. 运行`build.exe clean`，清理编译成果
6. 运行`build.exe dclean`，清理全部编译环境
### 跨平台编译
1. 编辑`buildConfig,json`，配置要编译的工程
2. 启动docker容器
3. 配置Docker目录下的Dockerfile
4. 运行`build.exe`，执行编译
5. 查看`build`目录，查看编译成果
6. 运行`build.exe clean`，清理编译成果
7. 运行`build.exe dclean`，清理全部编译环境
