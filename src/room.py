from item import *
from random import random, choice
from myEnums import *
from monster import *


# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	global n_to, s_to, e_to, w_to

	def __init__(self, name, description, length, width):
		self.name: str = name
		self.description: str = description
		self.items = self.populate_items()
		self.length = length
		self.width = width
		self.monster = self.random_monster()

	def populate_items(self):
		temp_dict: Dict[str : Item] = {}
		rand_num = int(round(random() * 3))
		for i in range(rand_num):
			name, item = choice(list(item_types.items()))
			new_item = self.create_item(item)
			temp_dict[new_item.name] = new_item
		return temp_dict

	def random_monster(self):
		is_monster: bool = random() < 0.5
		if is_monster:
			monster_string = choice([Imp, Goblin, Orc])
			return monster_string()
		else:
			return None

	def __str__(self):
		return f"{self.name}"

	def add_item(self, item):
		self.items[item.name] = item

	def print_items(self, *args):
		items_string: str = ""
		for i in self.items:
			items_string += f"{i}\n"
		print(items_string)

	def item_picked_up(self, item):
		removed_item = self.items.pop(item)
		removed_item.on_take()

	def create_item(self, description_tuple):
		item_definitions = {
			"Torch"          : Torch,
			"Lamp"           : Lamp,
			"Helmet"         : Helmet,
			"Chestpeice"     : Chestpeice,
			"Legguard"       : Legguard,
			"Ring"           : Ring,
			"Coins"          : Coins,
			"Diamond"        : Diamond,
			"Health Potion"  : HealthPotion,
			"Strength Potion": StrengthPotion
		}

		search_item = description_tuple[0]
		this_item_type = item_definitions[search_item]
		if len(description_tuple) == 2:
			this_item = this_item_type(description_tuple[0], description_tuple[1])
		elif len(description_tuple) == 3:
			this_item = this_item_type(description_tuple[0], description_tuple[1], description_tuple[2])
		elif len(description_tuple) == 4:
			this_item = this_item_type(description_tuple[0], description_tuple[1], description_tuple[2],
			                           description_tuple[3])
		return this_item
