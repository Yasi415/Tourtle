# change the player's location
def moveDirection(direction):

	global location

	if direction in worldRooms[location]:
		print('You move to the %s' % direction)
		location = worldRooms[location][direction]
		displayLocation(location)
	else:
		print('You cannot move in that direction')

# go to the area to the north, if possible
def do_north(self, arg):
	moveDirection('north')

# go to the area to the south, if possible
def do_south(self, arg):
	moveDirection('south')

# go to the area to the east, if possible
def do_east(self, arg):
	moveDirection('east')

# go to the area to the west, if possible
def do_west(self, arg):
	moveDirection('west')

# go to the area upwards, if possible
def do_up(self, arg):
	moveDirection('up')

# go to the area downwards, if possible
def do_down(self, arg):
	moveDirection('down')

do_n = do_north
do_s = do_south
do_e = do_east
do_w = do_west
do_u = do_up
do_d = do_down



