# import math


# def elem(a, b):
#     a_set = set(a)
#     b_set = set(b)

#     val = a_set and b_set
#     return val


# gcd - Greatest common divisor
# def gcd(num1, num2):
#     list1 = list2 = []
#     for num in range(1, (num1//2)+1):
#         list1.append(num)
#     for num in range(1, (num2//2)+1):
#         list2.append(num)
#     val = elem(list1, list2)
#     print(val)

def gcd(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for num in range(1, smaller+1):
        if((num1 % num == 0) and (num2 % num == 0)):
            Gcd = num
    return Gcd


def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while(True):
        if((greater % num1 == 0) and (greater % num2 == 0)):
            Lcm = greater
            break
        greater += 1
    return Lcm
    

    
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
print(gcd(num1, num2))
print(lcm(num1, num2))