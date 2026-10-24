class MyException(Exception):
    pass





a = 1
b = 0
try:
    print(a / b)
except OverflowError as e:
    print('We are in zero division error')
    print(e)
except Exception as e:
    import traceback
    print(traceback.format_exc())
    print('We are in exception error')
    print(e)
else:
    print('No exception')
finally:
    print('ты ебанат')