my_list = [1,2,3,4,5]
print(f"Here's the original list: {my_list}")

print('Using map() and filter() functions')
# Using map() function
print(f'Squaring the list: {list(map(lambda num: num ** 2, my_list))}')

# Using filter() function
print(f'Filtering out numbers greater than 3: {list(filter(lambda num: num < 4, my_list))}')

print('Using list comprehensions instead of the map() and filter() functions')
# Using list comprehension instead of map() function
# ###############################################################
# my_list_map_comprehension = [num ** 2 for num in my_list]
# print(f'Squaring the list: {my_list_map_comprehension}')
# ###############################################################
print(f'Squaring the list: {[num ** 2 for num in my_list]}')

# Using list comprehension instead of filter() function
# ###############################################################
# my_list_filter_comprehension = [num for num in my_list if num < 4]
# print(f'Filtering out numbers greater than 3: {my_list_filter_comprehension}')
# ###############################################################
print(f'Filtering out numbers greater than 3: {[num for num in my_list if num < 4]}')