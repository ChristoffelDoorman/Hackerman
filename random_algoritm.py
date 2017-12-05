# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import pdb
import numpy as np
import locale
import timeit
import math

# import files
import classes
import main
import helpers
import visualisation



TOTAL_HOUSES = 60
X_DIMENSION = 360
Y_DIMENSION = 320


def main(total_houses, iterations):
    best_iteration = 0

    for i in range(iterations):

        # fill building array with a house at a random point
        buildings = []

        # append first house to array 'buildings'
        buildings.append(classes.House(X_DIMENSION, Y_DIMENSION))

        # set number of each building type
        h_number = 0.6 * total_houses
        b_number = 0.25 * total_houses
        m_number = 0.15 * total_houses

        # create counters to count number of each building
        h_counter, b_counter, m_counter = 0, 0, 0

        # build houses until maximum is reached
        while (len(buildings) - 1) < total_houses:

	        # choose random building type
            building_type = random.choice(['house', 'bungalow', 'maison'])

            if building_type == 'house' and h_counter < h_number:
                buildings, h_counter = helpers.h_build(buildings, h_counter)

            if building_type == 'bungalow' and b_counter < b_number:
                buildings, b_counter = helpers.b_build(buildings, b_counter)

            if building_type == 'maison' and m_counter < m_number:
                buildings, m_counter = helpers.m_build(buildings, m_counter)

        # delete first house from array
        buildings.pop(0)

        # calculate closest distance to buildings
        counter = 0
        total_value = 0
        for current_building in buildings:
            counter += 1
            closest = helpers.closest_distance(current_building, buildings)
            total_value += current_building.score(closest)

        if (total_value > best_iteration):
            best_iteration = total_value

            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111, aspect='equal')
            ax1.set_xlim(0, 360)
            ax1.set_ylim(0, 320)

            for building in buildings:
                if building.name == 'house':
                    visualisation.drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'red')
                if building.name == 'bungalow':
                    visualisation.drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'black')
                if building.name == 'maison':
                    visualisation.drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'green')

            # safe figure
            fig1.savefig('probeersel.png', dpi=90, bbox_inches='tight')

        print best_iteration
	# stop = timeit.default_timer()
	# print "De tijd is: ", stop - start
    print "De hoogste score is: ", best_iteration

# if __name__ == "__main__":
#     main(iterations)
