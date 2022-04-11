"""
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""

dict1 = {}
print(dict1)
# 字典键赋值
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"
# 字典初始化并赋值
tinyDict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict1['one'])  # 输出键为 'one' 的值
print(dict1[2])  # 输出键为 2 的值
print(tinyDict)  # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values())  # 输出所有值

# dict 内置函数
map1 = dict([("Runoob", 1), ("Google", 2)])
print(map1)
# 字典遍历
for k in tinyDict.keys():
    print("{}:{}".format(k, tinyDict[k]))
for k, v in tinyDict.items():
    print("{}:{}".format(k, v))
