# ============================================================
# 第2课：变量与运算符
# ============================================================

# ── 1. 变量赋值 ──────────────────────────────────────────────
x = 10  # 普通赋值
y = 3
a = b = c = 0  # 多变量同时赋同一个值
m, n = 5, 8  # 多变量同时赋不同值（解包）

print("=== 变量赋值 ===")
print(a, b, c)  # 0 0 0
print(m, n)  # 5 8

# 交换两个变量（Python 特有的简洁写法）
m, n = n, m
print(m, n)  # 8 5

# ── 2. 算术运算符 ────────────────────────────────────────────
print("\n=== 算术运算符 ===")
print(x + y)  # 加法：13
print(x - y)  # 减法：7
print(x * y)  # 乘法：30
print(x / y)  # 除法（结果为浮点数）：3.3333...
print(x // y)  # 整除（去掉小数）：3
print(x % y)  # 取余（模运算）：1
print(x**y)  # 幂运算：1000（10的3次方）

# ── 3. 赋值运算符（简写） ────────────────────────────────────
print("\n=== 赋值运算符 ===")
num = 10
num += 5  # 等同于 num = num + 5
print(num)  # 15
num -= 3  # 等同于 num = num - 3
print(num)  # 12
num *= 2  # 等同于 num = num * 2
print(num)  # 24
num //= 5  # 等同于 num = num // 5
print(num)  # 4

# ── 4. 比较运算符（结果为 True 或 False） ────────────────────
print("\n=== 比较运算符 ===")
print(10 == 10)  # 等于：True
print(10 != 3)  # 不等于：True
print(10 > 3)  # 大于：True
print(10 < 3)  # 小于：False
print(10 >= 10)  # 大于等于：True
print(10 <= 9)  # 小于等于：False

# ── 5. 逻辑运算符 ────────────────────────────────────────────
print("\n=== 逻辑运算符 ===")
print(True and True)  # and：两者都为True才是True → True
print(True and False)  # → False
print(True or False)  # or：至少一个True就是True → True
print(False or False)  # → False
print(not True)  # not：取反 → False
print(not False)  # → True

# 实际应用示例
score = 85
has_id = True

# 判断是否成绩合格且携带了证件
can_enter = score >= 60 and has_id
print(f"\n成绩{score}分，携带证件：{has_id}")
print(f"能否进入：{can_enter}")  # True

# ── 6. 字符串运算符 ──────────────────────────────────────────
print("\n=== 字符串运算符 ===")
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # 拼接：Hello World
print(s1 * 3)  # 重复：HelloHelloHello
print("ell" in s1)  # 成员检测：True
print("xyz" not in s1)  # 非成员检测：True

# ── 练习题 ───────────────────────────────────────────────────
# TODO: 请尝试以下练习：
# 1. 计算圆的面积，半径 r = 5（面积 = π × r²，π 取 3.14159）
# 2. 判断一个数是否同时满足"大于10"且"是偶数"（提示：偶数 % 2 == 0）
# 3. 用一行代码交换变量 p = "苹果" 和 q = "香蕉"


def calc_circle_area(r: float = 1.0) -> float:
    return 3.14159 * r**2


def number_differentiate(num: int) -> bool:
    return num > 10 and num % 2 == 0


def swap_variables(p: str = "苹果", q: str = "香蕉") -> tuple[str, str]:
    p, q = q, p
    return p, q
