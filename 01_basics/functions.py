# ============================================================
# 第4课：函数
# ============================================================

# ── 1. 定义和调用函数 ────────────────────────────────────────
print("=== 基本函数 ===")

def greet():
    """这是函数的说明文档（docstring）"""
    print("你好，世界！")

greet()  # 调用函数

# ── 2. 参数 ──────────────────────────────────────────────────
print("\n=== 参数 ===")

# 位置参数
def greet_person(name, age):
    print(f"你好，我是{name}，今年{age}岁。")

greet_person("张三", 18)
greet_person("李四", 25)

# 默认参数（有默认值的参数放在后面）
def greet_with_default(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet_with_default("王五")           # 使用默认问候语
greet_with_default("赵六", "早上好") # 覆盖默认值

# 关键字参数（调用时指定参数名，顺序可以不同）
greet_person(age=20, name="小明")

# ── 3. 返回值 ────────────────────────────────────────────────
print("\n=== 返回值 ===")

def add(a, b):
    return a + b  # 返回计算结果

result = add(3, 5)
print(f"3 + 5 = {result}")  # 8

# 返回多个值（实际上是返回一个元组）
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(f"最小值：{low}，最大值：{high}")  # 1, 9

# ── 4. 作用域 ────────────────────────────────────────────────
print("\n=== 作用域 ===")

x = 100  # 全局变量

def show_scope():
    y = 200  # 局部变量，只在函数内部有效
    print(f"函数内部可以访问全局变量 x = {x}")
    print(f"函数内部的局部变量 y = {y}")

show_scope()
print(f"函数外部 x = {x}")
# print(y)  # ← 这行会报错！y 是局部变量，外部无法访问

# ── 5. 可变参数 ──────────────────────────────────────────────
print("\n=== 可变参数 ===")

# *args：接收任意数量的位置参数（存为元组）
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5)) # 15

# **kwargs：接收任意数量的关键字参数（存为字典）
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}：{value}")

print("个人信息：")
print_info(姓名="张三", 年龄=18, 城市="北京")

# ── 练习题 ───────────────────────────────────────────────────
# TODO: 请尝试以下练习：
# 1. 写一个函数 is_even(n)，判断 n 是否为偶数，返回 True 或 False
# 2. 写一个函数 factorial(n)，计算 n 的阶乘（n! = 1×2×3×...×n）
# 3. 写一个函数 greet_many(*names)，向多个人打招呼

