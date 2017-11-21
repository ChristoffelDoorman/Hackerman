class house:
	length = 24
	width = 24
	def __init__(self, x, y):
		# self.price = 285.000
		# self.marginalValue = 1.03
		# self.location = (x, y)
		self.left = x
		self.right = x + 24
		self.bottom = y
		self.top = y + 24

	# def __str__(self):
	# 	# return
    #
	# def score(self, distanceNeighbour):
	# 	self.freeSpace = distanceNeighbour
	# 	score = price * marginalValue * self.freespace


class bungalow:
	length = 21
	width = 26
	# price = 399.000
	# marginalValue = 1.04

	def __init__(self, x, y):
		self.left = x
		self.right = x + 21
		self.bottom = y
		self.top = y + 26
    #
	# def score(self, distanceNeighbour):
	# 	self.freeSpace = distanceNeighbour
	# 	value = price * marginalValue * self.freespace
    #

class maison:
	length = 33
	width = 34
	# price = 610.000
	# marginalValue = 1.06

	def __init__(self, x, y):
		self.left = x
		self.right = x + 33
		self.bottom = y
		self.top = y + 34
    #
	# def value(self, distanceNeighbour):
	# 	self.freeSpace = distanceNeighbour
	# 	value = price * marginalValue * self.freespace
