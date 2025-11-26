def is_safe(record):
    ascending = True
    descending = True
    for i in range(len(record)-1):
        x = record[i]
        y = record[i + 1]
        if x >= y:
            ascending = False
        if x <= y:
            descending = False
        if abs(x-y) not in [1, 2, 3]:
            return False

    return ascending or descending


def main():
    
    with open('AdventOfCode\\day2.txt', 'r') as file:
        lines = file.readlines()
    
    matrix = []
    
    for line in lines:
        record = list(map(int, line.split()))
        matrix.append(record)
    
    del lines
    del record

    no_of_safe_reports = 0
    no_of_safe_reports_damp = 0
    for record in matrix:
        if is_safe(record):
            no_of_safe_reports += 1
        for i in range(len(record)):
            if is_safe(record[:i] + record[i+1:]):
                no_of_safe_reports_damp += 1
                break
    
    print(no_of_safe_reports)
    print(no_of_safe_reports_damp)



main()