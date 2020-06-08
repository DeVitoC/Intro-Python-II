from random import random


class Monster:

	def __init__(self, name: str):
		self.name: str = name
		self.strength: int = 0
		self.armor: int = 0
		self.health: int= 0
		self.experience_worth = 0

	def view_stats(self, *args):
		print(f"{self.name}:\nStrength: {self.strength}\nArmor: {self.armor}\nHealth: {self.health}")


class Imp(Monster):
	def __init__(self, name = "Imp"):
		super().__init__(name)
		self.strength = int(random() * 5)
		self.armor = 0
		self.health = int(random() * 4) + 6
		self.experience_worth = 10


class Goblin(Monster):
	def __init__(self, name = "Goblin"):
		super().__init__(name)
		self.strength = int(random() * 8)
		self.armor = 3
		self.health = int(random() * 4) + 8
		self.experience_worth = 20


class Orc(Monster):
	def __init__(self, name = "Orc"):
		super().__init__(name)
		self.strength = int(random() * 4) + 8
		self.armor = 6
		self.health = int(random() * 4) + 12
		self.experience_worth = 30
