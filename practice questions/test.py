# 题目：从一份观众中抽出30%的人作为幸运观众
import random

names = input("请输入11个人得姓名；")
names1 = names.rstrip("'").lstrip("'").split(',')
# 主要是切割字符串，结果返回由字符串元素组成的一个列表
# rstrip 用于出去字符串首尾的字符串，lrstrip 用于出去最左边的字符串
a = len(names1)
b = int(a * 0.3)
print(random.sample(names1, b))
