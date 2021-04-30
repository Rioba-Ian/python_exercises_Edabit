import timeit

t = timeit.timeit(stmt="""
ls = []
for value in range(1, 1000000):
    ls.append(value*value)
""", number=1)

print(t)

t2 = timeit.timeit(stmt="""
l2 = [value * value for value in range(1, 1000000)]
""", number=1)
print(t2)

"""
[output expression for value in list filtering conditions]

"""

a = [1, 3, 4, 6, 8, 9, 11]

c = []
for x in a:
    c.append(x * 2)
print(c)

d = [x * 2 for x in a]
print(d)

b = []

b.append(10)
print(b)


e1 = []
for x in range(1,7):
    e1.append(x ** 2)
print(e1)

e2 = [x ** 3 for x in range(1, 7)]
print(e2)

# [36, 25, 16, 9, 4, 1]

e3 = [x ** 2 for x in range(6,0, -1)]
print(e3)

l = ['abc', 'abcd', 'aabbccddd', 'eeeeeeaaaaaaaaa']

le = [len(i) for i in l]
print(le)

e4 = [x % 2 == 0  for x in range(10)]
print(list(e4))