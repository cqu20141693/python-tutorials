"""
关键字：
if elif else

while
for
else
break
continue

global: 全局关键字
pass: pass是空语句，是为了保持程序结构的完整性。
"""

'''
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
    
global: 引用外部的全局变量
nonlocal:  引用外部的局部变量
'''


def testNonlocal():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


num = 1

def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
    testNonlocal()


fun1()
print(num)

print("--------------")
def testIfElse(age):
    if age <= 0:
        print("你是在逗我吧!")
    elif age == 1:
        print("相当于 14 岁的人。")
    elif age == 2:
        print("相当于 22 岁的人。")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄: ", human)


testIfElse(3)


def testIfNested(num):
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除 2 和 3")
        else:
            print("你输入的数字可以整除 2，但不能整除 3")
    else:
        if num % 3 == 0:
            print("你输入的数字可以整除 3，但不能整除 2")
        else:
            print("你输入的数字不能整除 2 和 3")


testIfNested(6)
testIfNested(3)

'''
while 判断条件(condition)：
    执行语句(statements)

while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
'''

n = 100
sum = 0


def doSum(counter):
    global n, sum  # 使用全局变量
    start = counter
    while counter <= n:
        sum = sum + counter
        counter += 1

    print("%d 到 %d 之和为: %d" % (start, n, sum))


doSum(1)
doSum(50)


def counts(count):
    while count < 5:
        print(count, " 小于 5")
        count = count + 1
    else:
        print(count, " 大于或等于 5")


counts(5)
counts(4)

'''
for <variable> in <sequence>:
    <statements>
else: 只执行一次
    <statements>
    
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行
break:
continue:
'''


def testFor():
    for n in range(2, 10):
        if n % 3 == 0:
            continue
        for x in range(2, n):
            if n % x == 0:
                print(n, '等于', x, '*', n // x)
                break
        else:
            # 循环中没有找到元素
            print(n, ' 是质数')


testFor()

'''
pass是空语句，是为了保持程序结构的完整性。
'''


# 空类
class MyEmptyClass:
    pass


def testPass():
    for letter in 'Runoob':
        if letter == 'o':
            pass
            print('执行 pass 块')
        print('当前字母 :', letter)


testPass()


def testReturn():
    pass
    return


testReturn()
