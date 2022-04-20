"""
oop:面向对象编程 object oriented programming

类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""
'''
class ClassName:
    <statement-1>
        ...
    <statement-N>
类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
类的方法与普通的函数只有一个特别的区别——类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
'''


class Animal:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def barking(self):
        print(f"it's a {self.name},{self.description}")

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Animal("dog", "wang wang wang")
print(dog.name)
dog.barking()

dog = Dog("dog", "wang wang wang")
dog.run()

cat = Cat("cat", "miao miao miao")
cat.run()
'''
继承
Python 同样支持类的继承
class DerivedClassName(BaseClassName):
    <statement-1>
    ...
    <statement-N>
'''


# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    # 学生私有成员变量，年级
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        # People.__init__(self, n, a, w)
        super(Student, self).__init__(n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


people = People("邬江涛", 27, 148)
people.speak()

s = Student('张三', 10, 60, 3)
s.speak()
# 用子类对象调用父类已被覆盖的方法
super(Student, s).speak()
'''
多继承
Python同样有限的支持多继承形式。多继承的类定义形如下例:
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
        ...
    <statement-N>
    super() 函数是用于调用父类(超类)的一个方法。

super() 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
'''


# 另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承 黄种人
class Asian(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Asian("Tim", 25, 80, 4, "Python")
# 方法名同，默认调用的是在括号中参数位置排前父类的方法
test.speak()

'''
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
在类内部的方法中使用时 self.__private_attrs。
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，
不能在类的外部调用。self.__private_methods。
'''


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    @staticmethod
    def __foo():  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
print(f"Site 公共属性{x.name=}")
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错

'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
