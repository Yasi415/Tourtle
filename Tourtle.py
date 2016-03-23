import cmd # supprt for line-oriented command interpreters
import textwrap
SCREEN_WIDTH = 80

global player_name
global response

from time import *
from random import *
import os,sys
# sleep(2)

import worldRooms.py
import worldItems.py

DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
GROUNDDESC = 'grounddesc' # a short string that displays in the area's description
SHORTDESC = 'shortdesc' # a short string that will be used in sentences like, 'You look at x'
LONGDESC = 'longdesc' #displayed when player looks at item
TAKEABLE = 'takeable' # boolean value is True if player can pick up item and place it in inventory
DESCWORDS = 'descwords' # list of strings that can be used in the player's commands
TOURDESC = 'tourdesc' # provides more of a description of a room
MOREDESC = 'moredesc' # provides more of a description of an item


location = 'Embarcadero' # start at Embarcadero
showFullExits = True

#===============================================================#

while True:
	displayLocation(location)
	response = input()
	if response == 'quit':
		break
	if response in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
		moveDirection(response)

#===============================================================#
# DISPLAY LOCATION

def displaylocation(loc):
	
	# print the room name
	print loc
	print '=' * len(loc)
	
	# print the room's description
	print '\n'.join(textwrap.wrap(worldRooms[loc][DESC],SCREEN_WIDTH))

	
	# print all the items on the ground
	if len(worldRooms[loc][GROUND]) > 0:
		print
		for item in worldRooms[loc][GROUND]:
			print worldItems[item][GROUNDDESC]

	# print all the exits
	extis = []
	for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
			if direction in worldRooms[loc].keys():
				exits.append(direction.title())
	print '\n'
	if showFullExits:
		for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
			if direction in worldRooms[location]:
				print '%s: %s' % (direction.title(), worldRooms[location][direction])
	else:
		print 'Exits: %s ' % (exits.join())

#===============================================================#

# TOUR DESCRIPTION #

# print the room's 'tour' description

def tourtle(loc):
	Tourtle = raw_input("If you would like to learn more type 'tourtle'")
	if Tourtle == 'tourtle':
		print '\n'.join(textwrap.wrap(worldRooms[loc][TOURDESC],SCREEN_WIDTH))
	else:
		print 'Enjoy the rest of the tour!'
	

#===============================================================#

# LOOKING #

def do_look(self,arg):

	lookingAt = arg.lower()
	if lookingAt == '':
		# look will re-print the area description
		displayLocation(location)
		return
	if lookingAt == 'exits':
		for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
			if direction in worldRooms[location]:
				print '%s: %s' % (direction.title(), worldRooms[location][direction])
		return


	if lookingAt in ('north', 'west', 'east', 'south', 'up', 'down', 'n', 'w', 'e', 's', 'u', 'd'):
		if lookingAt.startswith('n') and NORTH in worldRooms[location]:
			print worldRooms[location][NORTH]
		elif lookingAt.startswith('w') and WEST in worldRooms[location]:
			print worldRooms[location][WEST]
		elif lookingAt.startswith('e') and EAST in worldRooms[location]:
			print worldRooms[location][EAST]
		elif lookingAt.startswith('s') and SOUTH in worldRooms[location]:
			print worldRooms[location][SOUTH]
		elif lookingAt.startswith('u') and UP in worldRooms[location]:
			print worldRooms [location][UP]
		elif lookingAt.startswith('d') and DOWN in worldRooms[location]:
			print worldRooms[location][DOWN]
		else:
			print 'There is nothing in that direction.'
		return


	# see if the item beig looked at is on the ground at current location
	item = getFirstItemMatchingDesc(lookingAt, worldRooms[location][GROUND])
	if item != None:
		print '\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH))
		return
	print 'You do not see that nearby.'


def complete_look(self, text, line, begidx, endix):
	possibleItems = []
	lookingAt = text.lower()

	groundDescWords = getAllDescWords(worldRooms[location][GROUND])
	moreDesc = getMoreDescWords(worldItems[item][MOREDESC])


	for descWord in groundDescWords + [NORTH, SOUTH, EAST, WEST, UP,DOWN]:
		if line.startswith('look %s' % (descWord)):
			return [] #command is complete
		elif line.startswith('learn more %s' % (descWord)):
			return moreDesc
			return []


	# only typing 'look' but no item name- show all items on ground and directions
	if lookingAt == '':
		possibleItems.extend(getAllFirstDescWords(worldRooms[location][GROUND]))
		for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
			if direction in worldRooms[location]:
				possibleItems.append(direction)
		return list(set(possibleItems)) #make list unique


	# get a list of all the "description words" for ground items matching the command text so far:
	for descWord in groundDescWords:
		if descWord.startswith(lookingAt):
			possibleItems.append(descWord)


	# get a list for all "description words" for items in district (if this is one):
	for descWord in districtDescWords:
		if descWord.startswith(lookingAt):
			possibleItems.append(descWord)


	# check for matching directions
	for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
		if direction.startswith(lookingAt):
			possibleItems.append(direction)

    # get a list of all "description words" for inventory items matching the command text so far:
	for descWord in invDescWords:
		if descWord.startswith(lookingAt):
			possibleItems.append(descWord)

	return list(set(possibleItems)) #make list unique

#===============================================================#
# MOVE DIRECTION #

# change the player's location
def moveDirection(direction):

	global location

	if direction in worldRooms[location]:
		print 'You move to the %s' % direction
		location = worldRooms[location][direction]
		displayLocation(location)
	else:
		print 'You cannot move in that direction'

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


#==============================================================#

# FORTUNE COOKIE FUNCTION #

def cookie(fortune):
	while GROUNDDESC == 'Makoto Hagiwara':
		cookie = raw_input("Would you like a fortune cookie?")
		if cookie == 'yes':
			import fortune.py
		else:
			break