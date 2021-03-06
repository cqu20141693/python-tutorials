#                    Python中的字典和集合基础
#  字典(dic) 拥有良好的查询速度，dic中的值可以是Python中任意对象，多次对对一个key赋值value，后会覆盖前的value
# 字典的使用
# 字典的内容在{}内，键-值（key-value）之间用：隔开，键值之间用，隔开

# 第一种方法直接赋值
d = {'邬鑫': 90, '梅强': 99, '李昌霖': 250}
# d = dict(邬鑫='90'……)第二种创建
# d = dict([('邬鑫',90),('',),()])
print(d['邬鑫'])  # 通过key进行访问
""" 如果key不在dict中就会报错 为了防止报错 可以先用 in 来看key是否在 d中 格式 对象名 in 字典名
    还可以通过get方法  字典名.get（对象名） 不在会得到一个none
 """
# d = {} 和 d = dict（） 表示空字典
d['李昌霖'] = 520  # 修改字典
print(d)
print(d.pop('李昌霖'))  # 因为李昌霖开挂 所以吧他的成绩删除掉
print(len(d))  # 获取字典长度
print(d.clear())  # 清空列表
del d  # 删除字典d

# 第二种创建字典的方法
#  dictnmae = dict.fromkeys(list,value=None)  list为字典中的键 value为值  不写为空

# 遍历字典

s = dict(邬鑫=18, 无心=20, 小李=19, 小米=17)
for i in s.values():
    print(i)  # 遍历s的值


for i in s.keys():
    print(i)  # 遍历s的键


for i in s.items():
    print(i)  # 便利他的键和值

"""
注意，copy() 方法所遵循的拷贝原理，既有深拷贝，也有浅拷贝。拿拷贝字典 a 为例，
copy() 方法只会对最表层的键值对进行深拷贝，也就是说，
它会再申请一块内存用来存放 {'one': 1, 'two': 2, 'three': []}；
而对于某些列表类型的值来说，此方法对其做的是浅拷贝，也就是说，b 中的 [1,2,3] 的值不是自己独有，而是和 a 共有。
"""

#   copy() 方法
m1 = {'one':1,'two':2,'three':[1,2,3]}
m2 = m1.copy()
print(m2)
#  由于m2已经讲m1拷贝过来了 所有m1现在增添新的键值对不会影响m2
m1['four'] = 100
print(m1)
print(m2)
# 由于m1和m2共享的[1,2,3]（为浅拷贝） 因此移动m1中的元素会影响m2
m1['three'].remove(3)
print(m2)
print(m1)

"""#  和list比较 dict有以下几个特点
查找和插入的速度极快，不会随着key的增加而变慢
需要占用大量的内存，内存浪费多
#  list相反
查找和插入的时间随着元素的增加而增加
占用空间小，浪费内存少
# 牢记一条  dict的key必须是不可变对象
因为dict是根据key来计算value的储存位置  如果每次计算相同的key得到结果不同 dict就会乱套  这种算法叫 哈希算法(Hash)
list 是可变对象 因此不能作为key
"""
#                                      集合 （set）
#  集合是一个无序不重复元素的集。基本功能是关系测试和下厨重复元素
# 集合对象还支持 union 联合，intersection 交，difference 差，symmetric difference 对称差集
'大括号和set()可以用来创建集合 但是创建空集合set()而不是{} 后者是用于创建空字典'
s = {'a', 'b', 'c'}
print(type(s))
# 第二种创建集合 s = set(['a','b','c'])
s1 = {'a', 'a', 'b', 'c', 'c'}
print(s1)  # 自动过滤掉重复的元素
print(len(s1))  # 获得集合的长度
#   增添元素
s.add('d')
print(s)
s.update('e')
print(s)
#  删除元素
s.remove('c')
print(s)
