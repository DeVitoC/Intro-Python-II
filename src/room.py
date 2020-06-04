from item import *
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    global n_to, s_to, e_to, w_to
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        item1 = Torch("torch", "use this to light your way")
        item2 = Ring("ring", "a shiny, unenchanted ring with no special properties")
        item3 = Helmet("helmet", "a helmet with some minor defensive bonuses", 2)
        self.items = {item1.name: item1, item2.name: item2, item3.name: item3}
        
    def __str__(self):
        return f"{self.name}"
    
    def add_item(self, item):
        self.items[item.name] = item
        
    def print_items(self):
        items_string = ""
        for i in self.items:
            items_string += f"{i}\n"
        print(items_string)
        
    def item_picked_up(self, item):
        removed_item = self.items.pop(item)
        removed_item.on_take()