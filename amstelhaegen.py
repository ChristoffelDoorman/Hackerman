# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import classes
import random
import pdb

def drawBuilding(building, x, y):

	# add building to map
	ax1.add_patch(
	    patches.Rectangle(
	        (x, y),   			# (x,y)
	        24,    # length
	        24,     # width	# color
			linewidth = 1,
			edgecolor = 'r',
			facecolor = 'none'
	    )
	)

def overlap(building1, building2):
	overlap = True

	if (building1.left > building2.right or building2.left > building1.right
		or building1.bottom > building2.top or building2.bottom > building1.top):
		overlap = False

	return overlap

if __name__ == "__main__":
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')
	ax1.set_xlim(0,360)
	ax1.set_ylim(0,320)

	# fill building array with a house at a random point
	buildings = []
	xrandom = random.randint(0, 336)
	yrandom = random.randint(0, 296)
	buildings.append(classes.house(xrandom, yrandom))

	while len(buildings) < 60:
		xrandom = random.randint(0, 336)
		yrandom = random.randint(0, 296)
		house = classes.house(xrandom, yrandom)

		olap = True
		for building in buildings:
			olap = overlap(house, building)

			if olap:
				break

		if not olap:
			buildings.append(house)
			drawBuilding(house, house.left, house.bottom)
			#plt.pause(0.8)
	# for i in buildings
	# print overlap(buildings[0], buildings[1])
    #
	# 	for i in buildings:
	# 		overlap(buildings[building],  )
    #
	# 		while (overlap(building, building[building]) = True)
	# 		xrandom = random.randint(0, 170)
	# 		yrandom = random.randint(0, 150)
	# 		drawBuilding(classes.house, xrandom, yrandom, "red")
	# print buildings
    #
	# for i in range(5):
	# 	xrandom = random.randint(0, 170)
	# 	yrandom = random.randint(0, 150)
	# 	drawBuilding(classes.bungalow, xrandom, yrandom, "blue")
    #
	# for i in range(3):
	# 	xrandom = random.randint(0, 170)
	# 	yrandom = random.randint(0, 150)
	# 	drawBuilding(classes.maison, xrandom, yrandom, "green")
	fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')
