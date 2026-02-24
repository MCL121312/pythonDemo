# ============================================================
# 第1课：基本数据类型
# Python 中有四种最常用的基本数据类型
# ============================================================

# ── 1. 整数 int ──────────────────────────────────────────────
age = 18
year = 2026
negative = -100

print("=== 整数 int ===")
print(age)           # 18
print(type(age))     # <class 'int'>

# ── 2. 浮点数 float ──────────────────────────────────────────
price = 9.99
pi = 3.14159

print("\n=== 浮点数 float ===")
print(price)         # 9.99
print(type(price))   # <class 'float'>

# ── 3. 字符串 str ────────────────────────────────────────────
name = "张三"
greeting = '你好，世界！'
# 多行字符串使用三引号
poem = """
床前明月光，
疑是地上霜。
"""

print("\n=== 字符串 str ===")
print(name)          # 张三
print(greeting)      # 你好，世界！
print(type(name))    # <class 'str'>
print(len(name))     # 2  （字符串长度）

# 字符串拼接
full = "你好，" + name + "！"
print(full)          # 你好，张三！

# f-string 格式化（推荐写法）
message = f"我叫{name}，今年{age}岁。"
print(message)

# ── 4. 布尔值 bool ───────────────────────────────────────────
is_student = True
is_adult = False

print("\n=== 布尔值 bool ===")
print(is_student)        # True
print(type(is_student))  # <class 'bool'>

# 布尔值其实是整数的子类：True=1，False=0
print(True + 1)   # 2
print(False + 1)  # 1

# ── 5. 类型转换 ──────────────────────────────────────────────
print("\n=== 类型转换 ===")
print(int("123"))      # 字符串 → 整数：123
print(float("3.14"))   # 字符串 → 浮点数：3.14
print(str(100))        # 整数 → 字符串："100"
print(bool(0))         # 0 → False
print(bool(1))         # 非0 → True
print(bool(""))        # 空字符串 → False
print(bool("hello"))   # 非空字符串 → True

# ── 练习题 ───────────────────────────────────────────────────
# TODO: 请尝试以下练习：
# 1. 创建一个变量存储你的名字，用 f-string 打印一句自我介绍
# 2. 将字符串 "2026" 转换为整数，并加上 1
# 3. 打印 type("hello") 的结果，看看输出什么

# 1.
my_name = "mcl"
print(f"我叫{my_name}")

# 2.
year = "2026"
print(int(year) + 1)

# 3.
print(type("hello"))

