def seven_add(num):
    return num + 7

results = []
numbers = [1,2,3]

for number in numbers:
    results.append(seven_add(number))

# print(results)

print(list(map(seven_add, numbers)))


def add(num1, num2):
    return num1 + num2

list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]

m = map(add, list1, list2)
print(list(m))

l1 = [5, 7,8, 10, 11, 13,15, 16, 17, 19, 20]


def is_even(n):
    if n % 2 == 0:
        return n

   
m2 = filter(is_even, l1)

print(list(m2))