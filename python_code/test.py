def add_candles(cake_func):

    def insert_candles():

        return cake_func()+" and candles"

    return insert_candles


@add_candles
def make_cake():

    return "cake"

print(make_cake())


def add():
    return 1

print add()