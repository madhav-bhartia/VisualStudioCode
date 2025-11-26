menu = "Black Coffee, Espresso, Latte, Cappuccino"
price = 2

print("Hello!, Welcome to NetworkChuck Coffee!!!!!")
name = input("What is your Name?\n-> ")
print(f"Hello {name}, Thank you for coming in today!")

order = input(
    f"Here is our menu\n{menu}\nEvery item is {price}$\nWhat would you like to order?\n-> "
)
quantity = int(input("How many would you like to order?\n-> "))

bill = price * quantity

print(f"Hey {name}, your {quantity} {order} will be ready in a few minutes! :)")
print(f"The total bill is ${bill}")

# Note: formatted strings a.k.a "f" strings
#       can concatenate integers with string!
#       normal concatenation can't!!!
# bill = str(price * quantity)
# print("The total bill is" + bill + "$")
