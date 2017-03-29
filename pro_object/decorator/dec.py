# coding:utf-8
import logging


def adder(foo):

    print 'in adder'

    def wader():
        print 'in wader'
        foo()
    return wader

@adder
def foo():
    print 'in foo'
    pass

foo()
