import time


# 定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
# 2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
# 3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
# 4、使用新手机对象调用手机介绍的方法；
# 5、使用新手机对象调用打电话的方法；

class oldPhone:
    __brand = ""

    def set_brand(self, brand):
        if brand == "":
            print("品牌非空！")
        else:
            self.__brand = brand

    def get_brand(self):
        return self.__brand

    def phoned(self, number):
        print("正在打%d电话中" % number, end="")
        for i in range(6):
            print(".", end="")
            time.sleep(1)
        print("对方已接通")


class onephone(oldPhone):

    def phoned(self, number):
        print("语音拨号中", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        super().phoned(number)

    def introduce(self):
        print("品牌为%s的手机很好用..." % super().get_brand())


# old = oldPhone()
# old.phoned(15571651335)
# one = onephone()
# one.set_brand("洛基亚")
# one.phoned(18544533581)
# one.introduce()


# 1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
# 2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# 3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
# 4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
# 5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；


class cooking:
    __username = ""
    __age = 0

    def set_username(self, username):
        if username == "":
            print("你没名字？")
        else:
            self.__username = username

    def get_username(self):
        return self.__username

    def set_age(self, age):
        if 130 >= age >= 0:
            self.__age = age
        else:
            print("你是没出生还是打破了世界纪录？")

    def get_age(self):
        return self.__age

    def cook(self):
        return "蒸饭的方法:..."


class fry_cook(cooking):

    def fry(self):
        return "炒菜的方法：..."


class cook_dinner(fry_cook):

    def cook(self):
        print("大厨%s正在通过%s做饭" % (super().get_username(), super().cook()))

    def fry(self):
        print("大厨%s正在通过%s炒菜" % (super().get_username(), super().fry()))

    def age(self):
        print("大厨%s今年已经%d岁了" % (super().get_username(), super().get_age()))


cook = cook_dinner()
cook.set_username("张三")
cook.set_age(20)
print(cook.get_username(), cook.get_age())
cook.cook()
cook.fry()
cook.age()


# i.	人：年龄，性别，姓名。
#
# ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
#
# iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

class person:
    __age = 0
    __sex = ""
    __username = ""

    def set_age(self, age):
        if age > 120 or age < 0:
            print("你是没出生还是打破了世界纪录？")
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    def set_sex(self, sex):
        if sex == "男" or sex == '女':
            self.__sex = sex
        else:
            print("你就是传说中的秀吉吗！！！")

    def get_sex(self):
        return self.__sex

    def set_username(self, username):
        if username == "":
            print("你就是空白？")
        else:
            self.__username = username

    def get_username(self):
        return self.__username


class workers(person):

    def work(self):
        print("我是工人，我叫%s,性别%s,今年%d岁了,我正在干活" % (super().get_username(), super().get_sex(), super().get_age()))


class student(person):
    __number = ""

    def set_number(self, number):
        if number == "":
            print("学号非法！")
        else:
            self.__number = number

    def get_number(self):
        return self.__number

    def learn(self):
        print("我是学生,我叫%s,性别%s,今年%d岁了,这是我的学号:%s,我正在学习" % (self.get_username(), super().get_sex(),
                                                         super().get_age(), self.__number))

    def sing(self):
        print("我是学生,我叫%s,性别%s,今年%d岁了,这是我的学号:%s,我正在唱歌" % (self.get_username(), super().get_sex(),
                                                         super().get_age(), self.__number))


work = workers()
stu = student()
work.set_username("张三")
work.set_sex('男')
work.set_age(30)
stu.set_username("小小")
stu.set_sex("女")
stu.set_age(12)
stu.set_number(16512389456)
work.work()
stu.learn()
stu.sing()
