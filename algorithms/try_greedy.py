# import files
from helpers import h_build, b_build, m_build, calculate_score, move, overlap
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

X_DIMENSION = 360
Y_DIMENSION = 320

def main(total_houses):
    buildings = []

    # set number of each building type
    h_number = 0.6 * total_houses
    b_number = 0.25 * total_houses
    m_number = 0.15 * total_houses

    m_counter = 0
    b_counter, h_counter = 0, 0


    # bouw het eerste huis random, een maison wat die heeft de meeste waarde
    buildings, m_counter = m_build(buildings, m_counter)

    while (m_counter < 3):

        top_value = 0
        best_x = 0
        best_y = 0

        building = classes.Maison(0, 0)
        buildings.append(building)
        print building
        print "begin", best_x, best_y
        top_value, best_x, best_y = walk_check(building, buildings)

        building.update(best_x, best_y)
        print "na updata", best_x, best_y

        m_counter += 1
        plaatje(buildings)
        print("best: {}: {},{}".format(top_value, best_x, best_y))

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


def plaatje(buildings):
    visualisation.print_canvas(buildings, 'try_greedy')

def check_value(buildings, building, top_value, best_x, best_y):

    value = helpers.calculate_score(buildings)
    if value > top_value:
        top_value = value
        print "top value", top_value
        best_x = building.left_bottom[0]
        best_y = building.left_bottom[1]

        #print top_value, best_x, best_y

    return top_value, best_x, best_y

def check_possible(building, buildings):

    for build in buildings:

        if build == building:
                continue

        overlapping = helpers.overlap(build ,building)

        if overlapping:
            #print("overlapping {},{} : {},{}".format(building.left_bottom[0], building.left_bottom[1], building.left_bottom[0], building.left_bottom[0]))
            print 'overlap'
            print "gebouw 1 ", building.left_bottom[0], building.left_bottom[1]
            print "gebouw 2 ", build.left_bottom[0], build.left_bottom[1]
            return False

        if not overlapping:
            #print("NOT         {},{} : {},{}".format(building.left_bottom[0], building.left_bottom[1], building.left_bottom[0], building.left_bottom[0]))
            return True

def walk_check(building, buildings):

    # zet direction op: naar rechts lopen
    direction = 1
    top_value = 0
    best_x = 0
    best_y = 0

    # begin met lopen
    while True:

        helpers.move(building, direction, 1)
        possible = check_possible(building, buildings)
        if not possible:
            continue

        top_value, best_x, best_y = check_value(buildings, building, top_value, best_x, best_y)
        # # print building

        if building.right_top[0] >= 360:
            helpers.move(building, 2, 1)
            possible = check_possible(building, buildings)
            if not possible:
                direction = 1
                continue

            top_value, best_x, best_y = check_value(buildings, building, top_value, best_x, best_y)
            # helpers.move(building, -1, 1)
            # top_value, best_x, best_y = check_value(buildings, building, top_value, best_x, best_y)
            direction = -1

        if building.left_bottom[0] <= 0:
            helpers.move(building, 2, 1)
            possible = check_possible(building, buildings)
            if not possible:
                direction = 1
                continue
            top_value, best_x, best_y = check_value(buildings, building, top_value, best_x, best_y)
            # helpers.move(building, 1, 1)
            # top_value, best_x, best_y = check_value(buildings, building, top_value, best_x, best_y)
            direction = 1

        # bij 360, pakt hij hem niet. Later naar kijken, voor nu 359
        if building.right_top[1] >= 320 and building.right_top[0] >= 359:
            break

    return top_value, best_x, best_y
