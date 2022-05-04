"""
 函数定义：
def 函数名（参数列表）:
    函数体
定义函数时，需要确定函数名和参数个数；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None。
函数可以同时返回多个值，但其实就是一个tuple。

Python 3 提供了一个新的特性：函数注解,可以指定函数的参数类型和返回值

def 函数名(参数名：参数类型,...) -> 返回值类型
    函数体
    return 返回值
python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。
如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

参数：
必需参数
关键字参数
默认参数
不定长参数

python可以有默认参数，使用=号进行赋值，必选参数在前，默认参数在后
在Python函数中，还可以定义可变参数。在参数前面加了一个*号，调用该函数时，可以传入任意个参数，包括0个参数
参数类型在函数内为tuple类型，区分直接将tuple作为参数只能传tuple类型实参且一个
python允许把list或tuple的元素变成可变参数传进去，list或tuple前面加一个*号

关键字参数：关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict，利用**定义关键字参数
命名关键字参数: 可以限制和校验关键字参数的名字：需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
允许将dict传入关键字参数，使用**dict

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

递归函数：函数内部调用自身

高阶函数：变量可以指向函数，将函数作为函数的参数

关键字lambda表示匿名函数，冒号前面的x表示函数参数。匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
"""
from functools import reduce, partial

'''
指定参数类型和返回值
'''


def add(x: int, y: int) -> int:
    return x + y


print("add", add(21, 12))


def convertTuple(x: int, y: int) -> tuple[int, int]:
    return x, y


def convertList(x: int, y: int) -> list[int]:
    return [x, y]


print("add", add(21, 12))
print("convertTuple", convertTuple(21, 12))
print("convertList", convertList(21, 12))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll("cc", "F")


def calc(*numbers):
    print("可变参数类型:", type(numbers))
    sums = 0
    for n in numbers:
        sums = sums + n * n
    return sums


print(calc(1, 2, 3))
nums = [1, 2, 3]
print(calc(*nums))
tuples = (1, 2, 3)
print(calc(*tuples))


def person(name, age, **kw):
    print("关键字参数：", type(kw))
    print('name:', name, 'age:', age, 'other:', kw)


person('Adam', 45, gender='M', job='Engineer')

'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
'''
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

'''
命名关键字+默认参数
'''


def Person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


Person('Jack', 24, job='Engineer')
Person('cc', 27, city="chongqing", job='Engineer')

'''
递归函数:
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。可以使用记录表+动态规划
阶乘： fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n
'''


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(2))
print(fact(3))
print(fact(5))

'''
Python内建了map()和reduce()函数。
map： 接受一个函数f，将一个值映射转换为另外的一个值，再接受一个iterator,循环将iterator值作用到f生成新序列
reduce: 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''


def power(x: int) -> int:
    return x * x


# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list
maps = map(power, [1, 2, 3])
print("map:power", list(maps))


def add(x: int, y: int) -> int:
    return x + y


# 相当于先执行1+3=4，再执行4+5 ... 16+9=25
print("reduce:add->", reduce(add, [1, 3, 5, 7, 9]))
# lambda 匿名函数实现add
print("reduce:add->", reduce(lambda x, y: x + y, [1, 3, 5, 7, 9]))

'''
偏函数
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''
int2 = partial(int, base=2)
print("int(str,base=2)", int2('1000000'))
