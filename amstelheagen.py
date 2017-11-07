# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import helpers


def floorMap(building, x, y):
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')
	ax1.add_patch(
	    patches.Rectangle(
	        (x, y),   			# (x,y)
	        building.length,    # width
	        building.width,     # height
	    )
	)
	ax1.set_xlim(0,180)
	ax1.set_ylim(0,160)
	fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')


if __name__ == "__main__":
	floorMap(helpers.bungalow, 50, 20)
	floorMap(helpers.maison, 75, 30)
	floorMap(helpers.house, 30, 70)

