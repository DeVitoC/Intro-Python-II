from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def adventure_game():
    print(f"Welcome to Adventure Game, {adventurer}. Have fun storming the castle!")
    
    while True:
        print(f"\nYou are in the {adventurer.current_room}")
        print(f"The items in this room are:")
        adventurer.current_room.print_items()
        inp = input('What would you like to do? Type "help" for possible commands: ') 
        commands = inp.split(" ")
        if len(commands) > 1:
            action = commands[0]
            what = commands[1]
        elif len(commands) == 1:
            action = commands[0]
            what = commands[0]
        else:
            print("You didn't enter a command.")
        
        if inp[0] == "q":
            print(f"Thanks for playing, {adventurer}! Come back soon.")
            break 
        else:
            take_action(action, what) 

def print_help(*inp):       
    help_list = '''
    Type:
    "move north" to move to the room to the north
    "move south" to move to the room to the south
    "move east" to move to the room to the east
    "move west" to move to the room to the west
    "take *item*" or "get *item* to select an item to pick up
    "drop *item*" to drop an item from your inventory
    "i" or "inventory" to view inventory
    "q" or "quit" to quit
    "help" to see commands
    '''
    print(help_list)

def take_action(action, what):
    actions = {
        "help": print_help,
        "move": adventurer.move,
        "take": adventurer.pickup_item,
        "get": adventurer.pickup_item,
        "drop": adventurer.drop_item,
        "i": adventurer.view_inventory,
        "inventory": adventurer.view_inventory,
    }
    
    if action in actions:
        this_action = actions[action]
        return this_action(action, what)
    else:
        print("That was not a valid command. Please try again.")
    
# def pickup_item(action, what):
#     if what in adventurer.current_room.items:
#         adventurer.pickup_item(what)
#         print(f"You've picked up the {what}")
#     else:
#         print("That is not one of the items in this room.")

name = input("Enter your name: ")
adventurer = Player(name, room["outside"])

adventure_game()
