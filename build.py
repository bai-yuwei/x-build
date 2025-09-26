'''
Author       : Bai_Yuwei(yw_bai@outlook.com)
Version      : V1.0
Date         : 2025-09-16 21:26:32
Description  : 
Modify       : 
'''

import json
import os
import shutil
import sys
import subprocess
from typing import List, Dict, Optional
from pathlib import Path

class ConfigManager:
    def __init__(self):
        self.data = None
        self.file = "buildConfig.json"
        self.load()
    
    def load(self):
        try:
            with open(self.file, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"配置文件未找到: {self.file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON 解析错误: {e}")
        
    @property
    def get_version(self) -> int:
        return self.data.get("version", 0)
    
    def get_all_configs(self) -> List[Dict]:
        """获取所有配置项"""
        return self.data.get('config', [])
    
    def get_all_config_names(self) -> List[str]:
        if not isinstance(self.data, dict):
            return []
        configs = self.data.get('config')
        if not isinstance(configs, list):
            return []
        names = []
        for config in configs:
            if not isinstance(config, dict):
                continue
            name = config.get('name')
            if isinstance(name, str) and name.strip():
                names.append(name)
        return names

    def get_config(self, name: str) -> Optional[Dict]:
        """根据名称获取特定配置项"""
        for config in self.data.get('config', []):
            if config.get('name') == name:
                return config
        return None

    def get_cflags(self, name: str) -> List[str]:
        config = self.get_config(name)
        if config:
            return config.get('cflags', [])
        return []
    
    def get_lflags(self, name: str) -> List[str]:
        config = self.get_config(name)
        if config:
            return config.get('lflags', [])
        return []
    
    def get_platform(self, name: str) -> str:
        config = self.get_config(name)
        if config:
            return config.get('platform', "winArm")
        return "winArm"
    
    def get_compiler(self, name: str) -> str:
        config = self.get_config(name)
        if config:
            return config.get('compiler', "gcc")
        return "gcc"
    def get_type(self, name: str) -> str:
        config = self.get_config(name)
        if config:
            return config.get('type', "debug")
        return "debug"
    


def build_project(project, platform, compiler, buildType):
    """使用新式 CMake 命令构建项目"""
    
    # 确保构建目录存在
    build_dir = f"build/{project}"
    script_dir = Path(__file__).parent.absolute()
    os.makedirs(build_dir, exist_ok=True)
    
    try:
        # 配置项目（使用 -S 和 -B 参数）
        print("配置 CMake 项目...")
        subprocess.run([
            "cmake", 
            "-S", f"{script_dir}/code/{project}",
            "-B", build_dir,
            "-G", "Ninja",
            f"-DCMAKE_TOOLCHAIN_FILE={script_dir}/config/{platform}/{platform}-{compiler}.cmake",
            f"-DCMAKE_BUILD_TYPE={buildType}"
        ], check=True)
        
        # 构建项目
        print("构建项目...")
        subprocess.run([
            "cmake",
            "--build", build_dir
        ], check=True)

        print("install项目...")
        subprocess.run([
            "cmake",
            "--install", build_dir
        ], check=True)
        
        print("构建成功!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"构建失败: {e}")
        return False

def clean_build_directory(project):
    """使用纯 Python 清理构建目录（完全跨平台）"""
    build_dir = Path("build") / project
    
    if not build_dir.exists():
        print(f"No build directory to clean for project: {project}")
        return True
    
    print(f"Cleaning build directory: {build_dir}")
    
    # 递归删除目录及其内容
    try:
        for item in build_dir.iterdir():
            if item.is_file():
                item.unlink()  # 删除文件
            elif item.is_dir():
                shutil.rmtree(item)  # 删除子目录
        
        # 如果目录为空，尝试删除它
        if not any(build_dir.iterdir()):
            build_dir.rmdir()
            
        print(f"Successfully cleaned build directory: {build_dir}")
        return True
    except Exception as e:
        print(f"Error cleaning build directory: {e}")
        return False

if __name__ == "__main__":
    config_manager = ConfigManager()
    projects = config_manager.get_all_config_names()
    for project in projects:
        print(f"Building project: {project}...")
        cflags = config_manager.get_cflags(project)
        lflags = config_manager.get_lflags(project)
        platform = config_manager.get_platform(project)
        compiler = config_manager.get_compiler(project)
        buildType = config_manager.get_type(project)
        
        print(f"Platform: {platform}")
        print(f"Compiler: {compiler}")
        print(f"Type: {buildType}")
        print(f"CFLAGS: {' '.join(cflags)}")
        print(f"LFLAGS: {' '.join(lflags)}")
        
        if len(sys.argv) > 1 and sys.argv[1] == "clean":
            build_dir = f"build/{project}"
            if os.path.exists(build_dir):
                print(f"Cleaning build directory: {build_dir}")
                clean_build_directory(project)
            else:
                print(f"No build directory to clean for project: {project}")
        else:
            build_project(project, platform, compiler, buildType)
