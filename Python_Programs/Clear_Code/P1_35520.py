money_available = 100
is_hungry = True
is_bored = True
if money_available > 80 and is_hungry == True or is_bored == True:
    print("Eat something nice! :)")

if money_available > 80:
    if is_hungry == True:
        if is_bored == True:
            print("Eat something nice! :)")
else:
    print("it's okay. Do something fun :)")