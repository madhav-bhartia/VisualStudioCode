x = int(input("Enter a number: "))
n = int(input("Enter the final exponent for the series: "))
sum, count = 0, 1
while count <= n:
    factorial = 1
    for num in range(1, count+1):
        factorial *= num
    if (count % 2) == 0:
        sum += (x**count)/factorial
    else:
        sum -= (x**count)/factorial
    count += 1
print("Sum: ", sum)