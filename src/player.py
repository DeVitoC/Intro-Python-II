# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        
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