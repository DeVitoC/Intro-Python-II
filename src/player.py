# Write a class to hold player information, e.g. what room they are in
# currently.
# from random import random
from item import *
from room import Room
from monster import *
from combat import Combat


class Player():

	def __init__(self, name: str, current_room: Room):
		self.name: str = name
		self.current_room: Room = current_room
		self.inventory = {}
		self.equipped_armor = {}
		self.level: int = 1
		self.strength: int = 0
		self.wisdom: int = 0
		self.armor: int = 0
		self.health: int = 0
		self.max_health: int = self.health
		self.experience = 0


	def move(self, action: str, direction: str):
		if direction[0] == "N":
			try:
				self.current_room = self.current_room.n_to
			except:
				print("There is no room to the north")
		elif direction[0] == "S":
			try:
				self.current_room = self.current_room.s_to
			except:
				print("There is no room to the south")
		elif direction[0] == "E":
			try:
				self.current_room = self.current_room.e_to
			except:
				print("There is no room to the east")
		elif direction[0] == "W":
			try:
				self.current_room = self.current_room.w_to
			except:
				print("There is no room to the west")
		self.look_for_monster()

	def pickup_item(self, action: str, what: str):
		if what in self.current_room.items:
			self.inventory[what] = self.current_room.items[what]
			self.current_room.item_picked_up(what)
		else:
			print("That is not one of the items in this room.")

	def look_for_monster(self):
		if self.current_room.monster == None:
			return
		else:
			monster: Monster = self.current_room.monster
			new_combat = Combat()
			new_combat.fight(self, monster)

	def drop_item(self, action, what):
		if what in self.inventory:
			self.current_room.add_item(self.inventory[what])
			dropped_item = self.inventory.pop(what)
			dropped_item.on_drop()

	def __str__(self):
		return f"{self.name}"

	def view_inventory(self, *args):
		print("You are currently carrying: ")
		for i in self.inventory:
			print(i)

	def equip(self, action, armor):
		if armor not in self.inventory:
			return
		elif armor in self.equipped_armor and armor in self.inventory:
			response = input(f"Do you want to replace your current {armor}? 'y' or 'n'? ")
			if response == 'y':
				temp_armor = self.equipped_armor.pop(armor)
				self.equipped_armor[armor] = self.inventory[armor]
				self.inventory[armor] = temp_armor
				self.armor += self.equipped_armor[armor].armor_value - temp_armor.armor_value
			else:
				return
		else:
			self.equipped_armor[armor] = self.inventory.pop(armor)
			self.armor += self.equipped_armor[armor].armor_value

	def print_equipped_armor(self, *args):
		for i in self.equipped_armor:
			print(f"{i}: {self.equipped_armor[i].description}")

	def view_stats(self, *args):
		print(f"Strength: {self.strength}\nWisdom: {self.wisdom}\nArmor: {self.armor}\nMax Health: {self.max_health}\nHealth: {self.health}")


class Warrior(Player):
	def __init__(self,name: str, current_room: Room):
		super().__init__(name, current_room)
		self.strength: int = int(random() * 4) + 6
		self.wisdom: int = 2
		self.armor: int = 0
		self.health: int = int(random() * 4) + 10
		self.max_health: int = self.health

class Mage(Player):
	def __init__(self, name: str, current_room: Room):
		super().__init__(name, current_room)
		self.strength: int = 2
		self.wisdom: int = int(random() *4) + 8
		self.armor: int = 0
		self.health: int = int(random() * 3) + 8
		self.max_health: int = self.health

class Paladin(Player):
	def __init__(self, name: str, current_room: Room):
		super().__init__(name, current_room)
		self.strength: int = int(random() *2) + 3
		self.wisdom: int = int(random() *2) + 3
		self.armor: int = 0
		self.health: int = int(random() * 5) + 9
		self.max_health: int = self.health

class Thief(Player):
	def __init__(self, name: str, current_room: Room):
		super().__init__(name, current_room)
		self.strength: int = int(random() *3) + 10
		self.wisdom: int = 2
		self.armor: int = 0
		self.health: int = int(random() * 3) + 8
		self.max_health: int = self.health