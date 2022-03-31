# 多行注释可以用多个 # 号，还有 ''' 和 """
"""

标识符
 第一个字符必须是字母表中字母或下划线 _ 。
 标识符的其他的部分由字母、数字和下划线组成。
 标识符对大小写敏感

"""

# 变量与赋值，= 左边为变量，= 为赋值符号，= 右边为赋值数据
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

# 多变量赋值
a = b = c = 1
print(a, b, c)
a, b, c = 1, 2, "runoob"
print(a, b, c)
