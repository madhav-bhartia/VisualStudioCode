x = int(input("Enter a number: "))
n = int(input("Enter the final exponent for the series: "))
sum = count = 1
while count <= n:
    sum += x**count
    count += 1
print("Sum: ", sum)