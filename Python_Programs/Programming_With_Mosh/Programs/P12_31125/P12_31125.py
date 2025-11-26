class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello! I am {self.name}")


name = input("Enter a name. -> ")
AI = Person(name)
AI.talk()
