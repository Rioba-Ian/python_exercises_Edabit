a = ['banana','apple','microsoft']

for i in a:
    print(i)


b = [20, 10, 5]

total = 0

for e in b:
    total = total + e
print(total)

c = list(range(1,5))

total2 = 0

for j in c:
    total2 += j
print(total2)

print(list(range(1,8)))

total3 = 0

for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        total3 += i

print(total3)