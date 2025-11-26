def automated():
    # Searched online
    import random

    randomlist = random.sample(range(0, 9999999), 5)
    max = randomlist[0]
    for number in randomlist:
        if max < number:
            max = number
    print(max)


numbers = [5, 10, 2, 3, 9646845, 89, 10000, 546466]
max = numbers[0]
for number in numbers:
    if max < number:
        max = number
print(max)

automated()

# Mistake: I need to reset "max" not add it!!!
# *****This was before i realised a mistake i made*****
# YESSS!!! Did it first try
# Adjusted a bit from solution but still :D
