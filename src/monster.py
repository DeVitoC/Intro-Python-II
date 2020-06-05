from random import random
class Monster:
    
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.strength = 0
        self.armor = 0
        self.health = 0
        

class Imp(Monster):
    def __init__(self, name, room):
        super().__init__(name, room)
        self.strength = int(random() * 5)
        self.armor = 0
        self.health = int(random() * 4) + 6
        
class Goblin(Monster):
    def __init__(self, name, room):
        super().__init__(name, room)
        self.strength = int(random() * 8)
        self.armor = 3
        self.health = int(random() * 4) + 8
        
class Orc(Monster):
    def __init__(self, name, room):
        super().__init__(name, room)
        self.strength = int(random() * 4) + 8
        self.armor = 6
        self.health = int(random() * 4) + 12
    