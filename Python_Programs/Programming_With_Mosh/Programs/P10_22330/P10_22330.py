phone = list(input("Phone:"))
number_to_words = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
}
output = ""

for number in phone:
    output += number_to_words.get(number, "N/A") + " "

print(output)

# This is what I wrote before seeing the solution
# try:
#    for number in phone:
#      print(number_to_words[number])
# except KeyError:
#     print("Invalid Values!")
# :D Solved!
