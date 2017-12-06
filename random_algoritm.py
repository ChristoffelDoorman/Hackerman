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
from os import path

# import files
import classes
import main
import helpers
import visualisation

# start = timeit.default_timer()

X_DIMENSION = 360
Y_DIMENSION = 320



def main(total_houses, iterations):

    # where to save output files
    outpath = ("output/{}".format(total_houses))

    best_iteration = 0

    fig1 = plt.figure()

    for i in range(iterations):

        # fill building array with a house at a random point
        buildings = []

        # set number of each building type
        h_number = 0.6 * total_houses
        b_number = 0.25 * total_houses
        m_number = 0.15 * total_houses

        # create counters to count number of each building
        h_counter, b_counter, m_counter = 0, 0, 0

        # build houses until maximum is reached
        while len(buildings) < total_houses:

	        # choose random building type
            building_type = random.choice(['house', 'bungalow', 'maison'])

            if building_type == 'house' and h_counter < h_number:
                buildings, h_counter = helpers.h_build(buildings, h_counter)

            if building_type == 'bungalow' and b_counter < b_number:
                buildings, b_counter = helpers.b_build(buildings, b_counter)

            if building_type == 'maison' and m_counter < m_number:
                buildings, m_counter = helpers.m_build(buildings, m_counter)


        # calculate closest distance to buildings
        counter = 0
        total_value = 0
        for current_building in buildings:
            counter += 1
            closest = helpers.closest_distance(current_building, buildings)
            total_value += current_building.score(closest)

        if (total_value > best_iteration):
            best_iteration = total_value

            # add subplot
            ax1 = fig1.add_subplot(111, aspect='equal')
            ax1.set_xlim(0, X_DIMENSION)
            ax1.set_ylim(0, Y_DIMENSION)
            plt.suptitle("The total value is: {:,}".format(best_iteration))

            for building in buildings:
                if building.name == 'house':
                    visualisation.drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'red')
                if building.name == 'bungalow':
                    visualisation.drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'black')
                if building.name == 'maison':
                    visualisation.drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'green')

            # save figure
            fig1.savefig(path.join(outpath,"20_houses_{0}.png".format(i)))
            plt.gcf().clear()
            print best_iteration

	# stop = timeit.default_timer()
	# print "De tijd is: ", stop - start
    print "De hoogste score is: ", best_iteration
    return buildings

# if __name__ == "__main__":
#     main(iterations)
