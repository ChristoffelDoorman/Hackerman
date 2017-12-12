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


district = classes.Map


def main(total_houses, iterations):

    best_iteration = 0

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
        total_value = helpers.calculate_score(buildings)

        if (total_value > best_iteration):
            best_iteration = total_value

	# stop = timeit.default_timer()
	# print "De tijd is: ", stop - start

    return buildings, best_iteration
