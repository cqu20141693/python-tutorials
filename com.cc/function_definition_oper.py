# python中函数的定义和常用操作
#  函数是对程序逻辑结构化的一种编程方法

# 函数本质就是一段有特定功能，可以重复使用的代码，这段代码已经被提前编写好了，
# 并且去了一个好听的’名字‘ 后续编程中如果有程序需要同样功能时，直接通过起来的名字代用这段函数

"""
函数的定义
def 函数名称(参数列表):
    //实现特定功能的代码
    [return【 需要返回的内容】】

    A 函数名是一个符合Python语法的标识符  名字最好能够体现函数的功能
    B 参数列表：看呀接受多个参数，多个参数之间用，隔开
    C [return[返回值]] 整体作为可选参数  用于设置函数的返回值  根据具体实际情况来
注意 在创建函数时，即使函数不需要参数，也必须保留一对空的“()”，
    否则 Python 解释器将提示“invaild syntax”错误。
    另外，如果想定义一个没有任何功能的空函数，可以使用 pass 语句作为占位符。

函数的调用

  [返回值]=函数名称([形参值])
"""


#  定义一个空函数
def my_s13():
    pass


#  列子 自定义len（）函数
def my_len(str):
    length = 0
    for c in str:
        length += 1
    return length


# 调用自定义的my_len()函数
length = my_len("wuxinshiyigebaopilong.shagou")
print(length)

#  再次调用 my_len()函数

length1 = my_len('laozishidage///')
print(length1)


#  定义一个比较两个整数大小的函数

def int_max(x, y):
    return x if x > y else y


max1 = int_max(86456, 6455456)
print(max1)
help(int_max)

#            python中函数值传递和引用值传递（包括形式参数和实际参数的区别）

# 形式参数：在定义函数的时候，函数后面括号里面的就是形式参数
# 如上面def int_max(x,y)  xy就是形式参数

# 实际参数：在调用函数时，函数括号后面的为实际参数，也就是调用者给出的参数
# 如上面的int_max(86456, 6455456) 86456, 6455456 为实际参数
'形象比喻：实参和形参的区别，如同剧本中的主角，形参就是角色，实参就是扮演角色的演员'


#  Python中根据参数的类型不同可分为两种方式：值传递和引用（地址）传递
#  1.值传递：适用于实参类型为不可变类型（字符串，数字，元组）
#  2.引用地址传递：适用于参数类型为可变类型（列表，字典）

# 区别： 值传递不会因为形参的改变而改变，引用传递以为传递后形参的改变而改变实参

#  举例
def demo(obj):
    obj += obj
    print('形式参数', obj)


m = 'wuxinshigedabendan!'
print(m)
demo(m)
print('实际参数', m)  # 此时的实参不会受到形参的改变而改变
m1 = [8, 9, 6, 4, 5]
demo(m1)
print('实际参数', m1)  # 此时的实际参数已经跟着形参而改变


#               什么是位置参数，Python位置参数

# 位置参数也称必备参数： 实参和形参的数量和位置必须保持一致
# 例子
def girth(width, height):
    return 2 * (width + height)


print(girth(8, 5))


# 数量和位置都必须一致  少一个 或者多一个都会报错  交换实参位置意义不一样这里的计算虽然不会出错


#                   Python函数关键字参数及用法

def dis_str(str1, str2):
    print("str1:", str1)
    print("str2:", str2)


# 位置参数
dis_str("http://c.biancheng.net/python/", "http://c.biancheng.net/shell/")
# 关键字参数
dis_str("http://c.biancheng.net/python/", str2="http://c.biancheng.net/shell/")
# 使用位置参数和关键字参数混合传参的方式。但需要注意，混合传参时关键字参数必须位于所有的位置参数之后。也就是说，如下代码是错误的：
dis_str(str2="http://c.biancheng.net/python/", str1="http://c.biancheng.net/shell/")


#                Python默认值参数设置

#  语法格式： def 函数名(……，形参名，形参名=默认值):    代码块
#  注意，在使用此格式定义函数时，指定有默认值的形式参数必须在所有没默认值参数的最后，否则会产生语法错误。

# str3没有默认参数，str4有默认参数
def dis_str1(str3, str4="http://c.biancheng.net/python/"):
    #  如果说str4 默认值 放在str3的前面就会报错
    print("str3:", str3)
    print("str4:", str4)


dis_str1("http://c.biancheng.net/shell/")  # 因为str4有默认值参数所以只需要传一个参数
dis_str1("http://c.biancheng.net/java/", "http://c.biancheng.net/golang/")
#  也可以给所有的参数传值，即使str4有默认值，它会优先使用传递给他的新值

#  Python中有些内置函数或者第三方函数有默认值，可以使用“函数名.__defaults__”查看函数的默认值参数的当前值，
#  其返回值是一个元组。以本节中的 dis_str1() 函数为例，在其基础上，执行如下代码：
print(dis_str1.__defaults__)

#    Python函数的不定长参数
# 当我们不确定参数的个数时，可以使用不定长参数，在参数名前加 * 进行声明，格式如下所示：
"""
def 函数名(*参数名):
	函数体
"""

lisr1 = []


def s13(*b):  # 可变长参数  *b 是一个元组  **b是一个字典
    for i in b:
        lisr1.append(i)
    lisr1.sort()
    print(lisr1)


s13(4, 5, 45, 5, 6, 4, 564)


def person(name, age, *, city, job):  # 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)


person('wuxin', 20, city='chongqi', job='xuesheng')  # city和job都是关键字参数不给出关键字会报错


#  函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def chengfa(a, b, *t):
    if t == ():
        c1 = a * b
        return c1
    else:
        for i in t:
            c2 = a * b * i
        return c2


#  测试
print(chengfa(5, 6, 2, 5, 10))

#          Python中None（空值）及用法

# 在Python中有一个特殊的常量None N必须大写 和False不同 他不表示0也不表示空字符串 表示没有值 也就是空值

# 这里的空值不代表空对象，及None和[]，“” 不同
print(None is [])
print(None == "")
# None 有自己的数据类型
print(type(None))


# 如果希望变量中存储的东西不与任何其它值混淆，就可以使用 None。


#            递归函数  在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(5))
"""
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
"""


#  变量作用域（全局变量和局部变量）

# 局部变量（Local Variable） 他的作用只限制于函数内部，除了函数就不能使用了

def demo(name, add):
    print("函数内部 name =", name)
    print("函数内部 add =", add)


demo("Python教程", "http://c.biancheng.net/python/")
#   就就会报错  print("函数外部 name =", name)
#   就会报错   print("函数外部 add =", add)


# 全局变量 除了在函数内部定义变量，Python 还允许在所有函数的外部定义变量，这样的变量称为全局变量（Global Variable）。

add = "http://c.biancheng.net/shell/"


def text():
    print("函数体内访问：", add)


text()
print('函数体外访问：', add)


#    global关键字  可对变量进行修饰  修饰后变量变为全局变量

def text():
    global add
    add = "http://c.biancheng.net/java/"
    print("函数体内访问：", add)


text()
print('函数体外访问：', add)

#         globals() 函数
#  globals() 函数为 Python 的内置函数，它可以返回一个包含全局范围内所有变量的字典，该字典中的每个键值对，键为变量名，值为该变量的值。

# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"


def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd = "http://c.biancheng.net/shell/"


print(globals())  # 可以返回所有全局变量的字典  键 为变量名 值为变量的值

print(globals()['Pyname'])  # 输出 全局变量中 Python 键的值
globals()['Pyname'] = 'Python入门教程'  # 修改全局变量中 Python键的值
print(Pyname)

#     A
#     locals() 函数也是 Python 内置函数之一，通过调用该函数，我们可以得到一个包含当前作用域内所有变量的字典。
#     这里所谓的“当前作用域”指的是，在函数内部调用 locals() 函数，会获得包含所有局部变量的字典；
#     而在全局范文内调用 locals() 函数，其功能和 globals() 函数相同。

# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"


def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd = "http://c.biancheng.net/shell/"
    print("函数内部的 locals:")
    print(locals())


text()
print("函数外部的 locals:")
print(locals())
print(None == text)

# B
# 当使用 locals() 函数获得所有局部变量组成的字典时，可以向 globals() 函数那样，通过指定键访问对应的变量值，但无法对变量值做修改


# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"


def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd = "http://c.biancheng.net/shell/"
    print(locals()['Shename'])
    locals()['Shename'] = "shell入门教程"
    print(Shename)


text()

#  C
#  vars() 函数也是 Python 内置函数，其功能是返回一个指定 object 对象范围内所有变量组成的字典。
#  如果不传入object 参数，vars() 和 locals() 的作用完全相同。
# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"


class Demo:
    name = "Python 教程"
    add = "http://c.biancheng.net/python/"


print("有 object：")
print(vars(Demo))
print("无 object：")
print(vars())


#                 python 中的局部函数及用法

# 首先局部函数和局部变量一样，默认情况下 局部函数只能在奇所在函数的作用域内使用

# 全局函数
def outdef():
    def indef():  # 局部函数
        print('局部函数')
        # 调用局部函数

    return indef  # 返回局部函数名  indef() 叫做函数的调用


# 调用全局函数
new_indef = outdef()
# 调用全局函数中的局部函数
new_indef()


#                    什么是闭包， Python闭包
# 闭包，又称闭包函数或者闭合函数，其实和前面讲的嵌套函数类似，不同之处在于，闭包中外部函数返回的不是一个具体的值，而是一个函数。
# 例子  计算一个数的n次幂

def nth_power(x):
    def nth_power1(y):
        return y ** x

    return nth_power1


new_power = nth_power(2)  # 计算一个数的平方
new_power1 = nth_power(3)  # 计算一个数的立方
print(new_power(4))
print(new_power1(4))

#  python闭包的_closure_属性
# 闭包比普通的函数多了一个 __closure__ 属性，该属性记录着自由变量的地址。
# 当闭包被调用时，系统就会根据该地址找到对应的自由变量，完成整体的函数调用。
print(new_power.__closure__)


#                   python lambda表达式（匿名函数）及用法

# lambda表达式的语法格式：name = lambda[list]:表达式  []为可选参数

# 例子
def add1(x, y):
    return x + y


print(add1(3, 5))

add2 = lambda x, y: x + y
print(add2(2, 9))
