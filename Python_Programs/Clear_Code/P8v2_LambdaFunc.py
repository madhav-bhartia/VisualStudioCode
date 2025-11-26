
# This is Program 8 but with using lambda function

multiplier = 2
has_calculated = False

return_lambda = lambda number: number * multiplier
has_calculated = True

try:
    result_lambda = return_lambda(int(input("Enter a number to be multiplied\n-> ")))
    print(result_lambda)
    print(has_calculated)
except ValueError:
    print("Invalid value entered! Value enter must be a number (Integer)")
