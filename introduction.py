import textwrap

from time import *
from random import *
import os,sys

def clear_screen():
	os.system('cls' if os.name=='nt' else 'clear')


def title():
	print "(----------------------------------------------------)"
	print "(   ___________                 __    _              )"
	print "(  /____  ____/_____  _________|  |__| | ___         )"
	print "(      / / /  _  \||  |||  __|__   __| |/ _ \        )"
	print "(     / / |  |_|  ||  ||| |    |  |  | |   __        )"
	print "(    /_/   \_____/||__|||_|    |__|  |_|\___/        )"
	print "(                                                    )"
	print "(----------------------------------------------------)"

print title()

global player_name
global response


def player():
	return raw_input("What is your name? ")

player_name = raw_input("What is you name? ")

print "					"

def welcome(player_name):
	return "Welcome to San Francisco %s!" %(player_name)

print welcome(player_name)

print "					"

sleep(2)

print "					"
print "Before we begin exploring this wonderful city there are just a few things we need to review."
print "					"

sleep(5)

print "The first and most important question is this..."
print "								"
sleep(3)

def let_us_begin1():
	print "								"
	return raw_input("Are you ready to go on an adventure? Type yes or no: ")

reply = raw_input("Are you ready to go on an adventure? Type yes or no: ")

print "				"

if reply == 'yes':
	print "Wonderful! A city unlike any other awaits us..."
	sleep(3)

elif reply == 'no':
	print "Uh oh...Go grab some hot cocoa and come back when you're in a better mood"
	sleep(3)
else:
	print "You seem a little confused..."
	sleep(3)

print "						"



# TEMPORARY CODE:
# while True:
#     displayLocation(location)
#     response = input()
#     if response == 'quit':
#         break
#     if response in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
#         moveDirection(response)

