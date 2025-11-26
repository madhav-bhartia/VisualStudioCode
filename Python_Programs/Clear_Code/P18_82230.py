class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def get_damage(self, damage):
        self.health -= damage

class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
    
    def attack(self, monster.get_damage())
        


monster = Monster(health = 100, energy = 50)