from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    global n_to, s_to, e_to, w_to
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        item1 = Item("torch", "use this to light your way")
        self.items = [item1, "ring", "helmet"]
        
    def __str__(self):
        return f"{self.name}"
    
    def add_item(self, item):
        self.items.append(item)
        
    def print_items(self):
        items_string = ""
        for i in self.items:
            items_string += f"{i}\n"
        print(items_string)
        
    def item_picked_up(self, item):
        self.items.remove(item)