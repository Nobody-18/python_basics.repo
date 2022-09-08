from re import A


def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
value = next(g)

print(value)
value = next(g)

print(value)
value = next(g)
print(value)


def firstn(num):
    i = 0
    while i<=num:
        yield i
        i+=1
num2 = firstn(6)        
print(list(num2))
print(sum(firstn(6)))


def fibonaccii(limit):
    a,b,=0,1
    while a <limit:
        yield a
        a,b = b,b+a
fab = fibonaccii(10)
print(list(fab))
fab = fibonaccii(20)
for i in fab :
    print(i)


my_generator = (i for i in range (10) if i % 2 == 0)
for i in my_generator:
    print(i)
