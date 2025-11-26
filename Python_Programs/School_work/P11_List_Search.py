size = int(input('Enter the number of elements: '))
list = []
while size:
    elem = input('-> ')
    if elem.isdigit():
        elem = int(elem)
        list.append(elem)
    else:
        list.append(elem)
    size -= 1

val = input("Enter the value to search: ")
if val.isdigit():
    val = int(val)

index = len(list) - 1
while index >= 0:
    if val == list[index]:
        print('Value found:', val)
        print('At position', index + 1)
        break
    index -= 1
else:
    print('Value not found!')