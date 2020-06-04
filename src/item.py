# A class that defines the items that are in rooms and that players can pick up

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name}"
    
    def on_take(self):
        print(f"You have picked up {self.name}")
        
    def on_drop(self):
        print(f"You have picekd up {self.name}")