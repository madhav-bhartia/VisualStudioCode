students, loop = {}, True
print('Menu:')
print('1. Add a student')
print('2. Remove a student')
print('3. Display students with marks higher than 75.')
print('4. Quit')
while loop:
    chc = int(input('Enter your choice\n-> '))
    print()
    match chc:
        case 1:
            roll_no = int(input('Enter the roll number: '))
            name = input('Enter the name: ')
            marks = int(input('Enter the marks: '))
            students[roll_no] = [name, marks]
            print()
        case 2:
            roll_no = int(input('Enter the roll number: '))
            del students[roll_no]
        case 3:
            for roll_no in students.keys():
                name, marks = students.get(roll_no)
                if marks > 75:
                    print(name, '-', marks)
                    # nm, mks = students[roll_no]
                    # print(nm, '-', mks)
            print()
        case 4:
            print('Closing the program...')
            loop = False
        case _:
            print("Unexpected error!")