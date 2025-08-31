import yaml
import sys
import subprocess
import os

def get_immediate_subdirectories_listdir(path):
    """
    使用 os.listdir 和 os.path.isdir 获取一级子目录名称列表
    """
    if not os.path.isdir(path): # 检查路径是否为有效目录[2,6](@ref)
        print(f"错误：路径 {path} 不存在或不是一个目录。")
        return []
    all_entries = os.listdir(path)
    subdirs = []
    for entry in all_entries:
        full_path = os.path.join(path, entry) # 组合完整路径[1,2](@ref)
        if os.path.isdir(full_path):
            subdirs.append(entry) # 或者使用 full_path 获取完整路径
    return subdirs


if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(f"Project awaiting build: {arguments}")
    with open('./config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    sys.path.insert(0, config['c_compiler_path'])
    sys.path.insert(1, config['cxx_compiler_path'])
    sys.path.insert(2, config['asm_compiler_path'])
    print("c_compiler_path:", config['c_compiler_path'])
    print("cxx_compiler_path:", config['cxx_compiler_path'])
    print("asm_compiler_path:", config['asm_compiler_path'])
    # print(sys.path)
    if arguments[0] == "help" or len(arguments) == 0:
        print("Available build targets:")
        print("  clean  - Clean all build directories")
        print("  dclean - Deep clean all build directories")
        print("  all    - Build all projects")
        print("  <name> - Build specific project (e.g., project1, project2)")
    elif arguments[0] == "clean":
        for arg in arguments:
            if arg == "clean":
                continue
            subprocess.run(f"cmake --build build/{arg} --target clean")
    elif arguments[0] == "dclean":
        subprocess.run(f"cmake --build build --target clean")
    elif arguments[0] == "all":
        projectList = get_immediate_subdirectories_listdir("code")
        print("Building all projects:", projectList)
        for project in projectList:
            subprocess.run(f"cmake -S ./code/{project} -B build/{project} -G Ninja && cmake --build build/{project}")
    else:
        for arg in arguments:
            subprocess.run(f"cmake -S ./code/{arg} -B build/{arg} -G Ninja && cmake --build build/{arg}")



