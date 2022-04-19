"""
字符串(String)
Python 中单引号 ' 和双引号 " 使用完全相同。
使用三引号(' ' ' 或 " " ")可以指定一个多行字符串。
转义符 \
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
Python 访问子字符串，可以使用方括号 [] 来截取字符串
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
"""
strs = '123456789'

print(strs)  # 输出字符串
print(strs[0:-1])  # 输出第一个到倒数第二个的所有字符
print(strs[0])  # 输出字符串第一个字符
print(strs[2:5])  # 输出从第三个开始到第五个的字符
print(strs[2:])  # 输出从第三个开始后的所有字符
print(strs[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(strs * 2)  # 输出字符串两次
print(strs + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print("""who are you,
I am cc.
""")
'''
字符串api:
split: 分割字符串 bacada.split(a)=[b,c,d]
join: 链接字符串，a.join([b,c,d])=bacada

'''


# def 定义方法
def reverseWords(inputs):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = inputs.split(" ")
    print("字符串分割api:split-->", inputWords)
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    inputs = 'I like runoob'
    rw = reverseWords(inputs)
    print(rw)

'''
字符串运算符
+	字符串连接	a + b 输出结果： HelloPython
*	重复输出字符串	a*2 输出结果：HelloHello
[]	通过索引获取字符串中字符	a[1] 输出结果 e
[ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True
r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
print( r'\n' )
print( R'\n' )
%	格式字符串	请看下一节内容。
'''


def test_string_operator():
    a = "Hello"
    b = "Python"

    print("a + b 输出结果：", a + b)
    print("a * 2 输出结果：", a * 2)
    print("a[1] 输出结果：", a[1])
    print("a[1:4] 输出结果：", a[1:4])

    if "H" in a:
        print("H 在变量 a 中")
    else:
        print("H 不在变量 a 中")

    if "M" not in a:
        print("M 不在变量 a 中")
    else:
        print("M 在变量 a 中")

    print(r'\n 不进行字符串转义输出')
    print(R'\n 不进行字符串转义输出')
    print('进行字符串转义输出\n')

    print("我叫 %s 今年 %d 岁!" % ('小明', 10))


print("测试字符串运算符：")
test_string_operator()

'''
f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去,
用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d
在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果
'''


def test_string_format():
    name = "邬江涛"
    age = 27
    print("%s 的年龄是 %d" % (name, age))

    print(f'你好 {name}')
    print(f'你的年龄是 {age=}')


print("字符串格式化：")
test_string_format()

'''
字符串内建函数：
str包提供了字符串的常见功能方法函数，可以直接使用处理字符串
'''


def test_str_build_in_func():
    strs = "www.runoob.com"
    sub = 'o'
    print("strs.count('o') : ", strs.count(sub))
    print("strs.count('o',0,8) : ", strs.count(sub, 0, 8))

    print('strs.find', strs.find(sub))
    print('strs.find', strs.find('run', 0, 8))

    print('strs.index', strs.index('run', 0, 8))
    try:
        print('strs.index', strs.index('runs', 0, 8))
    except ValueError as err:
        print(f"strs.index {err}")


print("测试字符串的内建函数")
test_str_build_in_func()
