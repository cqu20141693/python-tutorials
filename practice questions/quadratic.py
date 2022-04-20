#  请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解

import math


def quadratic(a, b, c):
    if b ** 2 - 4 * a * c < 0:
        print('方程无解')
    elif b ** 2 - 4 * a * c == 0:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = x1
        print(x1)
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print('x1=', x1)
        print('x2=', x2)


#  测试
quadratic(4, 4, 1)

quadratic(4, 2, 1)

quadratic(5, 9, 4)
