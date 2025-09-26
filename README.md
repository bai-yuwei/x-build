# x-build
嵌入式跨平台构建框架

## 目录结构
```
├─build                -- 成果物路径
├─code                 -- 源码仓
│  └─WinArmDemo        -- windows交叉编译示例工程
├─config               -- 配置仓
│  ├─winArm            -- windows交叉编译配置（示例）
│  └─config.cmake      -- 通用配置cmake
├─docker               -- Dockerfile
├─repo                 -- repo仓
└─build.py            -- 构建入口脚本
```
## 使用说明
1. 编辑`buildConfig,json`，配置要编译的工程
2. 编辑`config`下的`cmake`文件，配置编译器本地路径
3. 运行`build,py`，执行编译
4. 查看`build`目录，查看编译成果
5. 运行`build.py clean`，清理编译成果
