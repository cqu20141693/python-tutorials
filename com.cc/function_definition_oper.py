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


# 当我们不确定参数的个数时，可以使用不定长参数，在参数名前加 * 进行声明，格式如下所示：
"""
def 函数名(*参数名):
	函数体
"""


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
