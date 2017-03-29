from django.test import TestCase

# Create your tests here.


class Empty:
    pass

ept = Empty
ept.foo = 'foo'
print ept.foo


def use_class(mc):

    return type(mc())

print use_class(ept)