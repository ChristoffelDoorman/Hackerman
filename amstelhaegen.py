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
	xoverlap = True
	yoverlap = True

	if ((building1.left > building2.right) or (building1.right < building2.left)):
		xoverlap = False

	if ((building1.top < building2.bottom) or (building1.bottom > building2.top)):
		yoverlap = False

	if not yoverlap and not xoverlap:
		return False

	return True

if __name__ == "__main__":
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')
	# fill building array with a house at a random point
	buildings = []

	while len(buildings) < 12:
		print(len(buildings))
		xrandom = random.randint(0, 170)
		yrandom = random.randint(0, 150)
		print (xrandom, yrandom)
		house = classes.house(xrandom, yrandom)

		olap = True
		while(olap and len(buildings)!=0):
			for building in buildings:
				olap = overlap(building, house)
				if olap:
					print ("bla")
					house.left = random.randint(0, 170)
					house.bottom = random.randint(0, 150)
					break


		buildings.append(house)
		drawBuilding(house, xrandom, yrandom, "red")

	#for i in buildings
	#print overlap(buildings[0], buildings[1])

		#for i in buildings:
			#overlap(buildings[building],  )

			# while (overlap(building, building[building]) = True)
			#xrandom = random.randint(0, 170)
			#yrandom = random.randint(0, 150)
			#drawBuilding(classes.house, xrandom, yrandom, "red")
	# print buildings
	'''
	for i in range(5):
		xrandom = random.randint(0, 170)
		yrandom = random.randint(0, 150)
		drawBuilding(classes.bungalow, xrandom, yrandom, "blue")

	for i in range(3):
		xrandom = random.randint(0, 170)
		yrandom = random.randint(0, 150)
		drawBuilding(classes.maison, xrandom, yrandom, "green")'''

	ax1.set_xlim(0,180)
	ax1.set_ylim(0,160)
	fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')
