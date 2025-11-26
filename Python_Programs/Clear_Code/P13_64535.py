inventory_names = ["Screws", "Wheels", "Metal Parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]
combined_list = list(zip(inventory_names, inventory_numbers))
print(combined_list)


# Sorting by inventory_numbers
sorted_list1 = sorted(combined_list, key = lambda num: num[1])
print(sorted_list1)


# Sorting by inventory_numbers
sorted_list2 = sorted(combined_list, key = lambda word: len(word[0]))
print(sorted_list2)