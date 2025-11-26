x = int(input("Enter a number: "))
n = int(input("Enter the final exponent for the series: "))
sum, count = 0, 1
while count <= n:
    if count % 2 == 0:
        sum += (x**count)/count
    else:
        sum -= (x**count)/count
    count += 1
print("Sum: ", sum)