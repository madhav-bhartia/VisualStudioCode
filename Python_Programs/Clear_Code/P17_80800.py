class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:
    def bite():
        print('used bite')
    
    def strike():
        print('used strike')
    
    def slash():
        print('used slash')
    
    def kick():
        print('used kick')

attacks = Attacks()
monster = Monster(attacks.slash)
monster.func()