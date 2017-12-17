# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file contains the classes of the buildings, the water and a map class.

import helpers

class House:
	name = 'house'
	price = 285000
	marginalValue = 1.03

	def __init__(self, x, y):
		# self.price = 285.000
		# self.marginalValue = 1.03
		# self.location = (x, y)
		self.length = 20
		self.width = 20
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def __repr__(self):
		return("x=%i, y=%i, type = house "%(self.left_bottom[0], self.left_bottom[1]))

	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	# Dit is nog cumulatief, en dat mag niet!
	def score(self, closest):
		self.freeSpace = closest
		value = 285000 + (285000 * 0.03 * (self.freeSpace / 2))
		self.value = value
		return value


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
		# self.score = 0

	def top_right(self):
		return [self.x+self.width, self.y+self.length]

	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def rotate(self):
		self.length, self.width = self.width, self.length
		self.update(self.left_bottom[0], self.left_bottom[1])

	def __repr__(self):
		return ("x=%i, y=%i, width=%i, length=%i, type = bungalow "%(self.left_bottom[0], self.left_bottom[1], self.width, self.length))

	def score(self, closest):
		self.freeSpace = closest
		value = 399000 + (399000 * 0.04 * (self.freeSpace / 2))
		self.value = value
		return value


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

	def __repr__(self):
		return ("x=%i, y=%i, type = maison "%(self.left_bottom[0], self.left_bottom[1]))

	def update(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def rotate(self):
		self.length, self.width = self.width, self.length
		self.update(self.left_bottom[0], self.left_bottom[1])

	def score(self, closest):
		self.freeSpace = closest
		value = 610000 + (610000 * 0.06 * (self.freeSpace / 2))
		self.value = value
		return value


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
		return ("x=%i, y=%i, type = water "%(self.left_bottom[0], self.left_bottom[1]))

class Map:

	def __init__(self, width, height, water_type):
		self.width = width
		self.height = height
		self.buildings = []
		self.waters = []
		self.add_water(water_type)

	def score(self):
		total_value = 0
		for current_building in self.buildings:
			closest = helpers.closest_distance(current_building, self.buildings)
			total_value += current_building.score(closest)

		return total_value

	def add_water(self, water_type):

        # no water
		if water_type == 0:
			return

		# one water stroke in the middle of the map
		if water_type == 0:
			return

		if water_type == 1:
			water = Water(100, 88.5, 161, 143)
			self.waters.append(water)

		# two strokes of water parralel positioned at 1/4 of the length from the top and bottom
		elif water_type == 2:
			water1 = Water(70, 217.3, 220, 55)
			water2 = Water(70, 52.5, 220, 55)
			self.waters.extend((water1, water2))

		# two strokes of water parralel positioned at 1/3 of the length from the top and bottom
		elif water_type == 3:
			water1 = Water(x, y, width, length)
			water2 = Water(x, y, width, length)

		# four strokes of water parralel for x and parralel for y positioned at 1/4 of the respective width and length from the outside of the map
		elif water_type == 4:
			water1 = Water(x, y, width, length)
			water2 = Water(x, y, width, length)
			water3 = Water(x, y, width, length)
			water4 = Water(x, y, width, length)

		# four pooles of water positioned at 1/4 of diagonal to the inside of the corners of the map
		elif water_type == 5:
			water1 = Water(x, y, width, length)
			water2 = Water(x, y, width, length)
			water3 = Water(x, y, width, length)
			water4 = Water(x, y, width, length)
