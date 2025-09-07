import yaml
import sys
import subprocess
import os

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if arguments[0] == "help" or len(arguments) == 0:
        print("Available build targets:")
        print("  <project>      - Config specific project (e.g., project1, project2)")
        print("  <configFile>   - Config specific file (e.g., user.yaml, debug.yaml), must be placed in the project directory")
    else:
        with open(f'./code/{arguments[0]}/{arguments[1]}', 'r') as file:
            config = yaml.safe_load(file)
        with open(f'./build/{arguments[0]}/Compilation.txt', 'w') as file:
            for key, value in config.items():
                if ("cflag" in key) :
                    file.write(f"{value} ")
        with open(f'./build/{arguments[0]}/Link.txt', 'w') as file:
            for key, value in config.items():
                if ("lflag" in key) :
                    file.write(f"{value} ")
