"""
 bytes 类型用来表示一个字节串
字节串（bytes）和字符串（string）的对比：
字符串由若干个字符组成，以字符为单位进行操作；字节串由若干个字节组成，以字节为单位进行操作。
字节串和字符串除了操作的数据单元不同之外，它们支持的所有方法都基本相同。
字节串和字符串都是不可变序列，不能随意增加和删除数据。

具有和字符串一样的api： 取值，切片...
"""

'''
字符串和 bytes 存在着千丝万缕的联系，我们可以通过字符串来创建 bytes 对象，
或者说将字符串转换成 bytes 对象。有以下三种方法可以达到这个目的：
如果字符串的内容都是 ASCII 字符，那么直接在字符串前面添加b前缀就可以转换成 bytes。
bytes 是一个类，调用它的构造方法，也就是 bytes()，可以将字符串按照指定的字符集转换成 bytes；
如果不指定字符集，那么默认采用 UTF-8。字符串本身有一个 encode() 方法，
该方法专门用来将字符串按照指定的字符集转换成对应的字节串；如果不指定字符集，那么默认采用 UTF-8。
'''


def testBytes():
    # 通过构造函数创建空 bytes
    b1 = bytes()
    print(b1)
    # 通过空字符串创建空 bytes
    b2 = b''
    print(b2)
    # 通过b前缀将字符串转换成 bytes
    b3 = b'http://c.biancheng.net/python/'
    print("b3: ", b3)
    print(b3[3])
    print(b3[7:22])
    strs = 'C语言中文网8岁了'
    b4 = bytes(strs, encoding='UTF-8')
    print("b4: ", b4)
    print("b4[3]: ", b4[3])
    # 通过 encode() 方法将字符串转换成 bytes
    b5 = "C语言中文网8岁了".encode('UTF-8')
    print("b5: ", b5)
    s = b4.decode('UTF-8')
    print("decode:", s)


testBytes()
