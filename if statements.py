age = int(input("Enter your age: "))
if age > 100:
    print("you are very old.")
    print("well done!")
elif age > 80:
    print("you are fairly old")
    print("pretty good!")
elif age > 40:
    print("you are middle aged")
    print("never mind")
elif 30 <= age <= 40:
    print("you're getting older")
else:
    print("you are not very old - yet")

name = input("enter your name: ")
if name != "":
    print("Your name is", name)
else:
    print("Name not entered")