SCREEN_WIDTH = 80

def displaylocation(loc):
	print(loc)
	print('=' * len(loc))
	
	# print the room's description
	print('\n'.join(textwrap.wrap(worldRooms[loc][DESC],SCREEN_WIDTH)))

	# print all the items on the ground
	if len(worldRooms[loc][GROUND]) > 0:
		print()
		for item in worldRooms[loc][GROUND]:
			print(worldItems[item][GROUNDDESC])

	# print all the exits
	extis =[]
	for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
			if direction in worldRooms[loc].keys():
				exits.append(direction.title())
	print()
	if showFullExits:
		for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
			if direction in worldRooms[location]:
				print('%s: %s' % (direction.title(), worldRooms[location][direction])
	else:
		print('Exits: %s' % ' '.join(exits))





