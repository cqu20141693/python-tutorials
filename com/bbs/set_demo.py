"""
基本功能是进行成员关系测试和删除重复元素。
创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试  in 内置函数
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

# 集合运算
# 差集，a中独有的元素
print(a - b)  # a 和 b 的差集
# 并集 ab中都存在的元素
print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素


# 遍历集合
for e in a:
    print(e)
