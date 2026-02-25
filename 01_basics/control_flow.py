# ============================================================
# 第3课：流程控制
# ============================================================

# ── 1. if / elif / else ──────────────────────────────────────
print("=== if / elif / else ===")

score = 75

if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")  # 输出这个
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 单行简写（三元表达式）
result = "成年" if score >= 18 else "未成年"
print(result)  # 成年

# ── 2. for 循环 ──────────────────────────────────────────────
print("\n=== for 循环 ===")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# range() 生成数字序列
print("\n1 到 5：")
for i in range(1, 6):  # range(start, stop)，不包含stop
    print(i, end=" ")  # end=" " 让输出在同一行
print()

print("\n0 到 8，步长为 2：")
for i in range(0, 9, 2):  # range(start, stop, step)
    print(i, end=" ")
print()

# enumerate() 同时获取索引和值
print("\n带索引遍历：")
for index, fruit in enumerate(fruits):
    print(f"第{index}个：{fruit}")

# ── 3. while 循环 ────────────────────────────────────────────
print("\n=== while 循环 ===")

count = 1
while count <= 5:
    print(f"第 {count} 次循环")
    count += 1  # 注意：一定要更新变量，否则会无限循环！

# ── 4. break 和 continue ────────────────────────────────────
print("\n=== break 和 continue ===")

# break：立刻退出循环
print("找到第一个偶数就停止：")
for i in range(1, 10):
    if i % 2 == 0:
        print(f"找到了：{i}")
        break

# continue：跳过本次循环，继续下一次
print("\n打印1到10中所有奇数：")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 偶数跳过
    print(i, end=" ")
print()

# ── 5. 嵌套循环 ──────────────────────────────────────────────
print("\n=== 嵌套循环：乘法表 ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # 换行

# ── 练习题 ───────────────────────────────────────────────────
# TODO: 请尝试以下练习：
# 1. 用 for 循环计算 1+2+3+...+100 的和
# 2. 用 while 循环打印 10 到 1 的倒计时
# 3. 遍历列表 [3, 7, 2, 9, 4, 6]，找出其中最大的数


def calc_sum(min: int = 1, max: int = 100) -> int:
    sum = 0
    for i in range(min, max + 1):
        sum += i
    return sum


def count_down(num: int = 10) -> None:
    while num > 0:
        print(num)
        num -= 1


def find_max(arr: list[int]) -> int:
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max
