# python中函数的定义和常用操作
#  函数是对程序逻辑结构化的一种编程方法

# 函数本质就是一段有特定功能，可以重复使用的代码，这段代码已经被提前编写好了，
# 并且去了一个好听的’名字‘ 后续编程中如果有程序需要同样功能时，直接通过起来的名字代用这段函数

"""
函数的定义
def 函数名称():
    代码
    return 需要返回的内容

函数的调用

  函数名称()
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
