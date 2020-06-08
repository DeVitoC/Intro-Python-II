import turtle as t


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
		# print(self.dungeon_map)
		map = self.draw_map()
		stop = input("Press enter to exit map. ")

	def draw_map(self):
		t.speed(speed = 10)
		t.pu()
		t.setpos(0, -250)
		t.pd()
		t.fd(50)
		t.lt(90)
		t.fd(50)
		t.lt(90)
		t.fd(20)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(20)
		t.lt(90)
		t.fd(50)
		t.lt(90)

		t.pu()
		t.setpos(50, -200)
		t.pd()
		t.lt(90)
		t.fd(10)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(30)
		t.lt(90)
		t.fd(20)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(20)
		t.lt(90)
		t.fd(50)

		t.pu()
		t.setpos(50, -150)
		t.pd()
		t.lt(180)
		t.fd(50)
		t.lt(90)
		t.fd(75)
		t.lt(90)
		t.fd(50)
		t.lt(90)
		t.fd(25)

		t.pu()
		t.setpos(50, -200)
		t.pd()
		t.fd(25)
		t.lt(90)
		t.fd(200)
		t.lt(90)
		t.fd(7)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(8)
		t.lt(90)
		t.fd(100)

		t.pu()
		t.setpos(75, 0)
		t.pd()
		t.lt(90)
		t.fd(25)
		t.lt(90)
		t.fd(75)
		t.lt(90)
		t.fd(132)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(8)
		t.lt(90)
		t.fd(75)
		t.lt(90)
		t.fd(100)

		t.pu()
		t.setpos(25, 75)
		t.pd()
		# t.fd(25)
		t.lt(90)
		t.fd(100)
		t.lt(90)
		t.fd(75)
		t.lt(90)
		t.fd(45)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(45)

		t.pu()
		t.setpos(-50, 150)
		t.pd()
		t.rt(90)
		t.fd(50)
		t.lt(90)
		t.fd(50)
		t.lt(90)
		t.fd(50)

		t.pu()
		t.setpos(-25, 175)
		t.pd()
		t.rt(90)
		t.fd(10)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(80)

		t.pu()
		t.setpos(-25, 125)
		t.pd()
		t.lt(90)
		t.fd(30)
		t.pu()
		t.fd(10)
		t.pd()
		t.fd(10)

		t.hideturtle()