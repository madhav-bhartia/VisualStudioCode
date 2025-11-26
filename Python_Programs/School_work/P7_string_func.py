def str_func(string):
    #Count the number of vowels, consonants, uppercase and lowercase characters
    vowel = const = ucase = lcase = 0
    for char in string:
        if char.islower():
            lcase += 1
        else:
            ucase += 1
        for ch in 'aeiouAEIOU':
            if ch == char:
                vowel += 1
    const = len(string) - vowel

    print("Number of vowels:", vowel)
    print("Number of consonants:", const)
    print("Number of uppercase characters:", ucase)
    print("Number of lowercase characters:", lcase)

string = input("Enter a word to display it's details.\n-> ")
str_func(string)