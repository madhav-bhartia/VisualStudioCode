count, list = int(input("Enter the number of elements: ")), []
while count:
    list.append(input())
    count -= 1
print(max(list), "is the maximum value in the list")
print(min(list), "is the minimum value in the list")