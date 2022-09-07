try:
    a = 5/10
    b = a+5
except ZeroDivisionError as e:
    print(e)
except TypeError as e :
    print(e)
else:
    print("Everything is fine")  # when no exceptions arise
finally:
    print("Done anyway")  # run in eighther case
class ValueTooHighError(Exception):
    pass
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x>100:
        raise ValueTooHighError('Value is too high')
    if x<5:
        raise ValueTooLowError('Value is too low', x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.value,e.message )