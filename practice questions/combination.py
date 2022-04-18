#   题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
分析：首先把这是个数字定义 ， 其次它们的不重复组合 1,2,3   1,2,4   1,3,4  2,3,4 四种
用三个循环结构表示出所有的三位数 然后用个if条件去掉相等的值 重复的值
"""
sum = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                sum = sum + 1
                print(i*100+j*10+k)
                print(sum)
