# small one line function without name
add10 = lambda x: x + 10
print(add10(5))
add = lambda x, y: x+y
print(add(5,6))
mul = lambda x, y: x*y
print(mul(9, 2))
points2D = [(1, 2), (13, 4), (5, -6), (17, 8)]
p2Ds = sorted(points2D, key=lambda x: x[1])
print(points2D)
p2Ds1 = sorted(points2D, key=lambda x: x[0] + x[1])
print(p2Ds)
print(p2Ds1)


a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))
c = [x*2 for x in a]
print(c)
d = filter(lambda x:x%2 == 0, a)
print(list(d))
e = [x for x in a if x%2 ==0]
print(e)
from functools import reduce
f = reduce(lambda x, y: x*y, a)
print(f)
