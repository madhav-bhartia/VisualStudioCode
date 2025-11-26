import random

def word_src():
    file_path = "Project_Hangman\hangman_words.txt"
    with open(file_path, "r") as hangman_words:
        return hangman_words.read().split("\n")

def og_word(word_list):
    random_word = random.choice(word_list)
    return random_word

def disp_word(p_og_word, p_constant):
    secret_word = ""
    for letter in p_og_word:
        secret_word += p_constant
    return secret_word

# A little test. It worked!! :D
# print(og_word)
# print(disp_word)
# print(f'The length of the original word is {len(og_word)}.')
# print(f'The length of the display word is {len(disp_word)}.')

# return og_word, disp_word, constant


def gameplay(og_word, disp_word, constant):
    list_disp_word = list(disp_word)
    final_word = "".join([str(elem) for elem in list_disp_word])
    print(f"The secret word is: {final_word}")
    lives_counter = 6

    while final_word.__contains__(constant):
        match lives_counter:
            case 6:
                print("__________________________")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")

            case 5:
                print("__________________________")
                print("|             |")
                print("|           /¯¯¯\\")
                print("|          |     | ")
                print("|          \\____/")

            case 4:
                print("__________________________")
                print("|             |")
                print("|           /¯¯¯\\")
                print("|          |  ツ | ")
                print("|          \\____/")

            case 3:
                print("__________________________")
                print("|             |")
                print("|           /¯¯¯\\")
                print("|          |  ツ | ")
                print("|          \\____/")
                print("|             |")
                print("|             |")
                print("|             |")
                print("|             |")
                print("|             |")

            case 2:
                print("__________________________")
                print("|             |")
                print("|           /¯¯¯\\")
                print("|          |  ツ | ")
                print("|          \\____/")
                print("|             |")
                print("|            /|\\")
                print("|           / | \\")
                print("|   ¯\\____/  |  \\____/¯")

            case 1:
                print("__________________________")
                print("|             |")
                print("|           /¯¯¯\\")
                print("|          |  ツ | ")
                print("|          \\____/")
                print("|             |")
                print("|            /|\\")
                print("|           / | \\")
                print("|   ¯\\____/  |  \\____/¯")
                print("|             |")
                print("|             |")

        print(final_word)
        char = input("Enter a letter.\n-> ")
        n = 0
        char_not_found = False

        while n < len(list_disp_word):
            if list_disp_word[n] == constant:
                if char == og_word[n]:
                    list_disp_word[n] = char
                    n += 1
                else:
                    n += 1
                    if og_word.__contains__(char) == False:
                        char_not_found = True

            else:
                n += 1

        final_word = "".join([str(elem) for elem in list_disp_word])
        print(final_word)

        if not (final_word.__contains__(constant)):
            break

        if char_not_found == True:
            lives_counter -= 1
            char_not_found = False

        print(f"Lives remaining: {lives_counter}")

        match lives_counter:
            case 0:
                print("__________________________")
                print("|             |")
                print("|             |")
                print("|           /¯¯¯\\")
                print("|          |     | ")
                print("|         \\_____/")
                print("|             |")
                print("|            /|\\")
                print("|           / | \\")
                print("|   ¯\\____/  |  \\____/¯")
                print("|             |")
                print("|            / \\")
                print("|           /   \\")
                print("|          /     \\")
                print("|         /       \\")
            case _:
                pass

        if lives_counter <= 0:
            return None

    return final_word, lives_counter

# og_word, disp_word, constant = secret_word()

word_list = word_src()

og_word = og_word(word_list)
print(og_word)

constant = input("Enter a letter to represent the original word secretly.\n-> ")

disp_word = disp_word(og_word, constant)

final_word, lives_counter = gameplay(og_word, disp_word, constant)

if final_word == None:
    print("Game over! You died.")
    print("Better luck next time! ¯\_(ツ)_/¯")
else:
    print("Congratulations, ╰(*°▽°*)╯")
    print(f"You guessed the word: {final_word}")
    print(f"Lives remaining: {lives_counter}")

