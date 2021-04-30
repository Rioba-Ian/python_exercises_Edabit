a, b = 12, 5

if a + b:
    print(True)
else:
    print(False)

if (1,2): 

 print('foo')


if 1 + 1 == 2:
    if 2 * 2 == 16:
        print("if")
    else:
        print("else")

if 1:
    print("Yes")
else:
    print("1 is not truthy!")


x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

def bar(z):
    i = 1
    while (i <= z):
        i *= 2
    return i
    print(i)
print(bar(7))

if "Ian is here":
    print("Yes")
else:
    print("No")