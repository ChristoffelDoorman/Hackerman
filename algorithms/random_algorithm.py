# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

# import files
from helpers.helper_functions import h_build, b_build, m_build
import visualisation.canvas_visualisation
import classes

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import locale
import time
import math
import copy
import math


def main(total_houses, iterations, water_type):

    # initialize a new class for what will be the best district
    best_district = classes.Map(360, 320, water_type)

    best_iteration = 0

    # start a timer to calculate the runningtime of the algorithm
    start_time = time.time()

    for i in range(iterations):

        district = classes.Map(360, 320, water_type)

        # set number of each building type
        h_number = math.floor(0.6 * total_houses)
        b_number = math.floor(0.25 * total_houses)
        m_number = math.floor(0.15 * total_houses)

        # create counters to count number of each building
        h_counter, b_counter, m_counter = 0, 0, 0

        # if the following while loop is more than one second, it will timeout
        timeout = time.time() + 1

        # build houses until maximum is reached
        while len(district.buildings) < total_houses:

            if time.time() > timeout:
                break

            # add buildings to district in random order
            building_type = random.randint(1, 3)

            # if building is successfully added, increment counter until total
            if building_type == 1 and h_counter < h_number:
                district, h_counter = h_build(district, h_counter)

            if building_type == 2 and b_counter < b_number:
                district, b_counter = b_build(district, b_counter)

            if building_type == 3 and m_counter < m_number:
                district, m_counter = m_build(district, m_counter)

        # calculate the score of the district
        total_value = district.score()

        # only change best buildings if value per iteration has increased
        if (total_value > best_iteration):
            best_district.buildings = district.buildings
            best_iteration = total_value

    # calculate end time of algorithm and return the district and corresponding score
    end_time = time.time() - start_time
    return best_district, best_iteration, end_time
