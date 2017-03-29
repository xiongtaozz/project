# coding: utf-8
import time


class SchoolMember(object):
    # 总人数,这个是类的变量
    sum_member = 0

    # __init__方法在类的对象被创建时执行
    def __init__(self, name):
        self.name = name
        SchoolMember.sum_member += 1
        print "学校新加入一个成员：%s" % self.name
        print "现在有成员%d人" % SchoolMember.sum_member

    # 自我介绍
    def say_hello(self):
        print "大家好，我叫：%s" % self.name

    # __del__方法在对象不使用的时候运行
    def __del__(self):
        SchoolMember.sum_member -= 1
        print "%s离开了，学校还有%d人" % (self.name, SchoolMember.sum_member)


# 老师类继承学校成员类
class Teacher(SchoolMember):
    def __init__(self, name, salary):
        super(Teacher, self).__init__(name)  # SchoolMember.__init__(name)
        self.salary = salary

    def say_hello(self):
        SchoolMember.say_hello(self)
        print "我是老师，我的工资是：%d" % self.salary

    def __del__(self):
        SchoolMember.__del__(self)
        # super(Teacher, self).__del__()
        pass


# 学生类
class Student(SchoolMember):
    def __init__(self, name, mark):
        super(Student, self).__init__(name)
        self.mark = mark

    def say_hello(self):
        SchoolMember.say_hello(self)
        print "我是学生，我的成绩是：%d" % self.mark

    def __del__(self):
        # SchoolMember.__del__(self)
        super(Student, self).__del__()
        pass

t = Teacher("老黄", 3000)
t.say_hello()
time.sleep(1)
s = Student("小河", 77)
s.say_hello()
time.sleep(2)
