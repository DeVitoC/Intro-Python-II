# A class that defines the items that are in rooms and that players can pick up
from enum import Enum
from myEnums import *

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def on_take(self):
        print(f"You have picked up {self.name}")
        
    def on_drop(self):
        print(f"You have dropped {self.name}")
        
##################
# Lightsource Classes
##################
class Lightsource(Item):
    def __init__(self, name, description, duration):
        super().__init__(name, description)
        self.duration = duration
        self.isOn = False
        
    def on_drop(self):
        print("It's not wise to drop your source of light!")
        
class Torch(Lightsource):
    def __init__(self, name, description, duration = 20):
        super().__init__(name, description, duration)
        
class Lamp(Lightsource):
    def __init__(self, name, description, duration = 40):
        super().__init__(name, description, duration)
        
##################
# Armor Classes
##################
class Armor(Item):
    def __init__(self, name, description, armor_value):
        super().__init__(name, description)
        self.armor_value = armor_value
        
class Helmet(Armor):
    def __init__(self, name, description, armor_value):
        super().__init__(name, description, armor_value)
        self.slot = ArmorSlot.HEAD

class Chestpeice(Armor):
    def __init__(self, name, description, armor_value):
        super().__init__(name, description, armor_value)
        self.slot = ArmorSlot.CHEST
        
class Legguard(Armor):
    def __init__(self, name, description, armor_value):
        super().__init__(name, description, armor_value)
        self.slot = ArmorSlot.LEGS

class Ring(Armor):
    def __init__(self, name, description, armor_value = 0):
        super().__init__(name, description, armor_value)
        self.slot = ArmorSlot.FINGER

##################
# Treasure Classes
##################
class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value 
        
class Coins(Treasure):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
        
    def __str__(self):
        return f"{self.value} coins: {self.description}"
    
class Diamond(Treasure):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
        


##################
# Consumable Classes
##################
class Consumable(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        
    def use(self):
        print(f"You consumed the {self.name}")
        
class HealthPotion(Consumable):
    def __init__(self, name, description, amount_healed):
        super().__init__(name, description)
        self.amount_healed = amount_healed
        
    def use(self):
        return self.amount_healed

class StrengthPotion(Consumable):
    def __init__(self, name, description, bonus_strength, duration):
        super().__init__(name, description)
        self.bonus_strength = bonus_strength
        self.duration = duration
        self.effect = (bonus_strength, duration)
        
    def use(self):
        return self.effect
    
    
item_types = {
    0: ('Torch', 'a torch that can light up the darkness for 20 turns'),
    1: ('Lamp', 'a lamp that can light up the darkness for 40 turns'),
    2: ('Helmet', 'a helmet with minor defensive capabilities', 2),
    3: ('Helmet', 'a helmet with medium defensive capabilities', 4),
    4: ('Helmet', 'a helmet with major defensive capabilities', 8),
    5: ('Chestpeice', 'a Chestpeice with minor defensive capabilities', 4),
    6: ('Chestpeice', 'a Chestpeice with medium defensive capabilities', 8),
    7: ('Chestpeice', 'a Chestpeice with major defensive capabilities', 12),
    8: ('Legguard', 'a legguard with minor defensive capabilities', 4),
    9: ('Legguard', 'a legguard with medium defensive capabilities', 8),
    10: ('Legguard', 'a legguard with major defensive capabilities', 12),
    11: ('Ring', 'a ring with no defensive capabilities'),
    12: ('Coins', 'a pile of coins', 100),
    13: ('Diamond', 'a valuable diamond', 1000),
    14: ("Health Potion", "A potion that will restore health", 15),
    15: ("Strength Potion", "a potion that will boost strength for a time", 10, 10)
}