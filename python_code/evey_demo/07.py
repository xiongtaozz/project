import time
# def foo(x):
#     print 'init foo,this x is:',x

def timeit(func):
    def water():
        start=time.clock()
        func
        end=time.clock()
        print 'time is:',start-end
    return water()
@timeit
def foo(x):
    print 'init foo,this x is:',x
# foo=foo(1)
# timeit(foo)