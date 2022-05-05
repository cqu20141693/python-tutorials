#                             python的类和对象
"""
类(Class):    用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：   类中定义的函数。
类变量：   类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：   类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：   如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：   定义在方法中的变量，只作用于当前实例的类。
实例变量：   在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：   即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：   创建一个类的实例，类的具体对象。
对象：   通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""


#                             python class:定义类
#  Python中定义一个类使用 class 关键字实现
class TheFirstDemo:
    """这是学习Python的定义的第一个类"""
    add = 'python教程 '  # 定义一个类属性

    def say(self, content):
        # 下面定义一个say方法
        print(content)


#                    Python中__init__()类构造法
"""
在创建类时，我们可以手动添加一个 __init__() 方法，该方法是一个特殊的类实例方法，称为构造方法（或构造函数）。

构造方法用于创建对象时使用，每当创建一个类的实例对象时，Python 解释器都会自动调用它。Python 类中，手动添加构造方法的语法格式如下：

def __init__(self,...):
    代码块
    
init__() 方法可以包含多个参数，但必须包含一个名为 self 的参数，且必须作为第一个参数。也就是说类的构造方法最少也要有一个 self 参数   
"""


class myclass:

    #  构造方法
    def __init__(self):
        print('调用构造方法')

    #  下面定义一个类属性 也就是类变量
    add = 'Python教程'

    # 定义一个say方法
    def say(self, content):
        print(content)


class Clanguage:
    def __init__(self, name, add):
        print(name, '长高了', add)
        # 创建add对象，并传递参数给构造函数


add = Clanguage('tom', '5cm')


#                   python中类对象的创建和使用
# Python类的实例化

class Pig:
    hari = 'black'
    high = 170  # 定义两个类变量

    def __init__(self, high, hari):
        self.higth = high
        self.hari = hari
        print(high, '的身高', hari, '的头发')

    def say(self, content):
        print(content)


pig = Pig(170, 'black')
#     类对象访问变量或方法   类对象名.变量名       对象名.方法名（参数）

# 输出higth和hari的变量的值

print(pig.hari, pig.higth)
#  修改实例变量的值
pig.higth = 173
pig.hari = 'yellow'
# 调用Pig中的say()方法
pig.say('人生苦短，我用Python')
print(pig.hari, pig.higth)

#                       Python self 用法详解
"""
事实上，Python 只是规定，无论是构造方法还是实例方法，最少要包含一个参数，并没有规定该参数的具体名称。
之所以将其命名为 self，只是程序员之间约定俗成的一种习惯，遵守这个约定，
可以使我们编写的代码具有更好的可读性（大家一看到 self，就知道它的作用）。

那么，self 参数的具体作用是什么呢？打个比方，如果把类比作造房子的图纸，那么类实例化后的对象是真正可以住的房子。
根据一张图纸（类），我们可以设计出成千上万的房子（类对象），每个房子长相都是类似的（都有相同的类变量和类方法），
但它们都有各自的主人，那么如何对它们进行区分呢？

当然是通过 self 参数，它就相当于每个房子的门钥匙，可以保证每个房子的主人仅能进入自己的房子（每个类对象只能调用自己的类变量和类方法）。
如果你接触过其他面向对象的编程语言（例如 C++），其实 Python 类方法中的 self 参数就相当于 C++ 中的 this 指针。

也就是说，同一个类可以产生多个对象，当某个对象调用类方法时，该对象会把自身的引用作为第一个参数自动传给该方法，
换句话说，Python 会自动绑定类方法的第一个参数指向调用该方法的对象。如此，Python解释器就能知道到底要操作哪个对象的方法了。
"""


class person:
    def __init__(self):
        print('正在执行构造法')

    # 定义一个study()实例方法
    def study(self):
        print(self, '正在学习Python')


# study() 中的 self 代表该方法的调用者，即谁调用该方法，那么 self 就代表谁。因此，该程序的运行结果为：
zhangsan = person()
zhangsan.study()
list = person()
list.study()


#  对于构造函数中的 self 参数，其代表的是当前正在初始化的类对象。举个例子：

class Person:
    name = "xxx"

    def __init__(self, name):
        self.name = name


zhangsan = Person("zhangsan")
print(zhangsan.name)
lisi = Person("lisi")
print(lisi.name)

#                          """  给类对象动态增添，删除变量"""

#  对已经创建好的对象动摇增加一个money实例变量
#  为pig对象增加一个money是实例变量
pig.money = 480
print(pig.money)
print(vars(pig))

# 删除增加的money实例变量
del pig.money
print(vars(pig))


# 再次尝试输出money，此时会报错  print(pig.money)

#                    给对象动态的增添方法
# 为 pig 对象动态增加的方法，Python 不会自动将调用者自动绑定到第一个参数（即使将第一个参数命名为 self 也没用）
# 先定义一个函数
def info(self):
    print("---info函数---", self)


# 使用info对clanguage的foo方法赋值（动态绑定方法）
pig.foo = info
# Python不会自动将调用者绑定到第一个参数，
# 因此程序需要手动将调用者绑定为第一个参数
pig.foo(pig)  # ①
pig.foo('pig')  # ①
# 使用lambda表达式为clanguage对象的bar方法赋值（动态绑定方法）
pig.single = lambda self: print('--lambda表达式--', self)
pig.two = lambda first, second: first + second
pig.single(pig)  # ②
print(pig.two(1, 2))


#  使用函数、lambda 表达式)为 clanguage 对象动态增加了方法，但对于动态增加的方法，
#  Python 不会自动将方法调用者绑定到它们的第一个参数，因此程序必须手动为第一个参数传入参数值，如上面程序中 ① 号、② 号代码所示。

# 有没有不用手动给 self 传值的方法呢？通过借助 types 模块下的 MethodType 可以实现，仍以上面的 info() 函数为例：
def info(self, content):
    print("C语言中文网地址为：%s" % content)


# 导入MethodType
from types import MethodType

pig.info = MethodType(info, pig)
# 第一个参数已经绑定了，无需传入
pig.info("http://c.biancheng.net")

#                         python 中类变量和实例变量
"""
前面章节提到过，在类体中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下 3 种类型：
类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量；
类体中，所有函数内部：以“变量名=变量值”的方式定义的变量，称为局部变量。
"""


#  通过类名不仅可以修改调用变量也可以修改他的值   也可以用类对象来调用所属类中的类变量（不推荐用）

class zhu:
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"

    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)


print("修改前，各类对象中类变量的值：")
clang1 = zhu()
print(clang1.name)
print(clang1.add)
clang2 = zhu()
print(clang2.name)
print(clang2.add)
print("修改后，各类对象中类变量的值：")
zhu.name = "Python教程"
zhu.add = "http://c.biancheng.net/python"
print(clang1.name)
print(clang1.add)
print(clang2.name)
print(clang2.add)


# 注意，通过类对象是无法修改类变量的。通过类对象对类变量赋值，其本质将不再是修改类变量的值，
# 而是在给该对象定义新的实例变量（在讲实例变量时会进行详细介绍）


#  实例变量 （实例属性）
# 实例变量指的是在任意类方法内部，以“self.变量名”的方式定义的变量，
# 其特点是只作用于调用方法的对象。另外，实例变量只能通过对象名访问，无法通过类名访问。

class other:
    high = 172

    def __init__(self):
        self.name = '邬鑫'
        self.add = '是一个没有自控能力的人'
        # 下面定义一个实例方法

    def say(self):
        self.age = 20


# 由于 __init__() 函数在创建类对象时会自动调用，而 say() 方法需要类对象手动调用。
# 因此，CLanguage 类的类对象都会包含 name 和 add 实例变量，而只有调用了 say() 方法的类对象，才包含 catalog 实例变量。
other1 = other()
print(other1.name)
print(other1.add)
# 由于 other 对象未调用 say() 方法，因此其没有 other 变量，下面这行代码会报错
# print(other1.age)

# #只有调用 say()，才会拥有 catalog 实例变量
other1.say()
print(other1.age)

# 前面讲过，通过类对象可以访问类变量，但无法修改类变量的值。这是因为，通过类对象修改类变量的值，不是在给“类变量赋值”，而是定义新的实例变量。

other1.high = 180
print(other1.high)  # 定义新的实例变量
print(other.high)  # 类变量并没有改变

other.high = 180
print(other1.high)
print(other.high)  # 改变了类变量的值


# 类中，实例变量和类变量可以同名，但这种情况下使用类对象将无法调用类变量，它会首选实例变量，这也是不推荐“类变量使用对象名调用”的原因。

# 另外，和类变量不同，通过某个对象修改实例变量的值，不会影响类的其它实例化对象，更不会影响同名的类变量

class CLanguage:
    name = "xxx"  # 类变量
    add = "http://"  # 类变量

    def __init__(self):
        self.name = "C语言中文网"  # 实例变量
        self.add = "http://c.biancheng.net"  # 实例变量

    # 下面定义了一个say实例方法
    def say(self):
        self.catalog = 13  # 实例变量


clang = CLanguage()
# 修改 clang 对象的实例变量
clang.name = "python教程"
clang.add = "http://c.biancheng.net/python"
print(clang.name)
print(clang.add)
clang2 = CLanguage()
print(clang2.name)
print(clang2.add)
# 输出类变量的值
print(CLanguage.name)
print(CLanguage.add)


#                                  局部变量
# 除了实例变量，类方法中还可以定义局部变量。和前者不同，局部变量直接以“变量名=值”的方式进行定义，例如：
class CLanguage:
    # 下面定义了一个say实例方法
    def count(self, money):
        sale = 0.8 * money
        print("优惠后的价格为：", sale)


clang = CLanguage()
clang.count(100)
# 通常情况下，定义局部变量是为了所在类方法功能的实现。需要注意的一点是，局部变量只能用于所在函数中，函数执行完成后，局部变量也会被销毁。


#                           python 中实例方法，静态方法和类方法详解 （区别和用法）
"""
和类属性的分类不同，对于初学者来说，区分这 3 种类方法是非常简单的，即采用 @classmethod 修饰的方法为类方法；
采用 @staticmethod 修饰的方法为静态方法；不用任何修改的方法为实例方法。
其中 @classmethod 和 @staticmethod 都是函数装饰器。
"""


#     python中的实例方法
class Classmate:
    # 类构造方法 也属于实例方法
    def __init__(self):
        self.name = '吴江'
        self.hihg = 170

        # 定义一个say的 实例方法

    def say(self):
        print('正在调用say()实例方法')


# 实例方法最大的特点就是，它最少也要包含一个 self 参数，用于绑定调用此方法的实例对象（Python 会自动完成绑定）。实例方法通常会用类对象直接调用
classmate = Classmate()
classmate.say()

# 当然，Python 也支持使用类名调用实例方法，但此方式需要手动给 self 参数传值
Classmate.say(classmate)


#                                  python类方法

# Python 类方法和实例方法相似，它最少也要包含一个参数，只不过类方法中通常将其命名为 cls，
# Python 会自动将类本身绑定给 cls 参数（注意，绑定的不是类对象）。也就是说，我们在调用类方法时，无需显式为 cls 参数传参。

# 和 self 一样，cls 参数的命名也不是规定的（可以随意命名），只是 Python 程序员约定俗称的习惯而已。

class ui:
    # 类构造方法，也属于实例方法
    def __init__(self):
        self.name = 'UI'
        self.add = 'NB'

        # 定义一个类方法

    @classmethod
    def info(cls):
        print('正在调用类方法', cls)


# 注意，如果没有 ＠classmethod，则 Python 解释器会将 fly() 方法认定为实例方法，而不是类方法。

# 类方法推荐使用类名直接调用，当然也可以使用实例对象来调用（不推荐）。例如，在上面 CLanguage 类的基础上

# 使用类名直接调用类方法
ui.info()
# s使用类对象来调用类方法
ui1 = ui()
ui1.info()

#                       python类 静态方法
"""
静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，
而函数则定义在程序所在的空间（全局命名空间）中。

静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。
也正因为如此，类的静态方法中无法调用任何类属性和类方法。
"""


# 静态方法需要使用＠staticmethod修饰
class pig1:
    @staticmethod
    def info(name, add):
        print(name, add)


# 静态方法的调用，既可以使用类名，也可以使用类对象
pig11 = pig1()
pig11.info('wuxin', 'shigehazi')
pig1.info('zhuer', 'shigezhuerchong')

#  在实际编程中，几乎不会用到类方法和静态方法，因为我们完全可以使用函数代替它们实现想要的功能，
#  但在一些特殊的场景中（例如工厂模式中），使用类方法和静态方法也是很不错的选择。

#  python类调用实例方法
"""
通过前面的学习，类方法大体分为 3 类，分别是类方法、实例方法和静态方法，其中实例方法用的是最多的。
我们知道，实例方法的调用方式其实有 2 种，既可以采用类对象调用，也可以直接通过类名调用。

通常情况下，我们习惯使用类对象调用类中的实例方法。但如果想用类调用实例方法，不能像如下这样：
"""


class CLanguage:
    def info(self):
        print("我正在学 Python")


# 通过类名直接调用实例方法
"""
CLanguage.info()
运行上面代码，程序会报出如下错误：
Traceback (most recent call last):
  File "D:\python3.6\demo.py", line 5, in <module>
    CLanguage.info()
TypeError: info() missing 1 required positional argument: 'self'

其中，最后一行报错信息提示我们，调用 info() 类方式时缺少给 self 参数传参。这意味着，和使用类对象调用实例方法不同，通过类名直接调用实例方法时，Python 并不会自动给 self 参数传值。
读者想想也应该明白，self 参数需要的是方法的实际调用者（是类对象），而这里只提供了类名，当然无法自动传值。
"""


# 因此，如果想通过类名直接调用实例方法，就必须手动为 self 参数传值。例如修改上面的代码为：
class CLanguage:
    def info(self):
        print("我正在学 Python")


clang = CLanguage()
# 通过类名直接调用实例方法
CLanguage.info(clang)


# 可以看到，通过手动将 clang 这个类对象传给了 self 参数，使得程序得以正确执行。实际上，这里调用实例方法的形式完全是等价于 clang.info()。

# 值得一提的是，上面的报错信息只是让我们手动为 self 参数传值，但并没有规定必须传一个该类的对象，其实完全可以任意传入一个参数，例如：
class CLanguage:
    def info(self):
        print(self, "正在学 Python")


# 通过类名直接调用实例方法
CLanguage.info("zhangsan")

# 可以看到，"zhangsan" 这个字符串传给了 info() 方法的 self 参数。显然，
# 无论是 info() 方法中使用 self 参数调用其它类方法，还是使用 self 参数定义新的实例变量，胡乱的给 self 参数传参都将会导致程序运行崩溃。

# 总的来说，Python 中允许使用类名直接调用实例方法，但必须手动为该方法的第一个 self 参数传递参数，这种调用方法的方式被称为“非绑定方法”。
# 用类的实例对象访问类成员的方式称为绑定方法，而用类名调用类成员的方式称为非绑定方法。


#                            浅谈 Python 类命名空间
#  类命名空间   Python 编写的整个程序默认处于全局命名空间内，而类体 则 处于类名空间内


#                           python 中 描述符详解

"""
描述符是 Python 中复杂属性访问的基础，它在内部被用于实现 property、方法、类方法、静态方法和 super 类型。

描述符类基于以下 3 个特殊方法，换句话说，这 3 个方法组成了描述符协议：
__set__(self, obj, type=None)：在设置属性时将调用这一方法（本节后续用 setter 表示）；
__get__(self, obj, value)：在读取属性时将调用这一方法（本节后续用 getter 表示）；
__delete__(self, obj)：对属性调用 del 时将调用这一方法。
其中，实现了 setter 和 getter 方法的描述符类被称为数据描述符；反之，如果只实现了 getter 方法，则称为非数据描述符。
"""
"""
实际上，在每次查找属性时，描述符协议中的方法都由类对象的特殊方法 __getattribute__() 
调用（注意不要和 __getattr__() 弄混）。也就是说，每次使用类对象.属性（或者 getattr(类对象，属性值)）的调用方式时，
都会隐式地调用 __getattribute__()，它会按照下列顺序查找该属性：

验证该属性是否为类实例对象的数据描述符；
如果不是，就查看该属性是否能在类实例对象的 __dict__ 中找到；
最后，查看该属性是否为类实例对象的非数据描述符。

"""


#             描述符类
class revealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("updating", self.name)
        self.val = val


class myClass:
    x = revealAccess(10, 'var "x"')
    y = 5


m = myClass()
print(m.x)
m.x = 20
print(m.x)
print(m.y)
"""
从这个例子可以看到，如果一个类的某个属性有数据描述符，那么每次查找这个属性时，都会调用描述符的 __get__() 方法，并返回它的值；同样，每次在对该属性赋值时，也会调用 __set__() 方法。

注意，虽然上面例子中没有使用 __del__() 方法，但也很容易理解，当每次使用 del 类对象.属性（或者 delattr(类对象，属性)）语句时，都会调用该方法。

除了使用描述符类自定义类属性被调用时做的操作外，还可以使用 property() 函数或者 @property 装饰器
"""



