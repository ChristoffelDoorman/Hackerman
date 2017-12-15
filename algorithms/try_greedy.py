# import files
from helpers import h_build, b_build, m_build, calculate_score, move, overlap, check_move
import visualisation
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

district = classes.Map(360, 320)

def main(total_houses):

    # set number of each building type
    h_number = int(0.6 * total_houses)
    b_number = int(0.25 * total_houses)
    m_number = int(0.15 * total_houses)

    # bouw het eerste huis random, een maison wat die heeft de meeste waarde
    district.buildings, m_counter = m_build(district.buildings, 0)
    # maison = classes.Maison(0,0)
    # district.buildings.append(maison)
    # print district.buildings

    for i in range(m_number - 1):

        maison = classes.Maison(0, 0)

        district.buildings.append(maison)
        top_score, best_x, best_y = walk_check(maison)
        maison.update(best_x, best_y)
        visualisation.main(district.buildings, "test", "test", top_score, True)


    for i in range(b_number):

        bungalow = classes.Bungalow(0, 0)

        district.buildings.append(bungalow)
        top_score, best_x, best_y = walk_check(bungalow)
        bungalow.update(best_x, best_y)
        visualisation.main(district.buildings, "test", "test", top_score, True)


    for i in range(h_number):

        house = classes.House(0, 0)

        district.buildings.append(house)
        top_score, best_x, best_y = walk_check(house)
        house.update(best_x, best_y)
        visualisation.main(district.buildings, "test", "test", top_score, True)


    visualisation.main(district.buildings, "test", "test", top_score, True)



def check_possible(building):

    for build in district.buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            return False

    if not olap:
        return True

def walk_check(building):

    # zet direction op: naar rechts lopen
    direction = 1
    top_score = 0
    best_x = 0
    best_y = 0
    best_scores = {}
    # begin met lopen
    while True:

        move(building, direction, 1)

        if building.right_top[0] >= 360:
            move(building, 2, 1)
            direction = -1
            continue

        if building.left_bottom[0] <= 0:
            move(building, 2, 1)
            direction = 1
            continue

        possible = check_possible(building)
        if possible:
            score = calculate_score(district.buildings)
            # print score
            if score > top_score:
                # print value
                top_score = score
                # print "top value", top_value

                best_x = building.left_bottom[0]

                best_y = building.left_bottom[1]
                # print "beste: ", best_x, best_y

        # bij 360, pakt hij hem niet. Later naar kijken, voor nu 359
        if building.right_top[1] >= 320 and building.right_top[0] >= 359:
            print "return: ", best_x, best_y
            return top_score, best_x, best_y
