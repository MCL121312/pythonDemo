"""
Python 学习项目主入口
"""

import importlib

# 动态导入模块
data_types = importlib.import_module('01_basics.data_types')
variables_operators = importlib.import_module('01_basics.variables_operators')
control_flow = importlib.import_module('01_basics.control_flow')
functions = importlib.import_module('01_basics.functions')
data_structures = importlib.import_module('01_basics.data_structures')


def show_menu():
    """显示菜单"""
    print("\n" + "="*50)
    print("Python 基础学习项目")
    print("="*50)
    print("请选择要学习的课程：")
    print("1. 基本数据类型 (int, float, str, bool)")
    print("2. 变量与运算符")
    print("3. 流程控制 (if/for/while)")
    print("4. 函数")
    print("5. 内置数据结构 (list, tuple, dict, set)")
    print("0. 退出")
    print("="*50)


def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("请输入选择 (0-5): ").strip()

        if choice == "1":
            print("\n【第1课：基本数据类型】\n")
            data_types
        elif choice == "2":
            print("\n【第2课：变量与运算符】\n")
            variables_operators
        elif choice == "3":
            print("\n【第3课：流程控制】\n")
            control_flow
        elif choice == "4":
            print("\n【第4课：函数】\n")
            functions
        elif choice == "5":
            print("\n【第5课：内置数据结构】\n")
            data_structures
        elif choice == "0":
            print("\n再见！继续加油学习 Python！👋\n")
            break
        else:
            print("\n❌ 输入错误，请重新选择！\n")


if __name__ == "__main__":
    main()