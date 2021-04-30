total = 0

for i in range(1, 5):
    total += i
print(total)

total2 = 0

j = 1

while j <5:
    total2 +=j
    j += 1
print(total2)

given_list = [5,4, 3, 2, 1, 8]

total3 = 0

i = 0
# This only works when the list has both negative and positive integres
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)

given_list2 = [5,4, 3, 2, 1, - 4, -7, 8]

total4 = 0 

for element in given_list2:
    if element <= 0:
        break
    total4 +=element
print(total4)


total5 = 0
i = 0

while True:
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break
print(total5)

