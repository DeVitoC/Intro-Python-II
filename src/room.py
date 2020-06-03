# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    global n_to, s_to, e_to, w_to 
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name}"