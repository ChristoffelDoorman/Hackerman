import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import pdb
import numpy as np
import locale
import timeit
import math

import classes

district = classes.Map(320, 360)

best_iteration = 0

def pythagoras(x1, y1, x2, y2):
	distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

	return distance


def overlap(building1, building2):
	overlap = True

	if (building1.left_bottom[0] > building2.right_bottom[0] or building2.left_bottom[0] > building1.right_bottom[0]
		or building1.left_bottom[1] > building2.left_top[1] or building2.left_bottom[1] > building1.left_top[1]):
		overlap = False

	return overlap


def h_build(buildings, h_counter):


	xrandom = random.randint(0, district.width - classes.House.width)
	yrandom = random.randint(0, district.height - classes.House.length)
	house = classes.House(xrandom, yrandom)

	if not buildings:
		buildings.append(house)
		return buildings, h_counter

	olap = True
	for building in buildings:
		olap = overlap(house, building)

		if olap:
			break

	if not olap:
		buildings.append(house)
		# drawBuilding(house, house.left_bottom[0], house.left_bottom[1], 'red')
		h_counter += 1

	return buildings, h_counter


def b_build(buildings, b_counter):

	xrandom = random.randint(0, district.width - classes.Bungalow.width)
	yrandom = random.randint(0, district.height - classes.Bungalow.length)
	bungalow = classes.Bungalow(xrandom, yrandom)

	choice = random.getrandbits(1)
	if choice:
		bungalow.length, bungalow.width = bungalow.width, bungalow.length
		bungalow.left_top[1] = yrandom + bungalow.length
		bungalow.right_top = [xrandom + bungalow.width, yrandom + bungalow.length]
		bungalow.right_bottom[0] = xrandom + bungalow.width

	if not buildings:
		buildings.append(bungalow)
		return buildings, b_counter

	olap = True
	for building in buildings:
		olap = overlap(bungalow, building)

		if olap:
			break

	if not olap:
		buildings.append(bungalow)
		# drawBuilding(bungalow, bungalow.left_bottom[0], bungalow.left_bottom[1], 'blue')
		b_counter += 1

	return buildings, b_counter


def m_build(buildings, m_counter):

	xrandom = random.randint(0, district.width - classes.Maison.width)
	yrandom = random.randint(0, district.height - classes.Maison.length)
	maison = classes.Maison(xrandom, yrandom)

	# random: length, width = width, length
	choice = random.getrandbits(1)
	if choice:
		maison.length, maison.width = maison.width, maison.length
		maison.left_top[1] = yrandom + maison.length
		maison.right_top = [xrandom + maison.width, yrandom + maison.length]
		maison.right_bottom[0] = xrandom + maison.width

	if not buildings:
		buildings.append(maison)
		return buildings, m_counter

	olap = True
	for building in buildings:
		olap = overlap(maison, building)

		if olap:
			break

	if not olap:
		buildings.append(maison)
		# drawBuilding(maison, maison.left_bottom[0], maison.left_bottom[1], 'green')
		m_counter += 1

	return buildings, m_counter


def closest_distance(current_building, buildings):

	distance = 500
	closest = distance

	for building in buildings:

        # area linksboven
		if (building.right_bottom[0] < current_building.left_top[0]
		 	and building.right_bottom[1] > current_building.left_top[1]):

            # calculate distance
			distance = pythagoras(current_building.left_top[0], current_building.left_top[1],
			building.right_bottom[0], building.right_bottom[1])


        # area midden boven
		elif (building.right_bottom[1] > current_building.left_top[1]
			and building.right_bottom[0] > current_building.left_top[0]
			and building.left_bottom[0] < current_building.right_top[0]):

			# calculate distance
			distance = building.right_bottom[1] - current_building.right_top[1]


        # area rechtsboven
		elif (building.left_bottom[0] > current_building.right_top[0]
		 	and building.right_bottom[1] > current_building.left_top[1]):

			# calculate distance
			distance = pythagoras(current_building.right_top[0], current_building.right_top[1],
			building.left_bottom[0], building.left_bottom[1])


        # area midden rechts
		elif (building.left_bottom[0] > current_building.right_top[0]
			and building.left_bottom[1] < current_building.right_top[1]
			and building.left_top[1] > current_building.right_bottom[1]):

			# calculate distance
			distance = building.left_bottom[0] - current_building.right_bottom[0]


        # area rechtsonder
		elif (building.left_top[0] > current_building.right_bottom[0]
		 	and building.right_top[1] < current_building.right_bottom[1]):

			# calculate distance
			distance = pythagoras(current_building.right_bottom[0], current_building.right_bottom[1],
			building.left_top[0], building.left_top[1])


		# area midden onder
		elif (building.right_top[1] < current_building.left_bottom[1]
			and building.right_top[0] > current_building.left_bottom[0]
			and building.left_top[0] < current_building.right_bottom[0]):

			# calculate distance
			distance = current_building.right_top[1] - building.right_bottom[1]


        # area linksonder
		elif (building.right_top[0] < current_building.left_bottom[0]
		 	and building.right_top[1] < current_building.left_bottom[1]):

			# calculate distance
			distance = pythagoras(current_building.left_bottom[0], current_building.left_bottom[1],
			building.right_top[0], building.right_top[1])


        # area midden rechts
		elif (building.right_bottom[0] < current_building.left_bottom[0]
			and building.right_bottom[1] < current_building.left_top[1]
			and building.right_top[1] > current_building.left_bottom[1]):

			# calculate distance
			distance = current_building.left_bottom[0] - building.right_bottom[0]


		# update closest distance if closer
		if distance < closest:
			closest = distance

	return closest


def calculate_score(buildings):

	total_value = 0

	for current_building in buildings:
		closest = closest_distance(current_building, buildings)
		total_value += current_building.score(closest)

	return total_value


def move(building, direction, step):

    if direction == 'left':

        building.left_bottom[0] -= step
        building.left_top[0] -= step
        building.right_top[0] -= step
        building.right_bottom[0] -= step

    if direction == 'up':
        building.left_bottom[1] += step
        building.left_top[1] += step
        building.right_top[1] += step
        building.right_bottom[1] += step

    if direction == 'right':
        building.left_bottom[0] += step
        building.left_top[0] += step
        building.right_top[0] += step
        building.right_bottom[0] += step

    if direction == 'down':
        building.left_bottom[1] -= step
        building.left_top[1] -= step
        building.right_top[1] -= step
        building.right_bottom[1] -= step

    return building


# def swap(building1, building2):
    #
	# building1, building2 = building2, buildings1
    #
	# building1.
	# for building in buildings:
    #
	# 	if overlap(building, building1) or overlap(building, building2):
	# 		building1, building2 = building2, building1
	# 		return buildings
