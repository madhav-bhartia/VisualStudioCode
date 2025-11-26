string = input("Enter a string.\n-> ")
rev_string = ''
for index in range ((len(string) - 1), -1, -1):
    rev_string += string[index]
if string.lower() == rev_string.lower():
    print(string, 'is a palindrome.')
else:
    print(string, 'is not a palindrome.')