# 题目：斐波那契数列。程序分析：斐波那契数列（Fibonacci sequence），
# 又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、55……。在数学上，费波那契数列是以递归的

#  递归函数思想
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
