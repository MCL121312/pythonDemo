"""
Python 学习项目主入口

用法：
    python main.py                  # 显示课程列表
    python main.py 1                # 运行第1课：基本数据类型
    python main.py 2                # 运行第2课：变量与运算符
    python main.py 3                # 运行第3课：流程控制
    python main.py 4                # 运行第4课：函数
    python main.py 5                # 运行第5课：内置数据结构
"""

import sys
import importlib

data_types = importlib.import_module("01_basics.data_types")
variables_operators = importlib.import_module("01_basics.variables_operators")
control_flow = importlib.import_module("01_basics.control_flow")
functions = importlib.import_module("01_basics.functions")
data_structures = importlib.import_module("01_basics.data_structures")

# (课程名, 运行函数)
lessons = {
    "1": ("第1课：基本数据类型", data_types.answers.answer),
    "2": ("第2课：变量与运算符", variables_operators.answers.answer),
    "3": ("第3课：流程控制", control_flow.answers.answer),
    "4": ("第4课：函数", functions.answers.answer),
    "5": ("第5课：内置数据结构", data_structures.run),
}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("可用课程：")
        for key, (name, _) in lessons.items():
            print(f"  {key} - {name}")
        print("\n用法：python main.py <课程编号>")
    else:
        choice = sys.argv[1]
        if choice in lessons:
            name, run_func = lessons[choice]
            print(f"=== {name} ===\n")
            run_func()
        else:
            print(f"未找到课程 {choice}，可用编号：{', '.join(lessons.keys())}")
