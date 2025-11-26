exercise_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]

for list in exercise_list:
    for num in list:
        if num > 100:
            break
        if num < 50:
            if num < 10:
                continue

            print(num)


# The one i did above is better.
# What I originally did:
# for list in exercise_list:
#     for num in list:
#         if num < 10:
#             continue
#         if num < 50:
#             print(num)
#         if num > 100:
#             break
