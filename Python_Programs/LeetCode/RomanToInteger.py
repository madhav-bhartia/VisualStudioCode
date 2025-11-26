roman = "IVXLCDM"
string = input("Enter the roman numeral: ")
converted = []
result = 0
dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

for elem in string:
    if elem in roman:
        converted.append(dict[elem])
    else:
        print("Invalid input!")
        break

length = len(converted)
i = 0
while i < length:
    if i+1 < length and converted[i] < converted[i+1]:
        result += converted[i+1] - converted[i]
        i+=2
    else:
        result += converted[i]
        i+=1

print(result)