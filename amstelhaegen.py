# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import classes
import random
import pdb

HUIZEN_AANTAL = 60
canvas_x = 360
canvas_y = 320

def drawBuilding(building, x, y, edgecolor):

	# add building to map
	ax1.add_patch(
	    patches.Rectangle(
	        (x, y),   			# (x,y)
	        building.length,    # length
	        building.width,     # width	# color
			linewidth = 1,
			edgecolor = edgecolor,
			facecolor = 'none'
	    )
	)

def overlap(building1, building2):
	overlap = True

	if (building1.left > building2.right or building2.left > building1.right
		or building1.bottom > building2.top or building2.bottom > building1.top):
		overlap = False

	return overlap

def h_build(buildings, h_counter):

	xrandom = random.randint(0, canvas_x - classes.house.width)
	yrandom = random.randint(0, canvas_y - classes.house.length)

	house = classes.house(xrandom, yrandom)

	olap = True
	for building in buildings:
		olap = overlap(house, building)

		if olap:
			break

	if not olap:
		buildings.append(house)
		drawBuilding(house, house.left, house.bottom, 'red')
		h_counter += 1

	return buildings, h_counter

def b_build(buildings, b_counter):

	xrandom = random.randint(0, canvas_x - classes.bungalow.width)
	yrandom = random.randint(0, canvas_y - classes.bungalow.length)
	bungalow = classes.bungalow(xrandom, yrandom)

	olap = True
	for building in buildings:
		olap = overlap(bungalow, building)

		if olap:
			break

	if not olap:
		buildings.append(bungalow)
		drawBuilding(bungalow, bungalow.left, bungalow.bottom, 'blue')
		b_counter += 1

	return buildings, b_counter

def m_build(buildings, m_counter):

	xrandom = random.randint(0, canvas_x - classes.maison.width)
	yrandom = random.randint(0, canvas_y - classes.maison.length)
	maison = classes.maison(xrandom, yrandom)

	olap = True
	for building in buildings:
		olap = overlap(maison, building)

		if olap:
			break

	if not olap:
		buildings.append(maison)
		drawBuilding(maison, maison.left, maison.bottom, 'green')
		m_counter += 1

	return buildings, m_counter


if __name__ == "__main__":

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')
	ax1.set_xlim(0,360)
	ax1.set_ylim(0,320)

	# fill building array with a house at a random point
	buildings = []

	# append first house to array 'buildings'
	buildings.append(classes.house(canvas_x, canvas_y))

	# set number of each building type
	h_number = 0.6 * HUIZEN_AANTAL
	b_number = 0.25 * HUIZEN_AANTAL
	m_number = 0.15 * HUIZEN_AANTAL

    # create counters to count number of each building
	h_counter, b_counter, m_counter = 0, 0, 0

	while len(buildings) < HUIZEN_AANTAL:

        # choose random building type
		building_type = random.choice(['house', 'bungalow', 'maison'])

		if building_type == 'house' and h_counter < h_number:
			buildings, h_counter = h_build(buildings, h_counter)

		if building_type == 'bungalow' and b_counter < b_number:
			buildings, b_counter = b_build(buildings, b_counter)

		if building_type == 'maison' and m_counter < m_number:
			buildings, m_counter = m_build(buildings, m_counter)

	fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')

    # delete first house from array
	buildings.pop(0)
