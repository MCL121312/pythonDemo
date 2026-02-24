# ============================================================
# 第5课：内置数据结构
# ============================================================

# ── 1. 列表 list（有序、可修改） ─────────────────────────────
print("=== 列表 list ===")

fruits = ["苹果", "香蕉", "橙子", "葡萄"]

print(fruits[0])     # 第一个：苹果（索引从0开始）
print(fruits[-1])    # 最后一个：葡萄（负索引从末尾开始）
print(fruits[1:3])   # 切片：['香蕉', '橙子']（不含索引3）

# 常用操作
fruits.append("西瓜")       # 末尾添加
fruits.insert(1, "草莓")    # 在索引1处插入
fruits.remove("香蕉")       # 删除指定元素
popped = fruits.pop()       # 弹出最后一个元素
print(f"弹出：{popped}")
print(f"当前列表：{fruits}")
print(f"长度：{len(fruits)}")

# 列表排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()              # 原地升序排列
print(f"排序后：{numbers}")
numbers.sort(reverse=True)  # 降序
print(f"降序：{numbers}")

# ── 2. 元组 tuple（有序、不可修改） ──────────────────────────
print("\n=== 元组 tuple ===")

point = (3, 7)          # 坐标，定义后不能修改
colors = ("红", "绿", "蓝")

print(point[0])         # 3
print(len(colors))      # 3

# 元组解包
x, y = point
print(f"x={x}, y={y}") # x=3, y=7

# ── 3. 字典 dict（键值对、可修改） ───────────────────────────
print("\n=== 字典 dict ===")

person = {
    "姓名": "张三",
    "年龄": 18,
    "城市": "北京"
}

# 访问值
print(person["姓名"])              # 张三
print(person.get("电话", "未填写")) # get() 不存在时返回默认值

# 修改 / 添加
person["年龄"] = 19        # 修改
person["爱好"] = "编程"    # 新增
del person["城市"]         # 删除

print(f"更新后：{person}")

# 遍历字典
print("所有信息：")
for key, value in person.items():
    print(f"  {key}: {value}")

# 常用方法
print(list(person.keys()))    # 所有键
print(list(person.values()))  # 所有值

# ── 4. 集合 set（无序、不重复） ──────────────────────────────
print("\n=== 集合 set ===")

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s1.add(6)           # 添加元素
s1.discard(1)       # 删除元素（不存在也不报错）

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"交集：{s1 & s2}")   # 两个集合共有的元素
print(f"并集：{s1 | s2}")   # 两个集合所有元素
print(f"差集：{s1 - s2}")   # 在s1中但不在s2中的元素

# 集合的常见用法：列表去重
lst = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(lst))
print(f"去重后：{unique}")

# ── 练习题 ───────────────────────────────────────────────────
# TODO: 请尝试以下练习：
# 1. 创建一个购物车列表，添加3件商品，删除其中一件，然后打印结果
# 2. 创建一个字典存储你的个人信息（姓名、年龄、爱好），并用循环打印
# 3. 找出两个列表 [1,2,3,4,5] 和 [3,4,5,6,7] 中共同包含的数字

