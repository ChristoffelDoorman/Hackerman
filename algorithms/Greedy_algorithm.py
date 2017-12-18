# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file contains the greedy algorithm.

# import files
from helpers.helper_functions import h_build, b_build, m_build, calculate_score, move, overlap, check_move
import visualisation.canvas_visualisation as visualisation

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import math
import classes
import time
import helpers

def main(total_houses):

    # start a timer to calculate the runningtime of the algorithm
    start_time = time.time()

    district = classes.Map(360, 320, 0)

    # set number of each building type
    h_number = int(0.6 * total_houses)
    b_number = int(0.25 * total_houses)
    m_number = int(0.15 * total_houses)

    # build random maison
    while len(district.buildings) == 0:
        district, m_counter = m_build(district, 0)

    # first, build all maisons
    for i in range(m_number - 1):

        maison = classes.Maison(0, 0)
        district.buildings.append(maison)
        top_score, best_x, best_y = walk_check(maison, district)
        maison.update(best_x, best_y)

    # second, build all bungalows
    for i in range(b_number):

        bungalow = classes.Bungalow(0, 0)
        district.buildings.append(bungalow)
        top_score, best_x, best_y = walk_check(bungalow, district)
        bungalow.update(best_x, best_y)

    # third, build all houses
    for i in range(h_number):

        house = classes.House(0, 0)
        district.buildings.append(house)
        top_score, best_x, best_y = walk_check(house, district)
        house.update(best_x, best_y)

    end_time = time.time() - start_time
    score = district.score()

    return district, score, end_time


def check_possible(building, district):

    for build in district.buildings:

        # don't check if building overlaps with itself
        if build == building:
            continue

        # check if building overlaps with other buildings
        olap = overlap(build, building)

        if olap:
            return False

    if not olap:
        return True

def walk_check(building, district):

    # begin to walk in positive x direction
    direction = 1
    top_score = 0
    best_x = 0
    best_y = 0
    best_scores = {}

    # start walking
    while True:

        move(building, direction, 1)

        # if right edge reached, move 1 up and start moving to left edge
        if building.right_top[0] >= 360:
            move(building, 2, 1)
            direction = -1
            continue

        # if left edge reached, move 1 up and start moving to right edge again
        if building.left_bottom[0] <= 0:
            move(building, 2, 1)
            direction = 1
            continue

        # if possible and score is better, remember location
        possible = check_possible(building, district)
        if possible:
            score = district.score()
            if score > top_score:
                top_score = score
                best_x = building.left_bottom[0]
                best_y = building.left_bottom[1]

        if building.right_top[1] >= 320 and building.right_top[0] >= 359:

            return top_score, best_x, best_y
