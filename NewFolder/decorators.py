def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper



@start_end_decorator
def sayhi(name):
    print('hii '+ name)
# sayhi = start_end_decorator(sayhi)
sayhi('alex')

@start_end_decorator
def add5(x):
    return x+5
print(add5(10) )   
