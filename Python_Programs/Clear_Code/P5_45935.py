def basic_calc(num1, num2, operation):
    if operation == 'add':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == 'subtract':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == 'multiply':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == 'divide':
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("¯\_(ツ)_/¯\nUnknown operation")

x = int(input("Enter your first number!\n-> "))
y = int(input("Enter your second number!\n-> "))
print("Please enter what you want to do?\nadd, subtact, multiply or divide")
operation = input("-> ")

basic_calc(x, y, operation)
