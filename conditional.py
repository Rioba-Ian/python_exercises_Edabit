name = "YK"

height_m = 2
weight_kg = 90

bmi = weight_kg/ (height_m ** 2)

print("bmi: ")
print(bmi)

if bmi < 25:
    print(name)
    print("is not overnight")
else:
    print(name)
    print("is overnight")
