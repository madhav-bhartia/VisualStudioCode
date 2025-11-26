num = int(input("Enter a number: "))
sum, count = 0, 1
while count < num:
    if num % count == 0:
        sum += count
        count += 1
    else:
        count += 1
if sum == num:
    print(num, "is a perfect number!")
else:
    print(num, "is not a perfect number!")