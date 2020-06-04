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
        self.str = int(random() * 10)
        
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
            #item_number = self.inventory.index(what)
            #inventory[item_number].on_take()
            #print(f"You've picked up the {what}")
        else:
            print("That is not one of the items in this room.")
        
    def drop_item(self, action, what):
        if what in self.inventory:
            self.current_room.add_item(self.inventory[what])
            dropped_item = self.inventory.pop(what)
            dropped_item.on_drop()
        
    def __str__(self):
        return f"{self.name}"
    
    def view_inventory(self, *inp):
        print("You are currently carrying: ")
        for i in self.inventory:
            print(i)