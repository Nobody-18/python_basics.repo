# collections counter, namedtuple, ordereddict, defaultdict, deque
from collections import Counter
a = "aabhsababsddhhaabd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.most_common(2))
print(list(my_counter.elements()))


from collections import namedtuple
point = namedtuple('point', "x,y")
pt = point(1, -4)
print(pt.x, pt.y)


from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['d'])


from collections import deque
de =deque()
de.append(1)
de.append(2)
de.appendleft(3)
de.popleft()
# de.clear()
de.extendleft([4, 5, 6])
de.rotate(-1)
print(de)
