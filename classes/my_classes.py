class House:
	name = 'house'
	length = 20
	width = 20
	price = 285000
	marginalValue = 1.03

	def __init__(self, x, y):
		# self.price = 285.000
		# self.marginalValue = 1.03
		# self.location = (x, y)
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
	length = 21
	width = 26
	price = 399000
	marginalValue = 1.04

	def __init__(self, x, y):
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

	def __repr__(self):
		return ("x=%i, y=%i, type = bungalow "%(self.left_bottom[0], self.left_bottom[1]))

	def score(self, closest):
		self.freeSpace = closest
		value = 399000 + (399000 * 0.04 * (self.freeSpace / 2))
		self.value = value
		return value


	def rotate():

		inheretence


class Maison:
	name = 'maison'
	length = 34
	width = 33
	price = 610000
	marginalValue = 1.06

	def __init__(self, x, y):
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

	def score(self, closest):
		self.freeSpace = closest
		value = 610000 + (610000 * 0.06 * (self.freeSpace / 2))
		self.value = value
		return value


class Water:
	name = 'water'

	def __init__(self, x, y, length, width):
		self.length = length
		self.width = width
		self.left_bottom = [x, y]
		self.left_top = [x, y + self.length]
		self.right_top = [x + self.width, y + self.length]
		self.right_bottom = [x + self.width, y]

	def __repr__(self):
		return("x=%i, y=%i, type = water, length=%i, width=%i, linksonder=%i, rechtsboven=%i "%(self.left_bottom[0], self.left_bottom[1], self.length, self.width, self.left_bottom[0], self.right_top[0]))

import helpers

class Map:

	#buildings = []

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.buildings = []

	def score(self):
		total_value = 0
		for current_building in self.buildings:
			closest = helpers.closest_distance(current_building, self.buildings)
			total_value += current_building.score(closest)

		return total_value

	# def score(self):
	# 	total_value = 0
    #
	# 	for current_building in self.buildings:
	# 		print current_building
	# 		closest = closest_distance(current_building, self.buildings)
	# 		total_value += current_building.score(closest)
    #
	# 	return total_value
