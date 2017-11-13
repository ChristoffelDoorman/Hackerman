# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import classes
import random

def drawBuilding(building, x, y):

	# add building to map
    ax1.add_patch(
        patches.Rectangle(
            (x, y),				# (x,y)
            building.length,	# length
            building.width,		# width
            )
    )

if __name__ == "__main__":
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')

	for i in range(12):
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
