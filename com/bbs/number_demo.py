"""
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j

Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
"""

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
#  isinstance 来判断变量属于某个类型
# isinstance()会认为子类是一种父类类型
print(isinstance(a, int))
# type()不会认为子类是一种父类类型
print(type(a) == int)


# 定义class A
class A:
    pass


# 定义class B 继承A
class B(A):
    pass


print(type(B()) == A)
print(type(B()) == B)
print(isinstance(B(), A))

# issubclass 判断子类
print("bool是int的子类", issubclass(bool, int))
print("True ==1", True == 1)
print("false ==0", False == 0)
print("false+1=", False + 1)
print("tue+1=", True + 1)

'''
Math :
'''
import math
import random

print("test math,random")
print(math.cos(0.5) ** 2 + math.sin(0.5) ** 2)
print(math.fabs(-5.0))
print(math.pi)
print(math.e)

print(random.random())
print(random.uniform(1, 10))
