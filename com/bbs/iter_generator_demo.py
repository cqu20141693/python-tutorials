"""
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。



StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
生成器：
使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
"""
import sys


def testIter():
    lists = [1, 2, 3, 4]
    it = iter(lists)
    while True:
        try:
            print(next(it), end=" ")
        except StopIteration:
            break


testIter()

'''
创建一个迭代器
_iter__() 方法返回一个特殊的迭代器对象，
这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
'''


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


# 创建一个迭代器器
myclass = MyNumbers()
# 创建迭代器方法
myiter = iter(myclass)
# next 迭代
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


print()
print("test generator:")
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        # 每次从上次yield 方法处执行
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
