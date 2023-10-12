names = ["Daniel", "Steve", "John", "Larry"]
for x in names:
    print(x)

for x in range(2, 11, 2):
    print(x ,"to the power of" , x , "=" , x ** x)

numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for x in numbers:
    if x > 100:
        break
    total += x
    print(total)
else:
    print("all numbers processed")