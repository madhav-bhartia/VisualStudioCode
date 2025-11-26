numbers = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 9, 10]
for i in numbers:
    if numbers.count(i) != 1:
        numbers.remove(i)
        numbers.sort()

print(numbers)

# Did it!!! :D

# This was the solution
# To use another list
numbers_solution = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 9, 10]
uniques_solution = []
for number in numbers_solution:
    if number not in uniques_solution:
        uniques_solution.append(number)

print(uniques_solution)
