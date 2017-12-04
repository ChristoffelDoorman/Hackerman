class House:
	name = 'house'
	length = 24
	width = 24
	price = 285000
	marginalValue = 1.03

	def __init__(self, x, y):
		# self.price = 285.000
		# self.marginalValue = 1.03
		# self.location = (x, y)
		self.left_bottom = [x, y]
		self.left_top = [x, y + 24]
		self.right_top = [x + 24, y + 24]
		self.right_bottom = [x + 24, y]


	def __repr__(self):
		return("x=%i, y=%i, type = house "%(self.left_bottom[0], self.left_bottom[1]))

	# Dit is nog cumulatief, en dat mag niet!
	def score(self, closest):
		self.freeSpace = closest
		value = 285000 * (1.03 ** self.freeSpace)
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
		self.left_top = [x, y + 26]
		self.right_top = [x + 21, y + 26]
		self.right_bottom = [x + 21, y]
		# self.score = 0


	def __repr__(self):
		return("x=%i, y=%i, type = bungalow "%(self.left_bottom[0], self.left_bottom[1]))


	def score(self, closest):
		self.freeSpace = closest
		value = 399000 * (1.04 ** self.freeSpace)
		self.value = value
		return value


class Maison:
	name = 'maison'
	length = 33
	width = 34
	price = 610000
	marginalValue = 1.06

	def __init__(self, x, y):
		self.left_bottom = [x, y]
		self.left_top = [x, y + 34]
		self.right_top = [x + 33, y + 34]
		self.right_bottom = [x + 33, y]

	def __repr__(self):
		return ("x=%i, y=%i, type = maison "%(self.left_bottom[0], self.left_bottom[1]))

	def score(self, closest):
		self.freeSpace = closest
		value = 610000 * (1.06 ** self.freeSpace)
		self.value = value
		return value
