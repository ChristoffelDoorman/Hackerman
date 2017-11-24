class house:
	length = 24
	width = 24

	def __init__(self, x, y):
		# self.price = 285.000
		# self.marginalValue = 1.03
		# self.location = (x, y)
		self.left_bottom = [x, y]
		self.left_top = [x, y + 24]
		self.right_top = [x + 24, y + 24]
		self.right_bottom = [x + 24, y]

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
		self.left_bottom = [x, y]
		self.left_top = [x, y + 26]
		self.right_top = [x + 21, y + 26]
		self.right_bottom = [x + 21, y]

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
		self.left_bottom = [x, y]
		self.left_top = [x, y + 34]
		self.right_top = [x + 33, y + 34]
		self.right_bottom = [x + 33, y]
    #
	# def value(self, distanceNeighbour):
	# 	self.freeSpace = distanceNeighbour
	# 	value = price * marginalValue * self.freespace
