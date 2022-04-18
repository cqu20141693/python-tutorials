# 题目：输入三个整数x,y,z，请把这三个数由小到大输出
# 思路 首先 的让用户输入三个整数，在对赛格数排序 可以想到列表中的sort方法
list1 = []
for i in range(3):
    a = int(input('请输入一个整数：'))
    list1.append(a)
list1.sort()
print(list1)