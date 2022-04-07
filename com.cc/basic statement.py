# python中的基本语句
# 条件语句if
"""
if 条件表达式：
执行语句……
elif 条件表达式：
执行语句……
elif 条件表达式：
执行语句……
else：
执行语句……
"""
# 循环语句 for while
# while语句的循环
'''
while 条件表达式：T or F
  循环体
  '''
lh_age = 23
while True:
    age = input('请猜一下他的年龄：')
    if age == 'q' or age == 'Q':
        print('你要才数字')
        break
    elif age.isdigit():  # .isdigit为字符串方法 如果字符串全部由数字组成返回True 反之F
        if int(age) > lh_age:
            print('你说的太老了！')
            continue
        elif int(age) == lh_age:
            print('恭喜你！猜对了!')
            break
        elif int(age) < lh_age:
            print('n你猜的太年轻了')
            continue
    else:
        print('你是真的傻瓜')
# for语句
list1 = [1, 2, 3, 4, 5, 9, 87]
str1 = 'hello world'
for i in list1:
    print(i, 'end=''')
for j in str1:
    print(j, 'end=''')
# for i in range(开始，结束，部长)
x1 = [x ** 3 for x in range(10)]
# x**3   out_exp_res
# x  tem
print(x1)
# 推导式 语法规则
# var=[out_exp_res for item in collection if condition]
"""
out_exp_res:列表生成元素表达式，可以是有返回值的函数
for item in collection:迭代collection将item传入 out_exp_res表达式中
condition：（可选）根据条件过滤列表中的一部分
"""
# 对字符串中的每一个字符进行ASCII标号代码的查找
# while 循环语句
import random as myrandom

a = True
while a:
    n = input("press any key and Enter to get a Random Number,Type Q to quit.")
    if n == 'Q' or n == 'q':
        a = False
    else:
        print(myrandom.randint(1, 6))

# break语句的应用：用来终止循环
list1 = [1, 2, 5, 6, 7, 8]
for i in list1:
    if i == 7:
        break  # 特别要注意缩进
    print(i)
    """
    list1 = [1, 2, 5, 6, 7, 8]
    for i in list1:
        if i == 7:
            break  # 特别要注意缩进 break enter下来之后是和break同级不能输出
            print(i)
        """
# conyinue语句的应用：用来终止当前循环
n = int(input("请输入一个数："))
for i in range(1, n):
    if i == 6:
        print("heoll,world")
        continue
    if i < n - 2:
        print(i + 1)
        continue
    if i == n - 1:
        break
