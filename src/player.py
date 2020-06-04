# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        
    def move(self, direction):
        if direction == "n":
            try:
                self.current_room = self.current_room.n_to
            except:
                print("There is no room to the north")
        elif direction == "s":
            try:
                self.current_room = self.current_room.s_to
            except:
                print("There is no room to the south")
        elif direction == "e":
            try:
                self.current_room = self.current_room.e_to
            except:
                print("There is no room to the east")
        elif direction == "w":
            try:
                self.current_room = self.current_room.w_to
            except:
                print("There is no room to the west")
                
    def pickup_item(self, item):
        self.inventory.append(item)
        self.current_room.item_picked_up(item)
        
    def __str__(self):
        return string(self.name)
    
    def view_inventory(self):
        print("You are currently carrying: ")
        for i in self.inventory:
            print(i)