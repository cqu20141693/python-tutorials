#                                                    序列
#  序列的基本操作  in , not in  , + (连接符)  , * 重复输出  [:整数]  切片

#        python中的字符串
# 访问  也就是索引 序列的索引支持非负数，索引为非负整数
#     访问单个字符
s = 'python hello'
print('y' in s)  # 判断y这个字符是否在s这个序列中
print(s[0])  # 访问s中第一个字符p
print(s[-1])  # 访问s中最后一个元素 从-1开始
#    访问范围内的字符
"""
切片 names[start:end:step]
names 表示序列的名称
start 开始索引的位置 默认值为0
end  表示切片结束的位置 默认为胥留德长度
step  表示步长
"""
print(s[1:3])  # 访问s中的2到3位的字符 yt
print(s[:3])  # 访问s中0带3位的字符 pyt
print(s[3:])  # 访问s中4到最后一个
print(s[:])  # 访问s中的所有字符

#       单个字符编码
# python中用ord()函数来返回字符的整数表示 用chr() 函数来把编码转换成相应的字符
s3 = 'a'
print(ord(s3))
print(chr(88))

#       字符串运算符
s1 = 'hello'
s2 = 'python'
print(s1 + s2)  # + 连接符
print(s1 * 2)  # *重复输出
print(s1[2])  # 通过索引来获取字符串中的字符
print(s1[1:3])  # 获取字符串中的一部分
print('h' in s1)  # 字符串中是否包含指定字符
print('h' not in s1)  # 不包含  格式一般为 val in sep 表示val是否在指定序列中
print(R'\r')  # 字符串原样输出
print('ab'.format(('hello', 'python')))

#            内置函数
# 还有一个sum（） 求和函数
print(len(s))  # 计算序列的长度
print(max(s))  # 找出序列中最大的元素
print(min(s))  # 找出序列中最小的元素
print(list(s))  # 将序列转化为流标输出
print(str(s))  # 将序列转化为字符串
print(sorted(s))  # 将序列进行排序 一般是从小到大
print(enumerate(s))  # 将序列组合成为一个索引序列 多用在for循环中

#         列表
# 列表（list） 列表可以储存任何类型的数据 ， 同一个列表中的数据类型可以不同
# 列表也是序列结构  可以进行序列的基本操作 索引，切片，加，乘，检查成员
# 创建  相邻之间的元素用逗号隔开
q = [1024, 2.5, 'python']
# 第二种操作 q = list()
# 对列表进行操作  对象名.(这里的.相当于访问符)方法（）
q[1] = 1025  # 修改列表中的第二个元素
print(q)
q.append('hello')  # 向列表中增添新的元素 且只有一个且在末尾
print(q)
q.insert(1, 'wuxin')  # 表示在指定的位置增添对象  索引，元素
print(q)
del q[2]  # 删除指定索引列表中的元素
print(q)
print(q.pop(1))  # 指定下标删除的元素，并且返回删除的下标值
#  count 用来统计一个列表中元素出现的次数
#  index  用来查找摸个元素在列表做那个首次出现的位置（索引）
q.remove(1024)
print(q)
#  remove 移除列表中某个值的首次匹配项
#  sort  对列表中的元素进行排序 一般是按着 ascll码
# copy  复制列表  对象名 = 对象名.copy（）
s5 = [1, 2, 3, 4, 5, 'q', 'e']
s6 = s5
del s5[4]
print(s5, s6)  # 可以发现s6跟着s5发生了改变
#  使用切片的方法
s8 = ['w', 1, 2, 6, 7, 8]
s9 = s8[:]
del s8[2]
print(s8, s9)  # 可以看到s9中的元素并没有收到影响
#  还可以是用 copy

#                                         元组
# 元组与列表类似 凡是元组是不可变的 可简单的看做不可变列表  所以元组经常被用于保存不可修改的内容
#  创建和使用  列表是中括号 元组是小括号
t = (1024, 5, 'p', 'Python', 'w')
# 元组的访问和列表相似
#  元组中的元素是不可以修改的 需要重新赋值的方法操作
# 元组不能被删除 只能删除整个元组
t1 = ('w', 'q', '23', '4')
print(max(t1))  # 必须是同一类型
#  常用方法有 len()  max()  min()  tuple() 表示将莫种类转化为元组

# 二维数组  三维数组等可以以此来推导
# 题目请用索引去除下面指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
# 表示L列表中第一个元素也是一个列表 中的第一个元素 输出Apple
