# import files
from helpers import h_build, b_build, m_build, move, overlap
import visualisation
import visualisation.canvas_visualisation as visualisation

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import locale
import timeit
import math
import copy
import classes
import time
import helpers

district = classes.Map(360, 320)

def main(total_houses):

    # set number of each building type
    h_number = 0.6 * total_houses
    b_number = 0.25 * total_houses
    m_number = 0.15 * total_houses

    m_counter = 0
    b_counter, h_counter = 0, 0

    # bouw het eerste huis random, een maison wat die heeft de meeste waarde
    district.buildings, m_counter = m_build(district.buildings, m_counter)
    # print district.buildings

    while (m_counter < 5):

        maison = classes.Maison(0, 0)

        district.buildings.append(maison)
        print district.buildings
        # print building
        # print "begin", best_x, best_y
        top_score, best_x, best_y = walk_check(maison)
        maison.update(best_x, best_y)
        # print "na updata", best_x, best_y
        print district.buildings
        m_counter += 1
        visualisation.main(district.buildings, "test", "test", top_score, True)
        # print district.buildings
        # print("best: {}: {},{}".format(top_value, best_x, best_y))


# def check_value(buildings, building, top_value, best_x, best_y):
#
#     value = helpers.calculate_score(buildings)
#     if value > top_value:
#         # print value
#         top_value = value
#         # print "top value", top_value
#         best_x = building.left_bottom[0]
#         best_y = building.left_bottom[1]
#         # print best_x, best_y
#         #print top_value, best_x, best_y
#
#     return top_value, best_x, best_y

def check_possible(building):

    for build in district.buildings:
        # print "gebouw: ", build
        if build == building:
            continue

        olap = helpers.overlap(build, building)

        if olap:
            #print("overlapping {},{} : {},{}".format(building.left_bottom[0], building.left_bottom[1], building.left_bottom[0], building.left_bottom[0]))
            # print 'overlap'
            # print "gebouw 1 ", build.left_bottom[0], build.left_bottom[1]
            # print "gebouw 2 ", building.left_bottom[0], building.left_bottom[1]
            return False

        if not olap:
            #print("NOT         {},{} : {},{}".format(building.left_bottom[0], building.left_bottom[1], building.left_bottom[0], building.left_bottom[0]))
            return True

def walk_check(building):

    # zet direction op: naar rechts lopen
    direction = 1
    top_score = 0
    best_x = 0
    best_y = 0

    # begin met lopen
    while True:

        helpers.move(building, direction, 1)
        # # print building

        if building.right_top[0] >= 360:
            helpers.move(building, 2, 1)
            direction = -1
            continue
            # possible = check_possible(building)
            # if not possible:
            #     direction = 1
            #     continue
            #
            # top_value, best_x, best_y = check_value(district.buildings, building, top_value, best_x, best_y)
            # helpers.move(building, -1, 1)
            # top_value, best_x, best_y = check_value(buildings, building, top_value, best_x, best_y)


        if building.left_bottom[0] <= 0:
            helpers.move(building, 2, 1)
            direction = 1
            continue
            # possible = check_possible(building)
            # if not possible:
            #     direction = 1
            #     continue
            #
            # top_value, best_x, best_y = check_value(district.buildings, building, top_value, best_x, best_y)
            # helpers.move(building, 1, 1)
            # top_value, best_x, best_y = check_value(buildings, building, top_value, best_x, best_y)


        # bij 360, pakt hij hem niet. Later naar kijken, voor nu 359
        if building.right_top[1] >= 320 and building.right_top[0] >= 359:
            return top_score, best_x, best_y

        possible = check_possible(building)

        if possible:
            score = helpers.calculate_score(district.buildings)
            # print score
            if score > top_score:
                # print value
                top_score = score
                # print "top value", top_value
                best_x = building.left_bottom[0]

                best_y = building.left_bottom[1]
                print best_x, best_y



    # while (b_counter < b_number):
    #     top_value = 0
    #     best_x = 0
    #     best_y = 0
    #
    #     print("Bungalow:{}".format(b_counter + 1))
    #     print("")
    #
    #     bungalow = Classes.bungalow(0,0)
    #     buildings.append(bungalow)
    #
    #     top_value, best_x, best_y = walk_check(bungalow, buildings, top_value, best_x, best_y)
    #     move_to_best(bungalow, best_x, best_y)
    #     b_counter += 1
    #     plaatje(buildings)
    #
    #     print("best: {}: {},{}".format(top_value, best_x, best_y))
    #     print("")
    #
    # plaatje(buildings)
