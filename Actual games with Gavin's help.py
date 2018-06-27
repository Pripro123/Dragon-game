print ("You wake up and find yourself trapped alone on an island")

print()

print("You must escape and find supplies in order to escape before it is too late")

print()

print ("You have nothing but a map and must decide where to explore before it reaches dark or else...")

#!/usr/bin/env python

import json

class Adventure:

	def __init__(self):
		playerlocation = [ 0, 0 ]
		matrix = self.loadmap()
		self.input_loop(matrix, playerlocation)

	def loadmap(self):
		with open('map.json') as json_file:  
			return json.load(json_file)

	def printlocation(self, matrix, playerlocation):
		print(f"You are at: {matrix[playerlocation[0]][playerlocation[1]]}")

	def valid_commands(self, matrix, playerlocation):
		commands = []
		height = len(matrix) - 1
		width = len(matrix[0]) - 1
		if playerlocation[0] != 0:
			commands.append("north")
		if playerlocation[0] != height:
			commands.append("south")
		if playerlocation[1] != 0:
			commands.append("west")
		if playerlocation[1] != width:
			commands.append("east")

		commands.append("quit")
		print(f"Valid commands are {', '.join(commands)}")
		return commands

	def processinput(self, command, directions, quit, playerlocation):
		if command == "quit":
			print("Thanks for playing... See you next time!")
			quit()

		if command in directions:
			if command == "north":
				playerlocation[0] = playerlocation[0] - 1
			if command == "south":
				playerlocation[0] = playerlocation[0] + 1
			if command == "east":
				playerlocation[1] = playerlocation[1] + 1
			if command == "west":
				playerlocation[1] = playerlocation[1] - 1


	def input_loop(self, matrix, playerlocation):
		while [ True ]:
			print(quit)
			self.printlocation(matrix, playerlocation)
			directions = self.valid_commands(matrix, playerlocation)
			command = input("You know that you are alone and need to escape. Where to go next?")
			self.processinput(command, directions, quit, playerlocation)


	def input_loop(self, matrix, playerlocation):
		while [ True ]:
			print(quit)
			self.printlocation(matrix, playerlocation)
			directions = self.valid_commands(matrix, playerlocation)
			command = input("Where would you like to go?")
			self.processinput(command, directions, quit, playerlocation)		


Adventure()
