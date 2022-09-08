# sets are unordered ,mutable, no duplicate elements
my_set = {1, 4, 2, 3, }
print(my_set)
myset = set([1, 2, 3, 4])
print(myset)
# set = {}  # not an empty set it is dictionary
set2 = set()  # empthy set
set1 = set("hello")
set2.add(1)
set2.add(2)
set2.add(3)
set2.add(5)
set2.add(6)
set2.remove(2)
set2.discard(4)
print(set2.pop())
print(set1,set2)
for i in set2:
    print(i)
odds = {1, 3, 5, 7, 9, 11, 13, 15}
evens = {2, 4, 6, 8, 10, 12, 14, 16}
prime = {1, 2, 3, 5, 7, 11, 13, 17, 19}
u = odds.union(evens)  # odd union even
print(u)
i = odds.intersection(prime)  # odd intersection prime
print(i)
d = odds.difference(prime)  # odd - prime
print(d)
sd = odds.symmetric_difference(prime)  # inv of odd intersection prime
print(sd)
A = {1, 2, 3, 4, 5, 6, 9, 10}
B = {1, 2, 3, 4, 7, 8, 11}
A.update(B)  # add elments of b that are not in a to a
print(A)
A.intersection_update(B)  # make a intesection of and b
print(A)
c = {1, 2, 3, 4, 5, 6}
d = {1, 2, 3, 4}
print(c.issubset(d))  # True if c is usbset of d
print(c.issuperset(d))
print(c.isdisjoint(d))
e = frozenset(d)  # immutable set
print(e)
