x = int(input("Enter a number: "))
n = int(input("Enter the final exponent for the series: "))
sum = count = 1
while count <= n:
    if (count % 2) == 0:
        sum += x**count
    else:
        sum -= x**count
    count += 1
print("Sum: ", sum)