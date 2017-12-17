# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

# import files
from helpers import h_build, b_build, m_build, add_water
import visualisation
import classes

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import locale
import time
import math
import copy


def main(total_houses, iterations):

    best_iteration = 0
    start_time = time.time()
    best_district = classes.Map(360, 320)

    for i in range(iterations):

        district = classes.Map(360, 320)

        # set number of each building type
        h_number = 0.6 * total_houses
        b_number = 0.25 * total_houses
        m_number = 0.15 * total_houses

        # create counters to count number of each building
        h_counter, b_counter, m_counter = 0, 0, 0

        # add water to map
        district = add_water(district, 1)

        # build houses until maximum is reached
        while len(district.buildings) < total_houses:
            # print district.buildings
	        # choose random building type
            building_type = random.randint(1, 3)

            if building_type == 1 and h_counter < h_number:
                district, h_counter = h_build(district, h_counter)

            if building_type == 2 and b_counter < b_number:
                district, b_counter = b_build(district, b_counter)

            if building_type == 3 and m_counter < m_number:
                district, m_counter = m_build(district, m_counter)

        # calculate closest distance to buildings
        total_value = district.score()
        # print total_value

        if (total_value > best_iteration):
            best_district.buildings = district.buildings
            best_iteration = total_value

	# stop = timeit.default_timer()
	# print "De tijd is: ", stop - start
    end_time = time.time() - start_time
    return best_district, best_iteration, end_time
