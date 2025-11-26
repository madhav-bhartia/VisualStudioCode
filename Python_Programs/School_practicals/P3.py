num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 > num3:
    print("Largest number: ", num1)
    print("Smallest number: ", num3)
elif num1 > num3 > num2:
    print("Largest number: ", num1)
    print("Smallest number: ", num2)
elif num2 > num1 > num3:
    print("Largest number: ", num2)
    print("Smallest number: ", num3)
elif num2 > num3 > num1:
    print("Largest number: ", num2)
    print("Smallest number: ", num1)
elif num3 > num1 > num2:
    print("Largest number: ", num3)
    print("Smallest number: ", num2)
elif num3 > num2 > num1:
    print("Largest number: ", num3)
    print("Smallest number: ", num1)
else:
    pass