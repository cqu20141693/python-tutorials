# python中的函数问题
# pythong 中分三种数值类型 整型int 浮点型 float 复数 complex
"""
整形有四种表示进制：
二进制： 由0和1组成 引导符 0b或0B
八进制：由0到7组成 引导符 0o或0O
十进制： 由0到9
十六进制：由0到15组成 引导符0x或0X

浮点型： 由整数部分和小数部分组成

复数： 由虚部和实部组成
"""
# 基本运算
"""
+,-,*,/,//,%,取反, abs() 取绝对值, int() 转化为整数 float() 转化为浮点数
complex(x,y) 一个带有实部为x 虚部为y的复数 y的默认值为0 
div-mod(x,y) 表示(x//y，x%y)
pow(x,y)  表示x的y次幂   x**y  同样
"""
# 数学函数
"""
除了上面的运算 忙完还可以借助数学模块math来是先更多运算
列如： 
import math
math.sqrt()
abs(x)  返回x的绝对值
ceil(x)  返回x的上入整数 如：math.ceil(1.1)返回2
floor(x)  返回x的下舍整数 如：math.floor(1.1)返回1
exp(x)  返回e的x幂
log(x)  返回以e为底x的对数
log10(x)  返回以10为底x的对数
pow(x,y)  返回x的y次幂
sqrt(x)  返回x的平方根
factorial  返回x的阶乘
"""

# 随机函数
"""
在安全领域有时会用到随机函数，random 模块对随机函数的生成提供了支持
引入  import random 
random(x)  随机生成一个0到1的实数
import random
random.random()

uniform(x,y)  随机生成一个x到y范围内的实数
"""
