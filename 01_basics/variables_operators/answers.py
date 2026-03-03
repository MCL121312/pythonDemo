def answer():
    print("=== 练习题 ===")
    print("=== 1. 计算圆的面积，半径 r = 5（面积 = π × r²，π 取 3.14159） ===")
    r = 5
    print(calc_circle_area(r))

    # 2.
    print(
        "=== 2. 判断一个数是否同时满足"
        "大于10"
        "且"
        "是偶数"
        "（提示：偶数 % 2 == 0） ==="
    )
    num = 12
    print(number_differentiate(num))

    # 3.
    print('=== 3. 用一行代码交换变量 p = "苹果" 和 q = "香蕉" ===')
    p, q = "苹果", "香蕉"
    print(swap_variables(p, q))


def calc_circle_area(r: float = 1.0) -> float:
    return 3.14159 * r**2


def number_differentiate(num: int) -> bool:
    return num > 10 and num % 2 == 0


def swap_variables(p: str = "苹果", q: str = "香蕉") -> tuple[str, str]:
    p, q = q, p
    return p, q


if __name__ == "__main__":
    answer()

