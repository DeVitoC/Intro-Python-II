# Write a class to hold player information, e.g. what room they are in
# currently.
from random import random

from item import *

class Player:
    
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = {}
        self.level = 1
        self.strength = int(random() * 10)
        self.armor = 0
        self.health = int(random() * 3) + 7
        self.equipped_armor = {}
        
    def move(self, action, direction):
        if direction[0] == "n":
            try:
                self.current_room = self.current_room.n_to
            except:
                print("There is no room to the north")
        elif direction[0] == "s":
            try:
                self.current_room = self.current_room.s_to
            except:
                print("There is no room to the south")
        elif direction[0] == "e":
            try:
                self.current_room = self.current_room.e_to
            except:
                print("There is no room to the east")
        elif direction[0] == "w":
            try:
                self.current_room = self.current_room.w_to
            except:
                print("There is no room to the west")
                
    def pickup_item(self, action, what):
        if what in self.current_room.items:
            self.inventory[what] = self.current_room.items[what]
            self.current_room.item_picked_up(what)
        else:
            print("That is not one of the items in this room.")
        
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
                temp_armor = self.euipped_armor.pop(what)
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
        print(f"Strength: {self.strength}\nArmor: {self.armor}\nHealth: {self.health}")