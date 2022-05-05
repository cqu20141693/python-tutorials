#  python property()函数： 定义属性


"""
我们一直在用“类对象.属性”的方式访问类中定义的属性，其实这种做法是欠妥的，因为它破坏了类的封装原则。
正常情况下，类包含的属性应该是隐藏的，只允许通过类提供的方法来间接实现对类属性的访问和操作。

因此，在不破坏类封装原则的基础上，为了能够有效操作类中的属性，
类中应包含读（或写）类属性的多个 getter（或 setter）方法，这样就可以通过“类对象.方法(参数)”
"""


class CLanguage:
    # 构造函数
    def __init__(self, name):
        self.name = name

    # 设置name属性值得函数
    def setname(self, name):
        self.name = name

    # 访问name属性值的函数
    def getname(self):
        return self.name

    # 删除name属性值函数
    def delname(self):
        self.name = 'xxx'


clang = CLanguage('猪儿')
print(clang.getname())  # 获取name属性的值
clang.setname('狗儿')  # 设置name属性值
print(clang.getname())
# 删除name属性值
clang.delname()
print(clang.getname())

"""
可能有读者觉得，这种操作类属性的方式比较麻烦，更习惯使用“类对象.属性”这种方式。

庆幸的是，Python 中提供了 property() 函数，可以实现在不破坏类封装原则的前提下，让开发者依旧使用“类对象.属性”的方式操作类中的属性。

property() 函数的基本使用格式如下：
属性名=property(fget=None, fset=None, fdel=None, doc=None)

其中，fget 参数用于指定获取该属性值的类方法，fset 参数用于指定设置该属性值的方法，
fdel 参数用于指定删除该属性值的方法，最后的 doc 是一个文档字符串，用于说明此函数的作用。

注意，在使用 property() 函数时，以上 4 个参数可以仅指定第 1 个、或者前 2 个、或者前 3 个，
当前也可以全部指定。也就是说，property() 函数中参数的指定并不是完全随意的。
"""


class CLanguage:
    # 构造函数
    def __init__(self, n):
        self.__name = n

    # 设置name属性值得函数
    def setname(self, n):
        self.__name = n

    # 访问name属性值的函数
    def getname(self):
        return self.__name

    # 删除name属性值函数
    def delname(self):
        self.__name = 'xxx'

    # 为name属性配置 property()函数
    name = property(getname, setname, delname, '指明出处')


# 调取说明文档的两种方式：
# print(CLanguage.name.__doc__)
help(CLanguage.name)
clang1 = CLanguage('猪儿会跑')
# 调用gatname方法
print(clang1.name)
# 调用setname（）方法
clang1.name = '狗儿更快'
print(clang1.name)
# 调用 delname()方法
del clang1.name
print(clang1.name)

"""
注意，在此程序中，由于 getname() 方法中需要返回 name 属性，如果使用 self.name 的话，其本身又被调用 getname()，
这将会先入无限死循环。为了避免这种情况的出现，程序中的 name 属性必须设置为私有属性，即使用 __name（前面有 2 个下划线）。
有关类属性和类方法的属性设置（分为共有属性、保护属性、私有属性），后续章节会做详细介绍。

当然，property() 函数也可以少传入几个参数。以上面的程序为例，我们可以修改 property() 函数如下所示
name = property(getname, setname)
这意味着，name 是一个可读写的属性，但不能删除，因为 property() 函数中并没有为 name 配置用于函数该属性的方法。
也就是说，即便 CLanguage 类中设计有 delname() 函数，这种情况下也不能用来删除 name 属性。 

同理，还可以像如下这样使用 property() 函数：
name = property(getname)    # name 属性可读，不可写，也不能删除
name = property(getname, setname,delname)    #name属性可读、可写、也可删除，就是没有说明文档
"""

#  python 封装机制以及实现方法

"""
和其它面向对象的编程语言（如 C++、Java）不同，Python 类中的变量和函数，不是公有的（类似 public 属性），
就是私有的（类似 private），这 2 种属性的区别如下：
public：公有属性的类变量和类函数，在类的外部、类内部以及子类（后续讲继承特性时会做详细介绍）中，都可以正常访问；
private：私有属性的类变量和类函数，只能在本类内部使用，类的外部以及子类都无法使用。

但是，Python 并没有提供 public、private 这些修饰符。为了实现类的封装，Python 采取了下面的方法：
默认情况下，Python 类中的变量和方法都是公有（public）的，它们的名称前都没有下划线（_）；
如果类中的变量和函数，其名称以双下划线“__”开头，则该变量（函数）为私有变量（私有函数），其属性等同于 private。

除此之外，还可以定义以单下划线“_”开头的类属性或者类方法（例如 _name、_display(self)），
这种类属性和类方法通常被视为私有属性和私有方法，虽然它们也能通过类对象正常访问，但这是一种约定俗称的用法，初学者一定要遵守。

注意，Python 类中还有以双下划线开头和结尾的类方法（例如类的构造函数__init__(self)），
这些都是 Python 内部定义的，用于 Python 内部调用。我们自己定义类属性或者类方法时，不要使用这种格式。
"""


class CLanguage:
    def setname(self, name):
        if len(name) < 3:
            raise ValueError('名称长度必须大于3！')
        self.__name = name

    def getname(self):
        return self.__name

    # 为name配置setter和getter 方法

    name = property(getname, setname)

    def setadd(self, add):
        if add.startswith("http://"):
            self.__add = add
        else:
            raise ValueError('地址必须以http://开头')

    def getadd(self):
        return self.__add

    # 为add配置 setter 和 getter 方法
    add = property(getadd, setadd)

    #  定义一个私有方法

    def __display(self):
        print(self.__name, self.__add)


clang2 = CLanguage()
clang2.name = '小猪佩奇'
clang2.add = "http://c.biancheng.net"
print(clang2.add)
print(clang2.name)

"""
上面程序中，CLanguage 将 name 和 add 属性都隐藏了起来，但同时也提供了可操作它们的“窗口”，
也就是各自的 setter 和 getter 方法，这些方法都是公有（public）的。

不仅如此，以 add 属性的 setadd() 方法为例，通过在该方法内部添加控制逻辑，即通过调用 startswith() 方法，
控制用户输入的地址必须以“http://”开头，否则程序将会执行 raise 语句抛出 ValueError 异常。
有关 raise 的具体用法，后续章节会做详细的讲解，这里可简单理解成，如果用户输入不规范，程序将会报错。

通过此程序的运行逻辑不难看出，通过对 CLanguage 类进行良好的封装，使得用户仅能通过暴露的 setter() 和 getter() 方法操作 name 和 add 属性，
而通过对 setname() 和 setadd() 方法进行适当的设计，可以避免用户对类中属性的不合理操作，从而提高了类的可维护性和安全性。

细心的读者可能还发现，CLanguage 类中还有一个 __display() 方法，由于该类方法为私有（private）方法，且该类没有提供操作该私有方法的“窗口”，

因此我们无法在类的外部使用它。换句话说，如下调用 __display() 方法是不可行的：
#尝试调用私有的 display() 方法
clang.__display()
这会导致如下错误：
Traceback (most recent call last):
  File "D:\python3.6\1.py", line 33, in <module>
    clang.__display()
AttributeError: 'CLanguage' object has no attribute '__display'
"""

# python 继承机制以及用法

"""
Python 中，实现继承的类称为子类，被继承的类称为父类（也可称为基类、超类）。因此在上面这个样例中，From 是子类，Shape 是父类。

子类继承父类时，只需在定义子类时，将父类（可以是多个）放在子类之后的圆括号里即可。语法格式如下：
class 类名(父类1, 父类2, ...)：
    #类定义部分

注意，如果该类没有显式指定继承自哪个类，则默认继承 object 类（object 类是 Python 中所有类的父类，即要么是直接父类，要么是间接父类）。
另外，Python 的继承是多继承机制（和 C++ 一样），即一个子类可以同时拥有多个直接父类。


注意，有读者可能还听说过“派生”这个词汇，它和继承是一个意思，只是观察角度不同而已。换句话话，继承是相对子类来说的，
即子类继承自父类；而派生是相对于父类来说的，即父类派生出子类。
"""


class People:
    def say(self):
        print('我是一个人，名字是：', self.name)


class Animal:
    def dispaly(self):
        print("人也是高级动物")


#  同时继承people和Animal类

# 同事拥有name属性，say（） display（）方法

class Person(People, Animal):
    pass


person = Person()
person.name = "小猪佩奇"
person.say()
person.dispaly()

# ，虽然 Person 类为空类，但由于其继承自 People 和 Animal 这 2 个类，因此实际上 Person 并不空，它同时拥有这 2 个类所有的属性和方法

#                       关于Python多继承

"""
事实上，大部分面向对象的编程语言，都只支持单继承，即子类有且只能有一个父类。而 Python 却支持多继承（C++也支持多继承）。
和单继承相比，多继承容易让代码逻辑复杂、思路混乱，一直备受争议，中小型项目中较少使用，后来的 Java、C#、PHP 等干脆取消了多继承。

使用多继承经常需要面临的问题是，多个父类中包含同名的类方法。对于这种情况，Python 的处置措施是：
根据子类继承多个父类时这些父类的前后次序决定，即排在前面父类中的类方法会覆盖排在后面父类中的同名类方法。
"""


class People:
    def __init__(self):
        self.name = People

    def say(self):
        print("People", self.name)


class Animal:
    def __init__(self):
        self.name = Animal

    def say(self):
        print("Animal类", self.name)


# people 中的那么属性和say（）会遮蔽Animal类中的

class person(People, Animal):
    pass


zhangsan = person()
zhangsan.name = '汪汪队'
zhangsan.say()

# 可以看到，当 Person 同时继承 People 类和 Animal 类时，People 类在前
# ，因此如果 People 和 Animal 拥有同名的类方法，实际调用的是 People 类中的。


#                               python 父类方法重写
"""
子类继承了父类，那么子类就拥有了父类所有的类属性和类方法。通常情况下，子类会在此基础上，扩展一些新的类属性和类方法。

但凡事都有例外，我们可能会遇到这样一种情况，即子类从父类继承得来的类方法中，大部分是适合子类使用的，
但有个别的类方法，并不能直接照搬父类的，如果不对这部分类方法进行修改，子类对象无法使用。针对这种情况，我们就需要在子类中重复父类的方法。

"""


class Bird:
    def iswing(self):
        print('鸟有翅膀')

    def fly(self):
        print('鸟会飞')


class Ostrich(Bird):
    # 重写Bird中的fly方法
    def fly(self):
        print('鸵鸟不会飞')


# 创建 Ostrich对象
ostrich = Ostrich()
# 调用Ostrich类中重写的fly方法
ostrich.fly()

#            如何调用被重写的方法

# 调用 Brid类中的fly方法

Bird.fly(ostrich)

# 此程序中，需要大家注意的一点是，使用类名调用其类方法，Python 不会为该方法的第一个 self 参数自定绑定值，
# 因此采用这种调用方法，需要手动为 self 参数赋值。
# 通过类名调用实例方法的这种方式，又被称为未绑定方法。


#                                         调用父类构造方法
"""
在子类中的构造方法中，调用父类构造方法的方式有 2 种，分别是：
类可以看做一个独立空间，在类的外部调用其中的实例方法，可以向调用普通函数那样，只不过需要额外备注类名（此方式又称为未绑定方法）；
使用 super() 函数。但如果涉及多继承，该函数只能调用第一个直接父类的构造方法。

但在 Python 3.x 中，super() 函数有一种更简单的语法格式，推荐大家使用这种格式：
super().__init__(self,...)
"""


class People:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("我是人，我的名字是：", self.name)


class Animal:
    def __init__(self, food):
        self.food = food

    def dispaly(self):
        print('我是动物，我吃', self.food)


class Person(People, Animal):
    # 定义构造法
    def __init__(self, name, food):
        # 调用 people类的构造方法
        super().__init__(name)  # super(People,self).__init__name
        # People.__init__(self,name)#使用未绑定方法调用 People 类构造方法
        # 调用其它父类的构造方法，需手动给 self 传值
        Animal.__init__(self, food)



per1 = Person('小猪佩奇', '猪猪侠')
per1.say()
per1.dispaly()

# 可以看到，Person 类自定义的构造方法中，调用 People 类构造方法，可以使用 super() 函数，
# 也可以使用未绑定方法。但是调用 Animal 类的构造方法，只能使用未绑定方法。
