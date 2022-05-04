"""
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下：
变量[头下标:尾下标]
"""

'''
list 初始化：[]
list元素获取：[]
list 切片：[:]
list 赋值：[]=   数据项更新
list复制：*
list 连接： +
list 添加： append
list 删除：del

in : 成员判断
for item in list: 
    func
'''


def list_basic_operator():
    global lists
    lists = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinyList = [123, 'runoob']
    print(lists)  # 输出完整列表
    print(lists[0])  # 输出列表第一个元素
    print(lists[1:3])  # 从第二个开始输出到第三个元素
    print(lists[2:])  # 输出从第三个元素开始的所有元素
    list_twice = tinyList * 2
    print(list_twice)  # * 输出两次列表
    list_twice[2] = "123"
    print(list_twice)
    join_list = lists + tinyList
    print(join_list)  # + 连接列表
    nestedList = [lists, tinyList]
    print(nestedList)  # 嵌套列表，列表的元素和列表，列表元素可以是任意类型
    list_twice[2:] = []
    print(list_twice)
    list_twice.append("go")
    list_twice.append("java")
    print(list_twice)
    del list_twice[3]
    print(list_twice)

    # 测试in
    if 'go' in list_twice:
        print("go already exist")
    else:
        print("go not exist")

    if 'java' in list_twice:
        print("java already exist")
    else:
        print("java not exist")
    # list 遍历
    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        if site == "Runoob":
            print("菜鸟教程!")
            break
        print("循环数据 " + site)
    else:
        print("没有循环数据!")
    print("完成循环!")


# list 可以是任何类型的嵌套
list_basic_operator()

'''
列表推导式格式为：[]
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
'''
print("list:[express for var in list if 条件]")
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

names = ["qq", "wechat", 123]
lists = [i for i in names if isinstance(i, str)]
print(lists)

'''
Python包含以下函数:

序号	    函数
1	   len(list) 列表元素个数
2	   max(list)返回列表元素最大值
3	   min(list)返回列表元素最小值
4	   list(seq)将元组转换为列表

Python包含以下方法: list的方法，使用.符号调用

序号	方法
1	list.append(obj)在列表末尾添加新的对象
2	list.count(obj)统计某个元素在列表中出现的次数
3	list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)将对象插入列表
6	list.pop([index=-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)移除列表中某个值的第一个匹配项
8	list.reverse()反向列表中元素
9	list.sort( key=None, reverse=False)对原列表进行排序
10	list.clear()清空列表
11	list.copy()复制列表
'''


def test_method():
    test_list = []
    print("len(list):", len(test_list))
    test_list.append(100)
    print("list.count(100):", test_list.count(100))
    test_list.extend([102, 99])
    print("len(list):", len(test_list))
    print("list.index(99):", test_list.index(99))
    test_list.insert(0, 99)
    print("list.count(99):", test_list.count(99))
    pop = test_list.pop()
    print("list.pop:", pop)
    print("len(list):", len(test_list))


def test_list_func_method():
    test_list = []
    print("len(list):", len(test_list))
    test_list = [1, 2, "3"]
    try:
        print("max(list):", max(test_list))
    except TypeError as err:
        print(f"max occur {err=}")
    test_list[2] = 3
    print("max(list):", max(test_list))
    print("min(list):", min(test_list))

    test_list = list('hello world')
    print("len(list):", len(test_list))
    test_list = list((1, 2, 3))
    print("list:", test_list)
    print("测试list 方法：")
    test_method()


print()
print("测试列表函数和方法")
test_list_func_method()

'''
嵌套列表解析
'''

print("testMatrixTransformation:")


def testMatrixTransformation():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
    print(matrix)
    matrix1 = [[row[i] for row in matrix] for i in range(4)]
    print(matrix1)
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print(transposed)


testMatrixTransformation()
