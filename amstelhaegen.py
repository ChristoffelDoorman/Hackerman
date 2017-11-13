# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import classes
import random


def drawBuilding(building, x, y, color):

	# add building to map
	ax1.add_patch(
	    patches.Rectangle(
	        (x, y),   			# (x,y)
	        building.length,    # length
	        building.width,     # width
	        facecolor=color		# color
	    )
	)

def overlap(building1, building2):
	xOverlap = True
	yOverlap = True

	if (building1.left > building2.right) or (building1.right < building2.left):
		xOverlap = False

	if (building1.top < building2.bottom) or (building1.bottom > building2.top):
		xOverlap = False

	return xOverlap and yOverlap

if __name__ == "__main__":
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')

	buildings = []

	for i in range(12):
		xrandom = random.randint(0, 170)
		yrandom = random.randint(0, 150)
		buildings.append([xrandom, yrandom])
		overlap(buildings[0], )
		for building in buildings:

			while (overlap(building, building[building]) = True)
			xrandom = random.randint(0, 170)
			yrandom = random.randint(0, 150)
			drawBuilding(classes.house, xrandom, yrandom, "red")

	for i in range(5):
		xrandom = random.randint(0, 170)
		yrandom = random.randint(0, 150)
		drawBuilding(classes.bungalow, xrandom, yrandom, "blue")

	for i in range(3):
		xrandom = random.randint(0, 170)
		yrandom = random.randint(0, 150)
		drawBuilding(classes.maison, xrandom, yrandom, "green")

	ax1.set_xlim(0,180)
	ax1.set_ylim(0,160)
	fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')
