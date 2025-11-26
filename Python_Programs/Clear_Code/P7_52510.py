def calc_inf(*addends):
    result = sum(addends)
    print(f"The total is: {result}")


calc_inf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Used "sum(addends)" after seeing it in the solution.
# NOTE: what I did originally.:
######################
# for number in addends:
#     result += number
###############################
