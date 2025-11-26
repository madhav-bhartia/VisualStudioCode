def fibonacci(num):
    count, n1, n2, nth = 0, 0, 1, 0
    if num < 0:
        print("Please enter a positive number!")
    elif num == 1:
        print(n1)
    else:
        while count < num:
            print(n1, end = ' ')
            nth = n1 + n2
            n1, n2 = n2, nth
            count += 1
            
        

num = int(input("Enter the number of terms of fibonacci series to print it.\n-> "))
fibonacci(num)