



class house:

	def __init__(self, x, y):
			length = 12
			width = 12
			price = 285.000
			marginalValue = 1.03
		self.location = (x, y)

	def score(self, distanceNeighbour):
		self.freeSpace = distanceNeighbour
		score = price * marginalValue * self.freespace


class bungalow:

	length = 10.5
	width = 13
	price = 399.000
	marginalValue = 1.04

	def __init__(self, x, y):
		self.location = (x, y)

	def score(self, distanceNeighbour):
		self.freeSpace = distanceNeighbour
		value = price * marginalValue * self.freespace


class maison:

	length = 16.5
	width = 17
	price = 610000
	marginalValue = 1.06

	def __init__(self, x, y):
		self.location = (x, y)
		self.length = 16.5
		self.width = 17
		self.price = 610000
		self.marginalValue = 1.06

	def value(self, distanceNeighbour):
		self.freeSpace = distanceNeighbour
		value = price * marginalValue * self.freespace
