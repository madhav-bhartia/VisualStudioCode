# Pattern 1: star right triangle
count = 0
while count < 5:
    print('* ' * count + '*')
    count += 1
print()

# Pattern 2: num right triangle in reverse
count = 5
while count > 0:
    for num in range(1, (count+1)):
        print(num, end = ' ')
    print()
    count -= 1
print()


# Pattern 3: Alphabet right triangle
alpha = 'ABCDE'
alpha_print = ''
for char in alpha:
    alpha_print += char
    print(alpha_print)