"""
python 内置函数测试

print(self, *args, sep=' ', end='\n', file=None)


"""


def testPrint():
    # Fibonacci series: 斐波纳契数列
    # 两个元素的总和确定了下一个数
    a, b = 0, 1
    while b < 1000:
        print(b, end=',')
        a, b = b, a + b


testPrint()
print()
import common


def testDir():
    print(dir())
    print(dir(common))

testDir()