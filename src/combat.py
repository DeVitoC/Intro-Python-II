from player import *
from monster import *
from random import random


class Combat:
	def fight(self, player_, monster_: Monster):
		print(f"Oh no, {player_.name}! A {monster_.name} has attacked you.")

		while True:
			action = input('Would you like to "attack", "flee", "examine" monster, or "drink" a potion? ')

			if action == "attack":
				did_win = self.attack(player_, monster_)
				if did_win:
					player_.current_room.monster = None
					player_.experience += player_.current_room.monster.experience_worth
					print(f"You have gained {player_.current_room.monster.experience_worth} experience.")
					return did_win
			elif action == "flee":
				if random() > 0.5:
					print("Sucessfully fled the monster.")
					return True
				else:
					print("You didn't get away before the monster could attack.")
					did_win: bool = self.attack(monster_, player_)
					return not did_win
			elif action == "examine":
				monster_.view_stats()
				continue
			elif action == "drink":
				self.drink_potion(player_)
				continue
			else:
				print("that was not a valid response")
				continue

			did_win = self.attack(monster_, player_)
			if did_win:
				return not did_win

	def attack(self, attacker, defender):
		print(defender.health)
		attack_strength = attacker.strength
		defender_defense = defender.armor
		if random() > 0.15 and attack_strength > defender_defense:
			attack = attack_strength - defender_defense
			defender.health -= attack
			print(f"The attack was successful! {defender.name} loses {attack} health")
			print(defender.health)
		else:
			print(f"{attacker.name}'s attack failed to damage {defender.name}.")
			print(defender.health)
			return False
		if defender.health <= 0:
			print(f"{defender.name} has been killed.")
			return True
		return False

	def drink_potion(self, player_):
		if "Health Potion" and "Strength Potion" in player_.inventory:
			response = input('Would you like to use your "Health" Potion or "Strength" Potion or "Cancel"? ')
		elif "Health Potion" in player_.inventory:
			response = self.should_use_potion(player_, "Health Potion")
		elif "Strength Potion" in player_.inventory:
			response = self.should_use_potion(player_, "Strength Potion")
		else:
			print("You do not have any potions.")
			return

		if response == "Health Potion" and (player_.max_health - player_.health <= 15):
			print(
				f"You used a Health Potion for {player_.max_health - player_.health}.\nYour health is now {player_.health}")
			player_.health = player_.max_health
		elif response == "Health Potion" and player_.max_health == player_.health > 15:
			player_.health += 15
			print(f"You used a Health Potion for 15 health points.\nYour health is now {player_.health}")
		elif response == "Strength Potion":
			print("You used a Strength Potion.")
			player_.strength += 10
		elif response == "Cancel":
			return

	def should_use_potion(self, player_, potion):
		while True:
			yes_no = input('Would you like to use your {potion} ("y"/"n")')
			if yes_no == "y":
				return potion
				break
			elif yes_no == "n":
				return "Cancel"
				break
			else:
				print("That wasn't a valid answer")
