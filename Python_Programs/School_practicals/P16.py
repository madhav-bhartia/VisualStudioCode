num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
if num1 > num2:
        smaller = num2
else:
    smaller = num1
for num in range(1, smaller+1):
    if((num1 % num == 0) and (num2 % num == 0)):
        gcd = num
print(gcd, "is the greatest common divisor of the 2 numbers.")
