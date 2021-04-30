numbers = [1, 3,2,5, 4,6,8]

for number in numbers:
    if number%2 == 0:
        continue
    else:
        print(number)

i = 0
while i <10:
    i += 1
    if i == 3:
        continue
    print(i)

# i = 0
# while i<3:
#     print('D')

x = ['data','science']
for i in x:
    i.upper()
print(x)


x = 'datascience'
for i in x:
    print(i.upper())

print(list(range(5, 0,-2)))

x =0
while x < 100:
    x += 2
print(x)

for num in range(2,-5,-1):
    print(num, end=",")

dphi = 10
for i in range(10):
    for j in range(2,10,1):
        if dphi % 2 == 0:
            continue
        dphi += 1
    dphi += 1
else:
    dphi += 1
print(dphi)

for num in range(10, 14):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break

numbers = [10,20]

items = ['Chair','Table']

for x in numbers:
    for y in items:
        print(x, y)