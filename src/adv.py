from room import *
from player import *
from item import *
from dungeon_map import *

# Declare all the rooms

room = {
	'outside'       : Room("Outside Cave Entrance", """North of you, the cave mount beckons""", 2, 2),
	'foyer'         : Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", 2,
	                       2),
	'overlook'      : Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
                     Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", 2,
	                       4),
	'narrow'        : Room("Narrow Passage",
	                       """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
	                       1, 8),
	'treasure'      : Room("Treasure Chamber",
	                       """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
	                       3, 6),
	# newly added rooms
	'secret passage': Room("Secret Passageway",
	                       """You've discovered a secret passage under the mountain at the back of the treasure chamber!""",
	                       1, 4),
	'bunker'        : Room("Bunker", "You've entered a room that seems to ahve once been a hidden military room", 2, 2),
	'north hideout' : Room("North Hideout",
	                       "This room seems to have once been a room where this family could hide in times of danger.",
	                       2, 2),
	'south hideout' : Room("South Hideout",
	                       "This room is the south half of the secret hideout. This side seemed to be where the family would sleep.",
	                       2, 2)
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

# New room collections
room['treasure'].n_to = room['secret passage']
room['secret passage'].w_to = room['bunker']
room['secret passage'].e_to = room['north hideout']
room['secret passage'].s_to = room['treasure']
room['bunker'].e_to = room['secret passage']
room['north hideout'].w_to = room['secret passage']
room['north hideout'].s_to = room['south hideout']
room['south hideout'].n_to = room['north hideout']

# Add Lightsource
torch: Torch = Torch('Torch', 'a torch that can light up the darkness for 20 turns')
room['foyer'].add_item(torch)

# Add Map
dungeon_map: DungeonMap = DungeonMap()


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
		print(f"{adventurer.current_room.description}")
		inp: str = input('What would you like to do? Type "help" for possible commands: ')
		commands = inp.split(" ")
		if len(commands) > 2:
			action: str = commands[0].lower()
			what: str = f"{commands[1].capitalize()} {commands[2].capitalize()}"
		if len(commands) == 2:
			action: str = commands[0].lower()
			what: str = commands[1].capitalize()
		elif len(commands) == 1:
			action: str = commands[0].lower()
			what: str = commands[0].capitalize()
		else:
			print("You didn't enter a command.")

		if action.lower() == "q":
			print(f"Thanks for playing, {adventurer}! Come back soon.")
			break
		else:
			take_action(action, what)
			if adventurer.health <= 0:
				print(f"Thanks for playing, {adventurer}! Try again.")
				break


def print_help(*inp):
	help_list = '''
    Type:
    "move north"         to move to the room to the north
    "move south"         to move to the room to the south
    "move east"          to move to the room to the east
    "move west"          to move to the room to the west
    "take *item*" or "get *item* to select an item to pick up
    "drop *item*"        to drop an item from your inventory
    "equip *armor*"      to equip a peice of armor from your inventory
    "view"               to view stats
    "i" or "inventory"   to view inventory
    "equipped"           to view equipped armor
    "search"             to search the room for items
    "map"                to view dungeon map
    "q" or "quit"        to quit
    "help"               to see commands
    '''
	print(help_list)


def take_action(action: str, what: str):
	actions = {
		"help"     : print_help,
		"move"     : adventurer.move,
		"take"     : adventurer.pickup_item,
		"get"      : adventurer.pickup_item,
		"drop"     : adventurer.drop_item,
		"equip"    : adventurer.equip,
		"equipped" : adventurer.print_equipped_armor,
		"view"     : adventurer.view_stats,
		"search"   : adventurer.current_room.print_items,
		"map"      : dungeon_map.show_map,
		"i"        : adventurer.view_inventory,
		"inventory": adventurer.view_inventory,
	}

	if action in actions:
		this_action = actions[action]
		return this_action(action, what)
	else:
		print("That was not a valid command. Please try again.")


name: str = input("Enter your name: ")
while True:
	player_class = input('"w" for Warrior\n"m" for Mage\n"p" for Paladin\n"t" for Thief\nWhat class would you like to play? ')
	if player_class == "w":
		adventurer = Warrior(name, room['outside'])
		break
	elif player_class == "m":
		adventurer = Mage(name, room['outside'])
		break
	elif player_class == "p":
		adventurer = Paladin(name, room['outside'])
		break
	elif player_class == "t":
		adventurer = Thief(name, room['outside'])
		break
	else:
		print("That was not a valid option.")

adventure_game()
