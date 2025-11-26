import re

def unconditional_mul(lines):
    arr = []
    for line in lines:
        partitioned = re.split(r'(mul\()', line)
        arr.append(partitioned)
    
    array = []
    for line in arr:
        for i in range(1, len(line)):
            if line[i] == 'mul(':
                array.append(line[i+1])
    
    del lines
    del arr

    valid_expressions = []
    for elem in array:
        pattern = re.compile(r'^(\d{1,3}),(\d{1,3})\)')
        matched = pattern.match(elem)
        if matched:
            valid_expressions.append(matched.groups())
    
    sum = 0
    num1 = 0
    num2 = 0
    for elem in valid_expressions:
        num1 = int(elem[0])
        num2 = int(elem[1])
        sum += num1 * num2
    
    return sum


def conditional_mul(lines):
    arr = []
    for line in lines:
        partitioned = re.split(r'(mul\(|do\(\)|don\'t\(\))', line)
        arr.extend(partitioned)
    
    array = []
    is_do = True
    for i in range(1, len(arr)):
        if arr[i] == 'don\'t()':
            is_do = False
        elif arr[i] == 'do()':
            is_do = True
        if arr[i] == 'mul(' and is_do:
            array.append(arr[i+1])
    
    del lines
    del arr
    del is_do

    valid_expressions = []
    for elem in array:
        pattern = re.compile(r'^(\d{1,3}),(\d{1,3})\)')
        matched = pattern.match(elem)
        if matched:
            valid_expressions.append(matched.groups())
    
    sum = 0
    num1 = 0
    num2 = 0
    for elem in valid_expressions:
        num1 = int(elem[0])
        num2 = int(elem[1])
        sum += num1 * num2
    
    return sum


def main():
    
    with open('AdventOfCode\\day3.txt', 'r') as file:
        lines = file.readlines()
    

    print(unconditional_mul(lines))
    print(conditional_mul(lines))


main()