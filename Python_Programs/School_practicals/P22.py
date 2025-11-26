size = int(input('Enter the number of elements: '))
list = []
while size:
    list.append(input())
    size -= 1
index = len(list)
if index % 2 != 0:
    index -= 1
print(list)
for i in range(0, index, 2):
    list[i], list[i+1] = list[i+1], list[i]
print(list)