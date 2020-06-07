from player import *
from monster import *
from random import random

class Combat:
    def fight(self, player_, monster_):
        print(f"Oh no, {player_.name}! A {monster_.name} has attacked you.")
        while True: 
            action = input('Would you like to "attack", "flee", "examine" monster, or "drink" a potion? ')
            
            if action == "attack":
                did_survive = self.attack(player_, monster_)
                if not did_survive: return did_survive
            elif action == "flee":
                if random() > 0.5: 
                    print("Sucessfully fled the monster.") 
                    return True
                else: 
                    print("You didn't get away before the monster could attack.")
                    did_survive = self.attack(monster_, player_)
                    return did_survive
            elif action == "examine":
                monster_.view_stats()
            elif action == "drink":
                self.drink_potion(player_)
                        
                print("that was not a valid response")
                continue 
            
            print("monster attacks here")

        
    def attack(self, attacker, defender):
        print(defender.health)
        attack_strength = attacker.strength 
        defender_defense = defender.armor
        if random() > 0.15 and attack_strength > defender_defense:
            attack = attack_strength - defender_defense
            defender.health - attack
            print(f"The attack was successful! {defender.name} loses {attack} health")
            print(defender.health)
        else: 
            print(f"{attacker.name}'s attack failed to damage {defender.name}.") 
            print(defender.health)
            return True 
        if defender.health <= 0:
            print(f"{defender.name} has been killed.") 
            print(f"Defender is player {defender is Player}. ")
            if defender is Player:
                return False 
        return True
    
    def drink_potion(self, player_):
        if "Health Potion" and "Strength Potion" in player_.inventory:
            response = input('Would you like to use your "Health" Potion or "Strength" Potion or "Cancel"? ')
            if response == "Health" and (player_.max_health - player_.health <= 20):
                print(f"You used a Health Potion for {player_.max_health - player_.health}.\nYour health is now {player_.health}")
                player_.health = player_.max_health
            elif response == "Health" and player_.max_health == player_.health > 20:
                print(f"You used a Health Potion for 20 health points.\nYour health is now {player_.health}")
            elif response == "Strength":
                print("You used a Strength Potion.")
                player_.strength += 10
            elif response == "Cancel":
                return 