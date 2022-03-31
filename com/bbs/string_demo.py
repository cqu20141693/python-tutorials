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
