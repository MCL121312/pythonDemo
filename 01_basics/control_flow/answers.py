def answer():
    print("=== 1. calc_sum(1, 100) ===")
    print(calc_sum(1, 100))

    print("=== 2. count_down(5) ===")
    count_down(5)

    print("=== 3. find_max([3, 1, 7, 2, 9]) ===")
    print(find_max([3, 1, 7, 2, 9]))


# 练习 1：写一个函数 calc_sum(min, max)，计算 min 到 max 的所有整数之和
def calc_sum(min: int = 1, max: int = 100) -> int:
    sum = 0
    for i in range(min, max + 1):
        sum += i
    return sum


# 练习 2：写一个函数 count_down(num)，从 num 开始倒数到 0
def count_down(num: int = 10) -> None:
    while num > 0:
        print(num)
        num -= 1


# 练习 3：写一个函数 find_max(arr)，返回列表 arr 中的最大值
def find_max(arr: list[int]) -> int:
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


if __name__ == "__main__":
    answer()

