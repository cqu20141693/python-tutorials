"""
Python本身就内置了很多非常有用的模块，提供了常用的功能更，只要安装完毕，这些模块就可以立刻使用。

作用域
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

import 语句 : 导入其他python 文件
import module1[, module2[,... moduleN]
from 语句让你从模块中导入一个指定的部分到当前命名空间中，
from modname import name1[, name2[, ... nameN]]
把一个模块的所有内容全都导入到当前的命名空间也是可行的
from modname import *

"""
# 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
import sys

# 自定义模块引用
from com.bbs.common import twoSum
from com.bbs.system import testOS

' a test module '

__author__ = 'Michael Liao'


def testCommon():
    """ 测试common包
    :return:
    """
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def testOSFunc():
    """
    测试操作系统接口
    :return:
    """
    testOS()


'''
Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
'''
if __name__ == '__main__':
    testCommon()
    print("twoSum:", twoSum([2, 5, 6, 7, 11], 9))
    testOSFunc()
