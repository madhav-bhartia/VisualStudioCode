counter = 0
even_list = []
odd_list = []

while counter <= 100:
    if counter % 2 == 0:
        even_list.append(counter)
    else:
        odd_list.append(counter)
    counter += 1

print(f"The even list is:\n{even_list}\n")
print(f"The odd list is:\n{odd_list}\n")


# my way of doing it:
# counter += 2
# good for even values
# but useless for odd values

# another way to do it
even_list_v2 = []
odd_list_v2 = []

even_list_v2.extend(range(0, 101, 2))
odd_list_v2.extend(range(1, 100, 2))

print(f"The even list v2 is:\n{even_list_v2}\n")
print(f"The odd list v2 is:\n{odd_list_v2}\n")

# for even_list_without_58
even_list_without_58 = []
counter = 0

while counter <= 100:
    if counter % 2 == 0 and counter != 58:
        even_list_without_58.append(counter)
    counter += 1

print(f"The even list without 58 is:\n{even_list_without_58}\n")


# What I did for this:
################################
# while counter <= 100:
#     if counter % 2 == 0:
#         if counter == 58:
#             counter += 1
#             continue
#         even_list_without_58.append(counter)
#     counter += 1
#################################
# The above one is better though
