# ── 练习题 ───────────────────────────────────────────────────
# 在下方写出你的答案，然后运行文件，通过则显示 ✅，否则会报错提示。
def answer():
    # 练习 1：写一个函数 is_even(n)，判断 n 是否为偶数，返回 True 或 False
    def is_even(n):
        pass  # ← 把 pass 替换成你的代码

    # 练习 2：写一个函数 factorial(n)，计算 n 的阶乘（n! = 1×2×3×...×n）
    def factorial(n):
        pass  # ← 把 pass 替换成你的代码

    # 练习 3：写一个函数 greet_many(*names)，向多个人打招呼，返回问候字符串列表
    def greet_many(*names):
        pass  # ← 把 pass 替换成你的代码

    # ── 自动验证（不需要修改这里）────────────────────────────────
    def check(label, got, expected):
        assert got == expected, f"❌ {label}：期望 {expected!r}，实际得到 {got!r}"
        print(f"✅ {label}")

    print("\n=== 练习验证 ===")
    check("is_even(4) 应为 True", is_even(4), True)
    check("is_even(7) 应为 False", is_even(7), False)
    check("is_even(0) 应为 True", is_even(0), True)

    check("factorial(1) 应为 1", factorial(1), 1)
    check("factorial(5) 应为 120", factorial(5), 120)
    check("factorial(0) 应为 1", factorial(0), 1)

    check(
        "greet_many('张三','李四') 应为 ['你好，张三！', '你好，李四！']",
        greet_many("张三", "李四"),
        ["你好，张三！", "你好，李四！"],
    )


if __name__ == "__main__":
    answer()

