multiplier = 2
has_calculated = False


def multiply_calc(number):
    global has_calculated
    has_calculated = True
    result = number * multiplier
    return result


try:
    result = multiply_calc(int(input("Enter a number to be multiplied\n-> ")))
    print(f"The result is: {result}")
    print(has_calculated)
except ValueError:
    print("Invalid value entered! Value enter must be a number (Integer)")




# NOTE: The Input function can be passed
#       in a user defined function as an argument!F
