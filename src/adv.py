from room import Room
from player import Player
from code import InteractiveConsole

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
    print("Welcome to Adventure Game. Have fun storming the castle!")
    
    name = input("Enter your name: ")
    adventurer = Player(name, room["outside"])
    
    while True:
        print(f"\nYou are in the {adventurer.current_room}")
        print(f"The items in this room are:")
        adventurer.current_room.print_items()
        inp = input('What would you like to do? Type "help" for possible commands: ')
        if inp == "help":
            print(help_list)
        elif inp == "n":
            # enter the room to the north
            adventurer.move("n")
        elif inp == "s":
            # enter the room to the south
            adventurer.move("s")
        elif inp == "e":
            # enter the room to the east
            adventurer.move("e")
        elif inp == "w":
            # enter the room to the west
            adventurer.move("w")
        elif inp == "p":
            while True:
                item_to_pickup = input("Which item would you like to pick up? (or 'q' to exit) ")
                if item_to_pickup in adventurer.current_room.items:
                    adventurer.pickup_item(item_to_pickup)
                    print(f"You've picked up the {item_to_pickup}")
                    break
                else:
                    print("That is not one of the items in this room.")
        elif inp == "q":
            print(f"Thanks for playing, {adventurer.name}! Come back soon.")
            break 
        
        
            
help_list = '''
Type:
"n to move to the room to the north
"s" to move to the room to the south
"e" to move to the room to the east
"w" to move to the room to the west
"p" to select an item to pick up
"q" to quit
"help" to see commands
'''


adventure_game()
