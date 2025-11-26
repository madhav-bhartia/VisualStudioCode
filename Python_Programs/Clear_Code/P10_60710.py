inventory_names = ["Screws", "Wheels", "Metal Parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]

# Solution in video

for index, inv_tuple in enumerate(zip(inventory_names, inventory_numbers)):
    print(f"{inv_tuple[0]} [id: {index}] - inventory: {inv_tuple[1]}")


# NOTE: What I did. (It's also more memory consuming I think)
# ##############################################################################
# index_list = []
# name_list = []
#
# for index, name in enumerate(inventory_names):
#     index_list.append(index)
#     name_list.append(name)
# for index, name, inventory in zip(index_list, name_list, inventory_numbers):
#     print(f"{name} [id: {index}] - inventory: {inventory}")
# ##############################################################################
