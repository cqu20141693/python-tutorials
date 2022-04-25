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

# 删除增加的money实例变量
del pig.money


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
# 使用lambda表达式为clanguage对象的bar方法赋值（动态绑定方法）
pig.bar = lambda self: print('--lambda表达式--', self)
pig.bar(pig)  # ②


#  使用函数、lambda 表达式为 clanguage 对象动态增加了方法，但对于动态增加的方法，
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


