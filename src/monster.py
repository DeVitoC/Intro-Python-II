from random import random
class Monster:
    
    def __init__(self, name):
        self.name = name
        self.strength = 0
        self.armor = 0
        self.health = 0
        
    def view_stats(self, *args):
        print(f"{self.name}:\nStrength: {self.strength}\nArmor: {self.armor}\nHealth: {self.health}")
        

class Imp(Monster):
    def __init__(self, name = "Imp"):
        super().__init__(name)
        self.strength = int(random() * 5)
        self.armor = 0
        self.health = int(random() * 4) + 6
        
class Goblin(Monster):
    def __init__(self, name = "Goblin"):
        super().__init__(name)
        self.strength = int(random() * 8)
        self.armor = 3
        self.health = int(random() * 4) + 8
        
class Orc(Monster):
    def __init__(self, name = "Orc"):
        super().__init__(name)
        self.strength = int(random() * 4) + 8
        self.armor = 6
        self.health = int(random() * 4) + 12
    