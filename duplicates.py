list1 = [10,20,51,60, 20, 10, 23, 25,23,51, 25]

# list1 = list(dict.fromkeys(list1))

# print(list1)


list2 = []

for i in list1:
    if i in list2:
        continue
    else:
        list2.append(i)
print(list2)