import secrets
a = secrets.randbelow(10)
print(a)
b = secrets.randbits(4)
print(b)
l = list("BBGGBJKMMB")
c = secrets.choice(l)
print(c)


import numpy as np
np.random.seed(1)
d = np.random.randint(0,10,(3, 4))
print(d)
l = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(l)
np.random.shuffle(l)
print(l)