# if <condition> :
    # when condition is true

if True:
    print("it's true")

if False:
    print("it's false")

number = input("input a number >>> ")
number = int(number)

if number % 2 == 0:
    print("even")
if number % 2 != 0:
    print("odd")


if number < 10:
    print("less than 10")
elif number < 20:
    print("less than 20")
elif number < 30:
    print("less than 30")
else:
    print("hahaha")