# 数据类型转换
"""
函数	描述
int(x [,base])

将x转换为一个整数

float(x)

将x转换到一个浮点数

complex(real [,imag])

创建一个复数

str(x)

将对象 x 转换为字符串

repr(x)

将对象 x 转换为表达式字符串

eval(str)

用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)

将序列 s 转换为一个元组

list(s)

将序列 s 转换为一个列表

set(s)

转换为可变集合

dict(d)

创建一个字典。d 必须是一个 (key, value)元组序列。

frozenset(s)

转换为不可变集合

chr(x)

将一个整数转换为一个字符

ord(x)

将一个字符转换为它的整数值

hex(x)

将一个整数转换为一个十六进制字符串

oct(x)

将一个整数转换为一个八进制字符串

"""
import string

# 隐式转换， 低精度转化为高精度
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

inta: int = 1
floatB: float = 1.0
boolC: bool = 1
s: string = "1"

# 显示转换，利用转换方法
# 字符串转int

strInt = int(s, 10)
print(strInt)
print(str(inta))
print(str(floatB))

# repr 将对象 x 转换为表达式字符串
print("repr:")
s = "物品\t单价\t数量\n包子\t1\t2"
print(s)
print(repr(s))

print("eval func:")
n = 81
print(eval("n + 4"))


def tupleConvert():
    print("tuple( iterable ):")
    lists = ['Google', 'Taobao', 'Runoob', 'Baidu']
    print(tuple(lists))
    strs = 'www'
    print(tuple(strs))
    # 字段转换时只保留键
    maps = {'www': 123, 'aaa': 234}
    print(tuple(maps))
    sets = set('abcd')
    print(tuple(sets))


tupleConvert()

'''
list()方法语法：
list( seq )
'''
print("list(seq): ")
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print("列表元素 : ", list1)

strs = "Hello World"
list2 = list(strs)
print("列表元素 : ", list2)
lists = ["hello", 1, 2, "world"]
list3 = list(lists)
print("列表元素:", list3)

'''
set 语法：
class set([iterable])

'''
print("set()")
sets = set("hello")
print("set:", sets)

'''
dict 语法：

class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
**kwargs -- 关键字。
mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
iterable -- 可迭代对象。
'''
print("dict: ")
numbers = {'x': 5, 'y': 0}
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =', numbers1)
# zip() 创建可迭代对象
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =', numbers3)

'''
hex 语法：

hex(x) int 转hex
'''
print("hex():")
print(hex(255))
print(hex(True))
