def palindrome(string):
    rev_string = ''
    for index in range ((len(string) - 1), -1, -1):
        rev_string += string[index]
    if string.lower() == rev_string.lower():
        print(string, 'is a palindrome.')
    else:
        print(string, 'is not a palindrome.')

def case_swap(string):
    case_swapped_string = string.swapcase()
    print('The case swapped string is:', case_swapped_string)

string = input("Enter a string.\n-> ")
palindrome(string)
case_swap(string)