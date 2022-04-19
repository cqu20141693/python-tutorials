# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。
# 元组写在小括号 () 里，元素之间用逗号隔开

tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
# 最小二元组
tinyTuple = (123, 'runoob')
# 变量为一元
singleTuple = 1
print(tuple1)  # 输出完整元组
print(tuple1[0])  # 输出元组的第一个元素
print(tuple1[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple1[2:])  # 输出从第三个元素开始的所有元素
print(tinyTuple * 2)  # 输出两次元组
print(tuple1 + tinyTuple)  # 连接元组

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup1)
print(tup2)

# 遍历Tuple
for t in tinyTuple:
    print(t)

'''
元组推导式基本格式：()
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
'''
print("tuple: func for item in Sequence")
tuples = (item % 5 for item in range(10) if item % 2 == 0)
# 元组推导式返回的结果是一个生成器对象。
print(tuples)
print(tuple(tuples))
