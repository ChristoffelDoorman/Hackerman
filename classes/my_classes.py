# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file contains the classes of the buildings, the water and a map class.

from helpers.helper_functions import closest_distance
import math

class House:
	name = 'house'
	price = 285000
	marginalValue = 1.03

	def __init__(self, x, y):
		self.length = 20
		self.width = 20
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# updates the corner values based on the left_bottom x and y
	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# calculates the score of building based on the closest distance
	def score(self, closest):
		self.freeSpace = closest
		value = 285000 + (285000 * 0.03 * math.floor(self.freeSpace / 2))
		self.value = value
		return value

	def __repr__(self):
		return("x=%i, y=%i, type = house "%(self.left_bottom[0], self.left_bottom[1]))

class Bungalow:
	name = 'bungalow'
	price = 399000
	marginalValue = 1.04

	def __init__(self, x, y):
		self.length = 21
		self.width = 26
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# updates the corner values based on the left_bottom x and y
	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# rotates the building by swapping the width and length, and then updating the corners
	def rotate(self):
		self.length, self.width = self.width, self.length
		self.update(self.left_bottom[0], self.left_bottom[1])

	# calculates the score of building based on the closest distance
	def score(self, closest):
		self.freeSpace = closest
		value = 399000 + (399000 * 0.04 * math.floor(self.freeSpace / 2))
		self.value = value
		return value

	def __repr__(self):
		return ("x=%i, y=%i, type = bungalow "%(self.left_bottom[0], self.left_bottom[1]))

class Maison:
	name = 'maison'
	price = 610000
	marginalValue = 1.06

	def __init__(self, x, y):
		self.length = 34
		self.width = 33
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# updates the corner values based on the left_bottom x and y
	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# rotates the building by swapping the width and length, and then updating the corners
	def rotate(self):
		self.length, self.width = self.width, self.length
		self.update(self.left_bottom[0], self.left_bottom[1])

	# calculates the score of building based on the closest distance
	def score(self, closest):
		self.freeSpace = closest
		value = 610000 + (610000 * 0.06 * math.floor(self.freeSpace / 2))
		self.value = value
		return value

	def __repr__(self):
		return ("x=%i, y=%i, type = maison "%(self.left_bottom[0], self.left_bottom[1]))

class Water:
	name = 'water'

	def __init__(self, x, y, width, length):
		self.width = width
		self.length = length
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def __repr__(self):
		return ("x=%i, y=%i, linksboven=%i, type = water "%(self.left_bottom[0], self.left_bottom[1], self.left_top[1]))

class Map:

	def __init__(self, width, height, water_type):
		self.width = width
		self.height = height
		self.buildings = []
		self.waters = []
		self.add_water(water_type)

	# calculates the score of the map by adding individual scores of buildings
	def score(self):
		total_value = 0
		for current_building in self.buildings:
			closest = closest_distance(current_building, self.buildings)
			total_value += current_building.score(closest)

		return total_value

	# adds water at init to the district based on the inputted water_type
	def add_water(self, water_type):

		if water_type == 0:
			water = Water(320, 360, 0, 0)
			self.waters.append(water)

		# one block of water in ratio of the map in the middle of the map
		elif water_type == 1:
			water = Water(100, 88.5, 161, 143)
			self.waters.append(water)

		# one water stroke in the middle of the map
		elif water_type == 2:
			water = Water(28, 122, 304, 76)
			self.waters.append(water)

		# two strokes of water parralel positioned at 1/4 of the length from the top and bottom
		elif water_type == 3:
			water1 = Water(72, 71, 215, 54)
			water2 = Water(72, 195, 215, 54)
			self.waters.extend((water1, water2))

		# two horizontal and two vertical strokes of water parralel positioned of one another
		elif water_type == 4:
		    water1 = Water(104, 40, 151.789, 37.947)
		    self.waters.append(water1)
		    water2 = Water(104, 243, 151.789, 37.947)
		    self.waters.append(water2)
		    water3 = Water(50, 89, 40.232, 143.045)
		    self.waters.append(water3)
		    water4 = Water(270, 89, 40.232, 143.045)
		    self.waters.append(water4)

		# four rectangles in the ratio of the canvas inside the corners of the map
		elif water_type == 5:
		    water1 = Water(66, 59, 81, 72)
		    self.waters.append(water1)
		    water2 = Water(66, 189, 81, 72)
		    self.waters.append(water2)
		    water3 = Water(213, 59, 81, 72)
		    self.waters.append(water3)
		    water4 = Water(213, 189, 81, 72)
		    self.waters.append(water4)

		else:
			water = Water(320, 360, 0, 0)
			self.waters.append(water)
