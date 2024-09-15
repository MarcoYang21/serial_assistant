import sys
import os

# 将项目根目录添加到 Python 路径
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

from src.main import main

if __name__ == "__main__":
    main()
