# Python中的错误和异常
"""
错误和异常是不相等的
异常是在出现错误时采用的正常控制流以外的动作
异常错的一般流程是： 检测错误，引发异常；对异常进行捕获的操作
try:  # 捕获异常
    <监控异常>  捕获异常的语句
except Exception[,reason]:
   <异常处理代码>
finally:
    <无论异常是否发生都执行>
"""
# i = j    报错 NameError:name 'j' is not defined  意思是j没有被定义
#  print()}  报错 SyntaxError: invalid syntax 语法错误
#  索引超出了范围  报错 IndexError: string index out of range
# 以上是开发者可能会出现的错误
#  用户输入昌盛的错误

'year = int(input(‘请输入一个整数：’))'
'输入abc  报错 valueError: invalid literal for int {} with base 10:\'abc\' '
try:
    year = int(input('请输入一个整数：'))
except ValueError:
    print('年份要输入数字')

'a = 123'
'a.append() AttributeError: int object has no attribute append'
"表示属性错误 整数类型没有这个属性"
# except (ValueError,AttributeError,keyError)  多个错误可以用元组
try:
    print(1 / 'a')
except Exception as e:
    print('%s' % e)

try:
    raise NameError('helloerror')
except NameError:
    print('my custom error')  # 可以输出自己打印的错误
    #  finally 一般使用是用在文件中操作
try:
    a = open('name.txt')
except Exception as e:
    print(e)

finally:
    a.close()
