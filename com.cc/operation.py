#                                    python中的运算符
# 0b是二进制 0o是八进制  0x是十六进制
# type() 是查询对象的数据类型
a = 5
b = 2
c = 3
print(a + b)  # 7=5+2
print(a - b)  # 3
print(a * b)  # 10
print(a / b)  # 2.5
print(a % b)  # 取余运算1
print(a ** b)  # 5的2次方2225
print(a // b)  # 整除取整数部分2
# 比较运算符 返回一个逻辑对象（F 或 T）
print(a == b)  # 错F
print(a != b)  # T
print(a > b)  # T
print(a < b)  # F
print(a >= b)  # T
print(a <= b)  # F
a = c  # 赋值运算
print(a)  # 3
a += b  # a=a+b
print(a)  # 5
a -= b  # a=a-b
print(a)  # 3
a *= b  # a=a*b
print(a)  # 6
a /= b  # a=a/b
print(a)  # 3.0
a %= b  # a=a%b
print(a)  # 1.0
# 位运算符
a = 13  # 1101
b = 6  # 0110
print(a & b)  # 1&1为1其余为0  4
print(a | b)  # 0|0为0 其余为1 15
print(a ^ b)  # 同为0不同为1  11
print(~a)  # 取反运算  取胆加一  -1110
print(a << 3)  # 1101000
print(a >> 1)  # 110
# 逻辑运算符
a = True
b = False
print(a and b)  # 同为T为T
print(a or b)  # 同为F为F
print(not b)  # 为T
print(a is b)  # a和b是同一种类型的对象
print(a is not b)  #
