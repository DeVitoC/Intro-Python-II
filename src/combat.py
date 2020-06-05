from player import *
from monster import *
from random import random

class Combat:
    def fight(self, player, monster):
        print(f"Oh no, {player.name}! A {monster.name} has attacked you.")
        while True: 
            action = input('Would you like to "attack", "flee", "examine" monster, or "drink" a potion? ')
            
            if action == "attack":
                print("do an attack")
            elif action == "flee":
                print("attempt to flee")
            elif action == "examine":
                print("examine monster")
            elif action == "drink":
                print("drink a potion")
            else:
                print("that was not a valid response")
                continue 
            
            print("monster attacks here")
            break