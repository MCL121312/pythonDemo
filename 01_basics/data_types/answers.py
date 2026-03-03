# ── 练习题 ───────────────────────────────────────────────────
# TODO: 请尝试以下练习：
# 1. 创建一个变量存储你的名字，用 f-string 打印一句自我介绍
# 2. 将字符串 "2026" 转换为整数，并加上 1
# 3. 打印 type("hello") 的结果，看看输出什么


def answer1():
    # 1.
    print("=== 1. 创建一个变量存储你的名字，用 f-string 打印一句自我介绍 ===")
    my_name = "mcl"
    print(f"我叫{my_name}")


def answer2():
    # 2.
    print('=== 2. 将字符串 "2026" 转换为整数，并加上 1 ===')
    year = "2026"
    print(int(year) + 1)


def answer3():
    # 3.
    print('=== 3. 打印 type("hello") 的结果，看看输出什么===')
    print(type("hello"))


def answer():
    answer1()
    answer2()
    answer3()


if __name__ == "__main__":
    answer()
