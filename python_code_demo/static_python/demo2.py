# -*- coding:utf-8 -*-

'''
    简单的工厂模式
'''


class Factory:

    def createFruit(self, fruit):  # 相似生成器
        if fruit == "apple":
            return Apple()
        elif fruit == "banana":
            return Banana()

# 水果类
class Fruit:
    def __str__(self):
        return "fruit"

# 水果子类
class Apple(Fruit):
    def __str__(self):
        return "apple"

# 水果子类
class Banana(Fruit):
    def __str__(self):
        return "banana"

if __name__ == "__main__":
    factory = Factory()
    print factory.createFruit("apple")
    print factory.createFruit("banana")
