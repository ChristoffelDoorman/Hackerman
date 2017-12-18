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

def pythagoras(x1, y1, x2, y2):
	distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

	return distance

def overlap(building1, building2):
	overlap = True

	if (building1.left_bottom[0] > building2.right_bottom[0] or building2.left_bottom[0] > building1.right_bottom[0]
		or building1.left_bottom[1] > building2.left_top[1] or building2.left_bottom[1] > building1.left_top[1]):
		overlap = False

	if (building1.left_bottom[0] == building2.left_bottom[0] and building1.left_bottom[1] == building2.left_bottom[1]):
		overlap = True

		# print "dit ligt op elkaar"

	# print "dit overlapt"
	return overlap

def overlap_canvas(building):

	olap = True
	if building.left_bottom[0] >= 0 and building.left_bottom[1] >= 0 and building.right_top[0] <= X_DIMENSION and building.right_top[1] <= Y_DIMENSION:
		olap = False

	return olap

def h_build(district, h_counter):

	xrandom = random.randint(0, X_DIMENSION - house_width)
	yrandom = random.randint(0, Y_DIMENSION - house_length)
	house = classes.House(xrandom, yrandom)

	for water in district.waters:
		olap = overlap(house, water)

		if olap:
			return district, h_counter

	if len(district.buildings) == 0:
		district.buildings.append(house)
		h_counter += 1
		return district, h_counter

	for building in district.buildings:
		olap = overlap(house, building)

		if olap:
			return district, h_counter

	if not olap:
		district.buildings.append(house)
		# drawBuilding(house, house.left_bottom[0], house.left_bottom[1], 'red')
		h_counter += 1

	return district, h_counter

def b_build(district, b_counter):

	xrandom = random.randint(0, X_DIMENSION - bungalow_width)
	yrandom = random.randint(0, Y_DIMENSION - bungalow_length)
	bungalow = classes.Bungalow(xrandom, yrandom)

	choice = random.getrandbits(1)
	if choice:
		bungalow.rotate()
		if overlap_canvas(bungalow):
			bungalow.rotate()

	for water in district.waters:
		olap = overlap(bungalow, water)

		if olap:
			return district, b_counter

	if len(district.buildings) == 0:
		district.buildings.append(bungalow)
		b_counter += 1
		return district, b_counter

	for building in district.buildings:
		olap = overlap(bungalow, building)

		if olap:
			return district, b_counter

	if not olap:
		district.buildings.append(bungalow)
		# drawBuilding(bungalow, bungalow.left_bottom[0], bungalow.left_bottom[1], 'blue')
		b_counter += 1

	return district, b_counter

def m_build(district, m_counter):

	xrandom = random.randint(0, X_DIMENSION - maison_width)
	yrandom = random.randint(0, Y_DIMENSION - maison_length)
	maison = classes.Maison(xrandom, yrandom)

	# random: length, width = width, length
	choice = random.getrandbits(1)
	if choice:
		maison.rotate()
		if overlap_canvas(maison):
			maison.rotate()

	for water in district.waters:
		olap = overlap(maison, water)

		if olap:
			return district, m_counter

	if len(district.buildings) == 0:
		m_counter += 1
		district.buildings.append(maison)
		return district, m_counter

	olap = True
	for building in district.buildings:
		olap = overlap(maison, building)

		if olap:
			return district, m_counter

	if not olap:
		district.buildings.append(maison)
		# drawBuilding(maison, maison.left_bottom[0], maison.left_bottom[1], 'green')
		m_counter += 1

	return district, m_counter

def distance_to_edge(current_building):
	# distance until left side of canvas
	distance_left = current_building.left_bottom[0]
	distance_up = Y_DIMENSION - current_building.left_top[1]
	distance_right = X_DIMENSION - current_building.right_bottom[0]
	distance_down = current_building.right_bottom[1]

	distance = min(distance_left, distance_up, distance_right, distance_down)
	return distance

def closest_distance(current_building, buildings):

	distance = 500

	# distance = distance_to_edge(current_building)
	closest = distance

	for building in buildings:

        # area linksboven
		if (building.right_bottom[0] <= current_building.left_top[0]
		 	and building.right_bottom[1] >= current_building.left_top[1]):

            # calculate distance
			distance = pythagoras(current_building.left_top[0], current_building.left_top[1],
			building.right_bottom[0], building.right_bottom[1])


        # area midden boven
		elif (building.right_bottom[1] >= current_building.left_top[1]
			and building.right_bottom[0] >= current_building.left_top[0]
			and building.left_bottom[0] <= current_building.right_top[0]):

			# calculate distance
			distance = building.right_bottom[1] - current_building.right_top[1]


        # area rechtsboven
		elif (building.left_bottom[0] >= current_building.right_top[0]
		 	and building.right_bottom[1] >= current_building.left_top[1]):

			# calculate distance
			distance = pythagoras(current_building.right_top[0], current_building.right_top[1],
			building.left_bottom[0], building.left_bottom[1])


        # area midden rechts
		elif (building.left_bottom[0] >= current_building.right_top[0]
			and building.left_bottom[1] <= current_building.right_top[1]
			and building.left_top[1] >= current_building.right_bottom[1]):

			# calculate distance
			distance = building.left_bottom[0] - current_building.right_bottom[0]


        # area rechtsonder
		elif (building.left_top[0] >= current_building.right_bottom[0]
		 	and building.right_top[1] <= current_building.right_bottom[1]):

			# calculate distance
			distance = pythagoras(current_building.right_bottom[0], current_building.right_bottom[1],
			building.left_top[0], building.left_top[1])


		# area midden onder
		elif (building.right_top[1] <= current_building.left_bottom[1]
			and building.right_top[0] >= current_building.left_bottom[0]
			and building.left_top[0] <= current_building.right_bottom[0]):

			# calculate distance
			distance = current_building.right_bottom[1] - building.right_top[1]


        # area linksonder
		elif (building.right_top[0] <= current_building.left_bottom[0]
		 	and building.right_top[1] <= current_building.left_bottom[1]):

			# calculate distance
			distance = pythagoras(current_building.left_bottom[0], current_building.left_bottom[1],
			building.right_top[0], building.right_top[1])


        # area midden links
		elif (building.right_bottom[0] <= current_building.left_bottom[0]
			and building.right_bottom[1] <= current_building.left_top[1]
			and building.right_top[1] >= current_building.left_bottom[1]):

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

    if direction == -1:

        building.left_bottom[0] -= step
        building.left_top[0] -= step
        building.right_top[0] -= step
        building.right_bottom[0] -= step

    if direction == 2:
        building.left_bottom[1] += step
        building.left_top[1] += step
        building.right_top[1] += step
        building.right_bottom[1] += step

    if direction == 1:
        building.left_bottom[0] += step
        building.left_top[0] += step
        building.right_top[0] += step
        building.right_bottom[0] += step

    if direction == -2:
        building.left_bottom[1] -= step
        building.left_top[1] -= step
        building.right_top[1] -= step
        building.right_bottom[1] -= step

    return building

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

def check_move(building, district, direction, stepsize):

    move(building, direction, stepsize)

    if overlap_canvas(building):
		return False, 0

    olap = True
    for water in district.waters:
        olap = overlap(building, water)

        if olap:
            move(building, -direction, stepsize)
            return False, 0

    olap = True
    for build in district.buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            move(building, -direction, stepsize)
            return False, 0

    if not olap:
        score = district.score()
        return True, score


def print_txt(district, algorithm, total_houses, variation):

    time_stamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    if variation == 0:
        outpath = ("output/{}/{}".format(algorithm, total_houses))
    else:
        outpath = ("output/{}/{}/{}".format(algorithm, variation, total_houses))

    if not os.path.exists(outpath):
        os.makedirs(outpath)

    text_file = open(path.join(outpath,"{}_{}_{}_{}.txt".format(algorithm, total_houses, time_stamp, variation)), "w+")

    for building in district.buildings:
        if building.name == 'maison':
            build = "maison"
        elif building.name == 'bungalow':
            build = "bungalow"
        elif building.name == 'house':
            build = "house"
        text_file.write("{} {} {}\n".format(build, building.left_bottom[0], building.left_bottom[1]))

    for water in district.waters:
        build = 'water'
        text_file.write("{} {} {}\n".format(build, water.left_bottom[0], water.left_bottom[1]))

    text_file.close()
