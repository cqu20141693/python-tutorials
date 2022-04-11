"""
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下：
变量[头下标:尾下标]
"""
# list 可以是任何类型的嵌套
lists = ['abcd', 786, 2.23, 'runoob', 70.2]
tinyList = [123, 'runoob']

print(lists)  # 输出完整列表
print(lists[0])  # 输出列表第一个元素
print(lists[1:3])  # 从第二个开始输出到第三个元素
print(lists[2:])  # 输出从第三个元素开始的所有元素
print(tinyList * 2)  # * 输出两次列表
print(lists + tinyList)  # + 连接列表


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
