def Down_payment(has_good_credit=input("Do you have good credit? ")):
    House_SP = 1000000

    if has_good_credit:
        down_payment = 0.1 * House_SP
    else:
        down_payment = 0.2 * House_SP

    print(f"down_payment: ${down_payment}")


Down_payment()
# Still can be improved
# Need to check for input value
