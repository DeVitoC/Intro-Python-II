from room import Room

class DungeonMap:
    def __init__(self):
        self.dungeon_map = """
        _______________________
        |        _______      |
        |   ____|       |     |
        |  |    |  |__  |     |
        |  |____   |    |     |
        |       |  |____|____ |
        |       |           | |
        |       |           | |
        |       |____  _____| |
        |           |  |      |
        |           |  |      |
        |           |  |      |
        |   ________|  |      |
        |   |       |  |      |
        |   |___  __   |      |
        |      |    |  |      |
        |      |  __ __|      |
        |      |    |         |
        |      |____|         |
        |                     |
        |_____________________|
        """
        
    def show_map(self, *args):
        print(self.dungeon_map)