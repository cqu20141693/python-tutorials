# 题目：从一份观众中抽出30%的人作为幸运观众
import random

names = (input("请输入11个人得姓名；"))
names1 = list(names)
a = len(names1)
b = int(a * 0.3)
print(random.sample(names1, b))


