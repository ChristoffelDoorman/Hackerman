# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import classes
import random
import pdb
import numpy as np


TOTAL_HOUSES = 60
X_DIMENSION = 360
Y_DIMENSION = 320

def distance(x1, y1, x2, y2):
	dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

	return dist

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

	if (building1.left_bottom[0] > building2.right_bottom[0] or building2.left_bottom[0] > building1.right_bottom[0]
		or building1.left_bottom[1] > building2.left_top[1] or building2.left_bottom[1] > building1.left_top[1]):
		overlap = False

	return overlap

def h_build(buildings, h_counter):


	xrandom = random.randint(0, X_DIMENSION - classes.house.width)
	yrandom = random.randint(0, Y_DIMENSION - classes.house.length)

	house = classes.house(xrandom, yrandom)

	olap = True
	for building in buildings:
		olap = overlap(house, building)

		if olap:
			break

	if not olap:
		buildings.append(house)
		drawBuilding(house, house.left_bottom[0], house.left_bottom[1], 'red')
		h_counter += 1

	return buildings, h_counter

def b_build(buildings, b_counter):

	xrandom = random.randint(0, X_DIMENSION - classes.bungalow.width)
	yrandom = random.randint(0, Y_DIMENSION - classes.bungalow.length)
	bungalow = classes.bungalow(xrandom, yrandom)

	olap = True
	for building in buildings:
		olap = overlap(bungalow, building)

		if olap:
			break

	if not olap:
		buildings.append(bungalow)
		drawBuilding(bungalow, bungalow.left_bottom[0], bungalow.left_bottom[1], 'blue')
		b_counter += 1

	return buildings, b_counter

def m_build(buildings, m_counter):

	xrandom = random.randint(0, X_DIMENSION - classes.maison.width)
	yrandom = random.randint(0, Y_DIMENSION - classes.maison.length)
	maison = classes.maison(xrandom, yrandom)

	olap = True
	for building in buildings:
		olap = overlap(maison, building)

		if olap:
			break

	if not olap:
		buildings.append(maison)
		drawBuilding(maison, maison.left_bottom[0], maison.left_bottom[1], 'green')
		m_counter += 1

	return buildings, m_counter

def score(buildings):

	# for building in buildings:
	current_building = buildings[10]
	print current_building.left_bottom, "gebouw"

	left_top_buildings = []
	closest = 50000
	for building in buildings:

        # area linksboven
		if (building.right_bottom[0] < current_building.left_top[0]
		 	and building.right_bottom[1] > current_building.left_top[1]):

			dist = distance(current_building.left_top[0], current_building.left_top[1],
			building.right_bottom[0], building.right_bottom[1])
			if dist < closest:
				closest = dist

        # area midden boven
		if (building.right_bottom[1] > current_building.left_top[1]
			and building.right_bottom[0] > current_building.left_top[0]
			and building.left_bottom[0] < current_building.right_top[0]):

			# print "onderkant verelijking", building.right_bottom[1]
			# print "bovenkant current", current_building.right_top[1]
			dist = building.right_bottom[1] - current_building.right_top[1]

			if dist < closest:
				closest = dist

        # area rechtsboven
		if (building.left_bottom[0] > current_building.right_top[0]
		 	and building.right_bottom[1] > current_building.left_top[1]):

			dist = distance(current_building.right_top[0], current_building.right_top[1],
			building.left_bottom[0], building.left_bottom[1])
			if dist < closest:
				closest = dist

        # area midden rechts
		if (building.left_bottom[0] > current_building.right_top[0]
			and building.left_bottom[1] < current_building.right_top[1]
			and building.left_top[1] > current_building.right_bottom[1]):

			# print "onderkant verelijking", building.right_bottom[1]
			# print "bovenkant current", current_building.right_top[1]
			dist = building.left_bottom[0] - current_building.right_bottom[0]

			if dist < closest:
				closest = dist

        # area rechtsonder
		if (building.left_top[0] > current_building.right_bottom[0]
		 	and building.right_top[1] < current_building.right_bottom[1]):

			dist = distance(current_building.right_bottom[0], current_building.right_bottom[1],
			building.left_top[0], building.left_top[1])
			if dist < closest:
				closest = dist

		# area midden onder
		if (building.right_top[1] < current_building.left_bottom[1]
			and building.right_top[0] > current_building.left_bottom[0]
			and building.left_top[0] < current_building.right_bottom[0]):

			# print "onderkant verelijking", building.right_bottom[1]
			# print "bovenkant current", current_building.right_top[1]
			dist = current_building.right_top[1] - building.right_bottom[1]

			if dist < closest:
				closest = dist

        # area linksonder
		if (building.right_top[0] < current_building.left_bottom[0]
		 	and building.right_top[1] < current_building.left_bottom[1]):

			dist = distance(current_building.left_bottom[0], current_building.left_bottom[1],
			building.right_top[0], building.right_top[1])
			if dist < closest:
				closest = dist

        # area midden rechts
		if (building.right_bottom[0] < current_building.left_bottom[0]
			and building.right_bottom[1] < current_building.left_top[1]
			and building.right_top[1] > current_building.left_bottom[1]):

			# print "onderkant verelijking", building.right_bottom[1]
			# print "bovenkant current", current_building.right_top[1]
			dist = current_building.left_bottom[0] - building.right_bottom[0]

			if dist < closest:
				closest = dist

			print building.left_bottom, "de vergelijking"
			print dist, "afstand"

	print closest


		# closest = 100
		# for building.left_bottom[0] in building:
		# 	distance = building.left_bottom[0] - building.left_bottom
		# 	if distance < closest:
		# 		closest = distance

	# building_coordinates = []
    #
	# for building in buildings:
	# 	building_coordinates.append(building.left_bottom)
	# 	building_coordinates.sort()
	# 	print building_coordinates




if __name__ == "__main__":

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')
	ax1.set_xlim(0,360)
	ax1.set_ylim(0,320)

	# fill building array with a house at a random point
	buildings = []

	# append first house to array 'buildings'
	buildings.append(classes.house(X_DIMENSION, Y_DIMENSION))

	# set number of each building type
	h_number = 0.6 * TOTAL_HOUSES
	b_number = 0.25 * TOTAL_HOUSES
	m_number = 0.15 * TOTAL_HOUSES

    # create counters to count number of each building
	h_counter, b_counter, m_counter = 0, 0, 0

	# build houses until maximum is reached
	while len(buildings) < TOTAL_HOUSES:

        # choose random building type
		building_type = random.choice(['house', 'bungalow', 'maison'])

		if building_type == 'house' and h_counter < h_number:
			buildings, h_counter = h_build(buildings, h_counter)

		if building_type == 'bungalow' and b_counter < b_number:
			buildings, b_counter = b_build(buildings, b_counter)

		if building_type == 'maison' and m_counter < m_number:
			buildings, m_counter = m_build(buildings, m_counter)

    # safe figure
	fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')

    # delete first house from array
	buildings.pop(0)

	score(buildings)

	# for building in buildings:
	# 	print building.left
