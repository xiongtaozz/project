class A:
    def __init__(self):
        self.b = 'info A'
    # def a(self):
    #     pass
    #
    # def b(self):
    #     pass

class B:
    def __init__(self, a):
        self.c = a

    def bb(self):
        print(self.c.b)  # a.a
a = A()
print(a.b)
x = B(a)
x.bb()