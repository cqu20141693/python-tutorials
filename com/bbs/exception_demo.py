"""
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
assert expression
等价于：
if not expression:
    raise AssertionError
assert 后面也可以紧跟参数:
assert expression [, arguments]
等价于：
if not expression:
    raise AssertionError(arguments)

Python 有两种错误很容易辨认：语法错误和异常。
except (RuntimeError, TypeError, NameError):

异常处理
try/except
异常捕捉可以使用 try/except 语句。

try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。

try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。

抛出异常
Python 使用 raise 语句抛出一个指定的异常。

用户自定义异常
你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承

Python 中的 with 语句用于异常处理，封装了 try…except…finally 编码范式，提高了易用性。
with 语句使代码更清晰、更具可读性， 它简化了文件流等公共资源的管理。
"""


def assertValue(param):
    assert param == 1, ' param !=1'


def testFinally():
    try:
        assertValue(1)
    except AssertionError as error:
        print(error)
    else:
        try:
            with open('file.log') as file:
                file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print('finally: 这句话，无论异常是否发生都会执行。')


def testRaise():
    try:
        raise NameError('HiThere')
    except NameError as err:
        print(f'An exception {err} flew by!')
        # 并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
        raise


def test_exception_catch():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            print(f"您输入的数字：{x}")
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
    testElse("www.baidu.com")
    testElse("www.bbi.com")

    testFinally()
    try:
        testRaise()
    except Exception as err:
        print(f"catch except {err}")


def testElse(website):
    index = -1
    try:
        index = website.index("bb")
    except ValueError as err:
        print(f"index {err}")
    else:
        print(f"{index=}")


print("测试异常捕获")
test_exception_catch()


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def test_custom_except():
    try:
        raise MyError(2 * 2)
    except MyError as e:
        print('My exception occurred, value:', e.value)


print("测试自定义异常")
test_custom_except()


def test_with():
    with open('./test_runoob.txt', 'w') as file:
        file.write('hello world !')
    print(file.closed)


print("测试with 资源自动释放")
test_with()
