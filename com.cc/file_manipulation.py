#                                          python 中的文件操作问题
"""
open() 打开文件
read() 输入
readline()  输入一行
seek() 文件内 移动
write () 输出
close ()  关闭文件
"""
# 将小说的主要人物记录文件中
file1 = open('name.txt', 'w')
file1.write('qweeqw')
file1.close()
#  写入一个文件流程 open--write--close    读出一个文件 write（read）
file2 = open('name.txt')
print(file2.read())
file2.close()

file3 = open('name.txt', 'a')  # a表示在末尾加上
file3.write('wuxin')
file3.close()

file4 = open('name.txt')
print(file4.readline())

file5 = open('name.txt')
for i in file5.readline():
    print(i)
    print('===')  # 循环

file6 = open('name.txt')
print(file6.tell())  # 告诉我们指针的位置
file6.read(2)  # 读出的位置
print(file6.tell())  # 读取指针的位置为2
file6.seek(0)  # seek 有两个值  第一个参数代表偏移的位置  0 表示重头开始  1表示重当前位置开始 2表示冲末尾开始
print(file6.tell())
file6.seek(3)
print(file6.tell())
print(file6.read(3))
"""
r 读取 （默认） 
w 写入， 并先截断文件
x  排他性创建，如果文件已存在失败
a 写入， 如果文件存在则在末尾追加
b 二进制模式
t 文本模式（默认）
+  更新磁盘文件 （读取并写入）
"""
"""
buffering : 是个可选的整数 用于设置缓冲策略
encoding ： 用于解码或者编码文件的名称
errors ： 是一个可选的字符串，用于指定如何处理编码和解码错误（不能在二进制模式下使用）
newline ： 区分换行符
closefd ：如果 closed 为 False 并且给出了文件描述符而不是文件名，那么当文件关闭时，
底层文件描述符将保持打开状态；如果给出文件名，closed 为 True （默认值），否则将引发错误。
opener : 可以通过传递可调用的 opener 来使用自定义开启器。
"""