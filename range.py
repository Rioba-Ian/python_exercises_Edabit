x =  1

# for i in range(1000):
#     print(x)
#     x /=2
#     if x <= 0.001:
#         break

x =1 
while x > 0.001:
    print(x)
    x /= 2

L = ['Alan', 'Zoe', 'Hunter', 'Maddox', 'Kate','Tiffany']

for name in L:
    if 'x' in name:
        continue
    print(name)

for i in range(3):
    for name in L:
        if i == 1 and 'x' in name:
            break
        print(name)
    print('-----')