# python中的基本语句
# 条件语句if
'''
if 条件表达式：
执行语句……
elif 条件表达式：
执行语句……
elif 条件表达式：
执行语句……
else：
执行语句……
'''
# 循环语句 for while
# while语句的循环
'''
while 条件表达式：T or F
  循环体
  '''
lhage = 23
while True:
    age = input('请猜一下他的年龄：')
    if age == 'q' or age == 'Q':
        print('你要才数字')
        break
    elif age.isdigit():#.isdigit为字符串方法 如果字符串全部由数字组成返回True 反之F
        if int(age) > lhage:
            print('你说的太老了！')
            continue
        elif int(age) == lhage:
            print('恭喜你！猜对了!')
            break
        elif int(age) < lhage:
            print('n你猜的太年轻了')
            continue
    else:
        print('你是真的傻瓜')
# for语句
list1 =[1,2,3,4,5,9,87]
str1='heoll world'
for i in list1:
    print(i,end='')
for j in str1:
    print(j,end='')
# for i in range(开始，结束，部长)
x1=[x**3 for x in range(10)]
print(x1)