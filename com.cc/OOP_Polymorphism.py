#              python __slots__ 限制类实例动态增加属性和方法
"""
Python 是否也允许动态地为类或实例对象添加方法呢？答案是肯定的。我们知道，类方法又可细分为实例方法、静态方法和类方法，
Python 语言允许为类动态地添加这 3 种方法；但对于实例对象，则只允许动态地添加实例方法，不能添加类方法和静态方法。
为单个实例对象添加方法，不会影响该类的其它实例对象；而如果为类动态地添加方法，则所有的实例对象都可以使用。
"""


class CLanguage:
    pass


# 下面定义个实例方法
def info(self):
    print('正在调用实例方法')


# 下面定义一个类方法
@classmethod
def info2(cls):
    print('正在调用类方法')


# 下面定义一个静态方法:
@staticmethod
def info3():
    print('正在调用静态方法')


# 类可以动态的添加以上3中方法，会影响所有的实例对象

CLanguage.info = info
CLanguage.info2 = info2
CLanguage.info3 = info3
clang = CLanguage()
# 以上clang有了以上三种方法
clang.info()
clang.info2()
clang.info3()

# 类实例对象只能动态的添加实例方法，不会影响其他实例对象
clang1 = CLanguage()
clang1.info = info
clang1.info(clang1)

"""
显然，动态给类或者实例对象添加属性或方法，是非常灵活的。但与此同时，如果胡乱地使用，也会给程序带来一定的隐患，
即程序中已经定义好的类，如果不做任何限制，是可以做动态的修改的。

庆幸的是，Python 提供了 __slots__ 属性，通过它可以避免用户频繁的给实例对象动态地添加属性或方法。
再次声明，__slots__ 只能限制为实例对象动态添加属性和方法，而无法限制动态地为类添加属性和方法。

__slots__ 属性值其实就是一个元组，只有其中指定的元素，才可以作为动态添加的属性或者方法的名称。
"""


class Pig:
    __slots__ = ('name', 'add', 'info')


def info(self, name):
    print("正在调用实例方法", self.name)


pig = Pig()
pig.name = '小猪猪'
pig.info = info
pig.info(pig, pig.name)

#                         python type()函数： 动态创建类
"""
type() 函数属于 Python 内置函数，通常用来查看某个变量的具体类型。其实，type() 函数还有一个更高级的用法，
即创建一个自定义类型（也就是创建一个类）。

type() 函数的语法格式有 2 种，分别如下：
type(obj) 
type(name, bases, dict)

以上这 2 种语法格式，各参数的含义及功能分别是：
第一种语法格式用来查看某个变量（类对象）的具体类型，obj 表示某个变量或者类对象。
第二种语法格式用来创建类，其中 name 表示类的名称；bases 表示一个元组，其中存储的是该类的父类；dict 表示一个字典，用于表示类内定义的属性或者方法。
"""
# 查看3.14的类型
print(type(3.14))


# 查看类对象的类型
class zhu:
    pass


z = zhu()
print(type(z))


#  定义一个实例方法
def say(self):
    print('我要学Python')


Mouse = type('Mouse', (object,), dict(say=say, name='喜欢吃大米'))
mouse = Mouse()
mouse.say()
print(mouse.name)

"""
，Python 元组语法规定，当 (object,) 元组中只有一个元素时，最后的逗号（,）不能省略。

可以看到，此程序中通过 type() 创建了类，其类名为 CLanguage，继承自 objects 类，且该类中还包含一个 say() 方法和一个 name 属性。
有读者可能会问，如何判断 dict 字典中添加的是方法还是属性？很简单，如果该键值对中，值为普通变量（如 "喜欢吃大米），
则表示为类添加了一个类属性；反之，如果值为外部定义的函数（如 say() ），则表示为类添加了一个实例方法。

可以看到，使用 type() 函数创建的类，和直接使用 class 定义的类并无差别。事实上，
我们在使用 class 定义类时，Python 解释器底层依然是用 type() 来创建这个类。
"""

#                                               python MateClass 元类详解

"""
如果在创建类时，想用 MetaClass 元类动态地修改内部的属性或者方法，则类的创建过程将变得复杂：
先创建 MetaClass 元类，然后用元类去创建类，最后使用该类的实例化对象实现功能。

和前面章节创建的类不同，如果想把一个类设计成 MetaClass 元类，其必须符合以下条件：
必须显式继承自 type 类；
类中需要定义并实现 __new__() 方法，该方法一定要返回该类的一个实例对象，因为在使用元类创建类时，
该 __new__() 方法会自动被执行，用来修改新建的类。
"""


# 定义一个元类
class FirstMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        attrs['name'] = '珠儿会跑'
        attrs['say'] = lambda self: print(' 正在调用say（）实例方法')

        return super().__new__(cls, name, bases, attrs)


class Test(object, metaclass=FirstMetaClass):
    pass


test = Test()
print(test.name)
test.say()

"""
可以看到，在创建类时，通过在标注父类的同时指定元类（格式为metaclass=元类名），则当 Python 解释器在创建这该类时，
FirstMetaClass 元类中的 __new__ 方法就会被调用，从而实现动态修改类属性或者类方法的目的。

显然，FirstMetaClass 元类的 __new__() 方法动态地为 Clanguage 类添加了 name 属性和 say() 方法，
因此，即便该类在定义时是空类，它也依然有 name 属性和 say() 方法。


对于 MetaClass 元类，它多用于创建 API，因此我们几乎不会使用到它。
"""

#  什么是多态 python多态及用法详解
"""
可以看到，a 可以被先后赋值为 CLanguage 类和 CPython 类的对象，但这并不是多态。类的多态特性，还要满足以下 2 个前提条件：
1. 继承：多态一定是发生在子类和父类之间；
2. 重写：子类重写了父类的方法。
"""


class Dog:
    def say(self):
        print('调用的是dog类的say方法')


class Chicken(Dog):  # 继承 并重写say方法
    def say(self):
        print('调用的是Chicken类的say方法')


class Rabbit(Dog):
    def say(self):
        print('调用的是Rabbit类的say方法')


a = Dog()
a.say()

a = Chicken()
a.say()

a = Rabbit()
a.say()


# 可以看到，CPython 和 CLinux 都继承自 CLanguage 类，且各自都重写了父类的 say() 方法。
# 从运行结果可以看出，同一变量 a 在执行同一个 say() 方法时，由于 a 实际表示不同的类实例对象，
# 因此 a.say() 调用的并不是同一个类中的 say() 方法，这就是多态。


class WhySay:
    def say(self, who):
        who.say()


class Du:
    def say(self):
        print('调用的是Du类的say方法')


class CPython(Du):
    def say(self):
        print('调用CPython类的say方法')


class CL(Du):
    def say(self):
        print('调用的是CL类的say方法')


a = WhySay()
# 调用Du类的say方法
a.say(Du())
# 调用 CPython类的say方法
a.say(CPython())
# 调用 CL 类的方法
a.say(CL())
