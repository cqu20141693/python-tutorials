# python中函数的定义和常用操作
#  函数是对程序逻辑结构化的一种编程方法
"""
函数的定义
def 函数名称():
    代码
    return 需要返回的内容

函数的调用

  函数名称()
"""


#    列子
def func():
    print(open('name1.txt').read())


func()


def func(filename):
    print(open(filename).read())


func('name1.txt')  # 首先执行的是 func('name1.txt')
