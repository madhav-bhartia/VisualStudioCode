num = int(input("Enter a number: "))
str_num = str(num)
sum, count = 0, len(str_num)
for digit in str_num:
    sum += int(digit) ** count
if sum == num:
    print(num, "is a armstrong number!")
else:
    print(num, "is not a armstrong number!")