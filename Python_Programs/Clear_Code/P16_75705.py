class Monster:
    
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def __str__(self):
        return 'A Monster'
    
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt.')
        monster.energy -= 20
        print(self.energy)
    
    def move(self, amount):
        print(f"The monster has moved.It's speed was {amount}.")


monster = Monster(50,90)
