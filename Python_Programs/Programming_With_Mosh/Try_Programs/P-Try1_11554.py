def name_check():
    name = str(input("What is your name? -->"))

    if 3 <= len(name) <= 50:
        print("Name looks good!")
    else:
        print("Name should be of lenght 3-50!")


name_check()
