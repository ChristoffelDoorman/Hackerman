# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file contains all functions neccesary for the algoritms.

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import pdb
import numpy as np
import locale
import timeit
import math
import os
from os import path
from datetime import datetime

import classes

X_DIMENSION = 360
Y_DIMENSION = 320
house_length = 20
house_width = 20
bungalow_length = 21
bungalow_width = 26
maison_length = 34
maison_width = 33
best_iteration = 0

# calculate diagonal distance between two coordinates
def pythagoras(x1, y1, x2, y2):
	distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

	return distance

# check overlap between two buildings
def overlap(building1, building2):

	overlap = True

	# check if it is impossible for two buildings to overlap, ifso change overlap to False
	if (building1.left_bottom[0] > building2.right_bottom[0] or building2.left_bottom[0] > building1.right_bottom[0]
		or building1.left_bottom[1] > building2.left_top[1] or building2.left_bottom[1] > building1.left_top[1]):
		overlap = False

	# if buildings are exactly the same, change overlap back to True
	if (building1.left_bottom[0] == building2.left_bottom[0] and building1.left_bottom[1] == building2.left_bottom[1]):
		overlap = True

	return overlap

# check if building is inside the map
def overlap_canvas(building):

	olap = True
	if building.left_bottom[0] >= 0 and building.left_bottom[1] >= 0 and building.right_top[0] <= X_DIMENSION and building.right_top[1] <= Y_DIMENSION:
		olap = False

	return olap

# builds a house and appends it to the district.buildings
def h_build(district, h_counter):

	# choose random position for x and y (left bottom), inside the canvas
	xrandom = random.randint(0, X_DIMENSION - house_width)
	yrandom = random.randint(0, Y_DIMENSION - house_length)
	house = classes.House(xrandom, yrandom)

	# check for overlap with water
	for water in district.waters:
		olap = overlap(house, water)

		if olap:
			return district, h_counter

	# if no buildings yet, append the building and increment counter
	if len(district.buildings) == 0:
		district.buildings.append(house)
		h_counter += 1
		return district, h_counter

	olap = True
	# check for overlap with buildings
	for building in district.buildings:
		olap = overlap(house, building)

		if olap:
			return district, h_counter

	# if no overlap is found append building and increment counter
	if not olap:
		district.buildings.append(house)
		# drawBuilding(house, house.left_bottom[0], house.left_bottom[1], 'red')
		h_counter += 1

	return district, h_counter

# builds a bungalow and appends it to the district.buildings
def b_build(district, b_counter):

	# choose random position for x and y (left bottom), inside the canvas
	xrandom = random.randint(0, X_DIMENSION - bungalow_width)
	yrandom = random.randint(0, Y_DIMENSION - bungalow_length)
	bungalow = classes.Bungalow(xrandom, yrandom)

	# randomly rotate or not
	choice = random.getrandbits(1)
	if choice:
		bungalow.rotate()

		# if the rotate causes the building to overlap with canvas, rotate back
		if overlap_canvas(bungalow):
			bungalow.rotate()

	# check for overlap with water
	for water in district.waters:
		olap = overlap(bungalow, water)

		if olap:
			return district, b_counter

	# if no buildings yet, append the building and increment counter
	if len(district.buildings) == 0:
		district.buildings.append(bungalow)
		b_counter += 1
		return district, b_counter

	olap = True
	# check for overlap with buildings
	for building in district.buildings:
		olap = overlap(bungalow, building)

		if olap:
			return district, b_counter

	# if no overlap is found append building and increment counter
	if not olap:
		district.buildings.append(bungalow)
		b_counter += 1

	return district, b_counter

# builds a maison and appends it to the district.buildings
def m_build(district, m_counter):

	# choose random position for x and y (left bottom), inside the canvas
	xrandom = random.randint(0, X_DIMENSION - maison_width)
	yrandom = random.randint(0, Y_DIMENSION - maison_length)
	maison = classes.Maison(xrandom, yrandom)

	# randomly rotate or not
	choice = random.getrandbits(1)
	if choice:
		maison.rotate()

		# if the rotate causes the building to overlap with canvas, rotate back
		if overlap_canvas(maison):
			maison.rotate()

	# check for overlap with water
	for water in district.waters:
		olap = overlap(maison, water)

		if olap:
			return district, m_counter

	# if no buildings yet, append the building and increment counter
	if len(district.buildings) == 0:
		m_counter += 1
		district.buildings.append(maison)
		return district, m_counter

	olap = True
	# check for overlap with buildings
	for building in district.buildings:
		olap = overlap(maison, building)

		if olap:
			return district, m_counter

	# if no overlap is found append building and increment counter
	if not olap:
		district.buildings.append(maison)
		# drawBuilding(maison, maison.left_bottom[0], maison.left_bottom[1], 'green')
		m_counter += 1

	return district, m_counter

# returns the colest distance to the bounds of the canvas
def distance_to_edge(current_building):
	# distance until left, upper, right, or lower bound of canvas
	distance_left = current_building.left_bottom[0]
	distance_up = Y_DIMENSION - current_building.left_top[1]
	distance_right = X_DIMENSION - current_building.right_bottom[0]
	distance_down = current_building.right_bottom[1]

	# return the shortest distance
	distance = min(distance_left, distance_up, distance_right, distance_down)
	return distance

# returns the closest distance to the nearest building
def closest_distance(current_building, buildings):

	# initialize the distance to high value
	distance = 500

	# if you want the 'urban district' (which means the bounds of the canvas count as the shorest distance)
	# uncomment the line here below
	'''distance = distance_to_edge(current_building)'''

	closest = distance

	for building in buildings:

        # area left up
		if (building.right_bottom[0] <= current_building.left_top[0]
		 	and building.right_bottom[1] >= current_building.left_top[1]):

            # calculate distance
			distance = pythagoras(current_building.left_top[0], current_building.left_top[1],
			building.right_bottom[0], building.right_bottom[1])

        # area middle up
		elif (building.right_bottom[1] >= current_building.left_top[1]
			and building.right_bottom[0] >= current_building.left_top[0]
			and building.left_bottom[0] <= current_building.right_top[0]):

			# calculate distance
			distance = building.right_bottom[1] - current_building.right_top[1]

        # area right up
		elif (building.left_bottom[0] >= current_building.right_top[0]
		 	and building.right_bottom[1] >= current_building.left_top[1]):

			# calculate distance
			distance = pythagoras(current_building.right_top[0], current_building.right_top[1],
			building.left_bottom[0], building.left_bottom[1])

        # area middle right
		elif (building.left_bottom[0] >= current_building.right_top[0]
			and building.left_bottom[1] <= current_building.right_top[1]
			and building.left_top[1] >= current_building.right_bottom[1]):

			# calculate distance
			distance = building.left_bottom[0] - current_building.right_bottom[0]

        # area right down
		elif (building.left_top[0] >= current_building.right_bottom[0]
		 	and building.right_top[1] <= current_building.right_bottom[1]):

			# calculate distance
			distance = pythagoras(current_building.right_bottom[0], current_building.right_bottom[1],
			building.left_top[0], building.left_top[1])

		# area middle down
		elif (building.right_top[1] <= current_building.left_bottom[1]
			and building.right_top[0] >= current_building.left_bottom[0]
			and building.left_top[0] <= current_building.right_bottom[0]):

			# calculate distance
			distance = current_building.right_bottom[1] - building.right_top[1]

        # area left down
		elif (building.right_top[0] <= current_building.left_bottom[0]
		 	and building.right_top[1] <= current_building.left_bottom[1]):

			# calculate distance
			distance = pythagoras(current_building.left_bottom[0], current_building.left_bottom[1],
			building.right_top[0], building.right_top[1])

        # area middle left
		elif (building.right_bottom[0] <= current_building.left_bottom[0]
			and building.right_bottom[1] <= current_building.left_top[1]
			and building.right_top[1] >= current_building.left_bottom[1]):

			# calculate distance
			distance = current_building.left_bottom[0] - building.right_bottom[0]

		# update closest distance if closer
		if distance < closest:
			closest = distance

	return closest

# calculates the score of the current buildings list
def calculate_score(buildings):

	total_value = 0

	# calculate score per building for the closest distance to next object
	# add all scores together
	for current_building in buildings:
		closest = closest_distance(current_building, buildings)
		total_value += current_building.score(closest)

	return total_value

# moves buildings in direction with stepsize
def move(building, direction, step):

	# left direction with given stepsize
    if direction == -1:

        building.left_bottom[0] -= step
        building.left_top[0] -= step
        building.right_top[0] -= step
        building.right_bottom[0] -= step

	# up direction with given stepsize
    if direction == 2:
        building.left_bottom[1] += step
        building.left_top[1] += step
        building.right_top[1] += step
        building.right_bottom[1] += step

	# right direction with given stepsize
    if direction == 1:
        building.left_bottom[0] += step
        building.left_top[0] += step
        building.right_top[0] += step
        building.right_bottom[0] += step

	# down direction with given stepsize
    if direction == -2:
        building.left_bottom[1] -= step
        building.left_top[1] -= step
        building.right_top[1] -= step
        building.right_bottom[1] -= step

    return building

# NOG INVULLEN STOF
def check_position(building, district, x_direction, y_direction, x_stepsize, y_stepsize):

    move(building, x_direction, x_stepsize)
    move(building, y_direction, y_stepsize)

    if overlap_canvas(building):
        return False, 0

    olap = True
    for water in district.waters:
        olap = overlap(building, water)

        if olap:
            move(building, - x_direction, x_stepsize)
            move(building, - y_direction, y_stepsize)
            return False, 0

    olap = True
    for build in district.buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            move(building, - x_direction, x_stepsize)
            move(building, - y_direction, y_stepsize)
            return False, 0

        if not olap:
            score = district.score()
            move(building, - x_direction, x_stepsize)
            move(building, - y_direction, y_stepsize)
            return True, score

# checks if move if possible and if so returns the move score
# if not possible a False is returned and a 0 for the move score
def check_move(building, district, direction, stepsize):

	# move building with stepsize in direction
    move(building, direction, stepsize)

	# check overlap with canvas
    if overlap_canvas(building):
        return False, 0

    olap = True
	# check overlap with water
    for water in district.waters:
        olap = overlap(building, water)

        if olap:
			# if overlap move in opposite direction
            move(building, -direction, stepsize)
            return False, 0

    olap = True
	# check overlap with buildings
    for build in district.buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
			# if overlap move in opposite direction
            move(building, -direction, stepsize)
            return False, 0

    if not olap:
		# calculate score and return True
        score = district.score()
        return True, score

# prints the buildings and water to a txt file for later use
def print_txt(district, algorithm, total_houses, variation):

	# create time stamp for unique file name
    time_stamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

	# if no variation of a algorithm don't add it to the outpath
    if variation == 0:
        outpath = ("output/{}/{}".format(algorithm, total_houses))
    else:
        outpath = ("output/{}/{}/{}".format(algorithm, variation, total_houses))

	# if path doesn't exist already, create it
    if not os.path.exists(outpath):
        os.makedirs(outpath)

	# open a txt file at outpath position in folders
    text_file = open(path.join(outpath,"{}_{}_{}_{}.txt".format(algorithm, total_houses, time_stamp, variation)), "w+")

	# write in txt file the buildings
    for building in district.buildings:
        if building.name == 'maison':
            build = "maison"
        elif building.name == 'bungalow':
            build = "bungalow"
        elif building.name == 'house':
            build = "house"
        text_file.write("{} {} {}\n".format(build, building.left_bottom[0], building.left_bottom[1]))

	# write water in txt file
    for water in district.waters:
        build = 'water'
        text_file.write("{} {} {}\n".format(build, water.left_bottom[0], water.left_bottom[1]))

    text_file.close()
