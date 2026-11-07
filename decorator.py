def mydecorator(func):
    count = 0
    def f(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{count} раз вызвана функция и ее результат:')
        result = func(*args, **kwargs)

        return result
    return f

@mydecorator
def test():
    print(456)
    return 0

@mydecorator
def summ(a, b):
    print(a + b)
    return 0

test()
test()
summ(2,3)
summ(4,5)
test()
