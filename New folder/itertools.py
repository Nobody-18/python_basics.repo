from itertools import product, accumulate
a = [1, 2]
b = [3]
q = product(a, b)
p = product(a, b, repeat = 2)
print(list(p))
print(list(q))


from itertools import permutations
c = [1, 2, 3, 4]
r = permutations(c)
s = permutations(c, 2)
print(list(r),list(s))


from itertools import combinations, combinations_with_replacement
t = combinations(c, 2)
u = combinations_with_replacement(c,2)
print(list(t), list(u))


acc = accumulate(c)
print(c,list(acc))
import operator
op = accumulate(c,func = operator.mul)
max = accumulate(c, func  = max)
print(list(op),list(max))


from itertools import groupby as gp


def smaller_than3(x):
    return x < 3


grp = gp(c, key=smaller_than3)
for key, value in grp :
    print(key, list(value))
persons = [{"name":"tim", "age":25}, {"name":"cook", "age":25}, {"name":"mary", "age":29}, {"name":"tommy", "age":19}]
g = gp(persons, key=lambda x:x["age"])
for key, value in g:
    print(key, list(value))


from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
for i in cycle(c):
    print(i)
    break
for i in repeat(1, 40):
    print(i)
