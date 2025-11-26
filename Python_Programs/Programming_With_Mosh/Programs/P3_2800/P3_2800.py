def convert():
    try:
        weight = float(input("weight: "))
        unit = input("(L)bs or (K)gs): ")
    except:
        print("Enter a valid numeric value!")

    if unit.upper() == "L":
        weight *= 2.205
        print(f"your weight in pounds is: {weight} lbs")
        print("Thank you for using this program\nHave a nice day! :)")
    elif unit.upper() == "K":
        weight /= 2.205
        print(f"your weight in kilgrams is: {weight} kgs")
        print("Thank you for using this program\nHave a nice day! :)")
    else:
        print("Unexpected error")


convert()
# need to lean why chc was not accepted but "CHCODDES" was accepted
