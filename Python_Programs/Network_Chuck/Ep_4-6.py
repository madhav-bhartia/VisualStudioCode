menu = "Black Coffee... $1, Espresso... $3, Latte... $1, Cappuccino... $4, Frappuccino... $6"
price = 0
quantity = 0

print("Hello!, Welcome to NetworkChuck Coffee!!!!!")

name = input("What is your Name?\n-> ")

if name == "Ben" or "Patricia" or "Loki":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        number_of_good_deeds = int(input("How many good deeds have you done today?\n-> "))
        if number_of_good_deeds < 4:
            print(f"you are not welcome here evil {name}! Get Out!!!")
            exit()
        else:
            pass
    else:
        pass

print(f"Hello {name}, Thank you for coming in today!")

order = input(
    f"Here is our menu\n{menu}\nWhat would you like to order?\n-> "
)

if order == "Black Coffee":
    price = 1
    quantity = int(input("How many would you like to order?\n-> "))
elif order == "Espresso":
    price = 3
    quantity = int(input("How many would you like to order?\n-> "))
elif order == "Latte":
    price = 1
    quantity = int(input("How many would you like to order?\n-> "))
elif order == "Cappuccino":
    price = 4
    quantity = int(input("How many would you like to order?\n-> "))
elif order == "Frappuccino":
    price = 6
    quantity = int(input("How many would you like to order?\n-> "))
else:
    print("Sorry! but we don't have that here yet!")
    exit()

bill = price * quantity

print(f"Hey {name}, your {quantity} {order} will be ready in a few minutes! :)")
print(f"The total bill is ${bill}")
print("Come again later :)")

# Note: formatted strings a.k.a "f" strings
#       can concatenate integers with string!
#       normal concatenation can't!!!
# bill = str(price * quantity)
# print("The total bill is" + bill + "$")
