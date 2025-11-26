from datetime import datetime

def greet(person="Person", greet="Hello", weekday="Monday"):
    print(f"{greet}!, {person}. Today is {weekday}")


greet(input("Please enter your name.\n-> "), weekday = datetime.now().strftime('%A'))
