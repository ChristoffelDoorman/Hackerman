# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file contains the expanding universe algorithm

# import files
from classes import *
from helpers import overlap, move, check_position, check_move

import math
import matplotlib.pyplot as plt

# import visualisation
# from classes import *
# from helpers import *

house_length = 20
house_width = 20
bungalow_length = 21
bungalow_width = 26
maison_length = 34
maison_width = 33

def set_initial_map(total_houses):

    district = Map(360, 320, 0)


    # set number of each building type
    h_number = int(0.6 * total_houses)
    b_number = int(0.25 * total_houses)
    m_number = int(0.15 * total_houses)

    # build houses in middle of map
    grid_size = int(math.ceil(math.sqrt(h_number)))
    counter = 0
    for i in range(grid_size):

        x = (district.width - (house_width * (grid_size - (2.2 * i)))) / 2


        for j in range(grid_size):

            if counter == h_number:
                break

            y = (district.height + (house_length * (grid_size - 2.2 - (2 * j)))) / 2

            counter += 1
            house = House(x, y)
            district.buildings.append(house)

    # place bungalows around houses
    r = (house_width / 2) * (grid_size + 1)
    t = ((2 * math.pi) / (b_number))

    for i in range(b_number):

        x = ((district.width - bungalow_width) / 2) + r * math.cos(t * i)
        y = ((district.height - bungalow_length) / 2) + r * math.sin(t * i)

        bungalow = Bungalow(x, y)
        for building in district.buildings:
            olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] <= district.width / 2) and (bungalow.left_bottom[1] >= district.height / 2) and olap:
                while olap:
                    bungalow = move(bungalow, -1 , 10)
                    bungalow = move(bungalow, 2, 10)
                    olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] <= district.width / 2) and (bungalow.left_bottom[1] < district.height / 2) and olap:
                while olap:
                    bungalow = move(bungalow, -1, 10)
                    bungalow = move(bungalow, -2, 10)
                    olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] > district.width / 2) and (bungalow.left_bottom[1] <= district.height / 2) and olap:
                while olap:
                    bungalow = move(bungalow, 1, 10)
                    bungalow = move(bungalow, -2, 10)
                    olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] > district.width / 2) and (bungalow.left_bottom[1] > district.height / 2) and olap:
                while olap:
                    bungalow = move(bungalow, 1, 10)
                    bungalow = move(bungalow, 2, 10)
                    olap = overlap(bungalow, building)

        district.buildings.append(bungalow)

    # yw1 = (district.height / 2) + ((grid_size / 2) * house_width) + bungalow_length
    # yw2 = district.height - yw1 - 43
    # xw1 = 110
    # xw3 = (district.width / 2) - ((grid_size / 2) * house_width) - 40.232 - bungalow_width
    # yw3 = 88.5
    # xw4 = district.width - xw3 - 20
    #
    # water1 = Water(xw1, yw1, 151.789, 37.947)
    # district.waters.append(water1)
    # water2 = Water(xw1, yw2, 151.789, 37.947)
    # district.waters.append(water2)
    # water3 = Water(xw3, yw3, 40.232, 143.045)
    # district.waters.append(water3)
    # water4 = Water(xw4, yw3, 40.232, 143.045)
    # district.waters.append(water4)


    # place maisons around bungalows
    r = (house_width / 2) * (grid_size + 1) + bungalow_width
    t = ((2 * math.pi) / (m_number))
    for i in range(m_number):

        x = ((district.width - maison_width) / 2) + r * math.cos(t * i)
        y = ((district.height - maison_length) / 2) + r * math.sin(t * i)

        maison = Maison(x, y)
        for building in district.buildings:
            olap = overlap(maison, building)

            # buildings linksboven
            if (maison.left_bottom[0] <= district.width / 2) and (maison.left_bottom[1] >= district.height / 2) and olap:
                while maison.left_top[0] >= 0 and maison.left_top[1] <= district.height:
                    maison = move(maison, -1, 1)
                    maison = move(maison, 2, 1)

            # buildings linksonder
            if (maison.left_bottom[0] <= district.width / 2) and (maison.left_bottom[1] < district.height / 2) and olap:
                while maison.left_bottom[0] >= 0 and maison.left_bottom[1] >=0:
                    maison = move(maison, -1, 1)
                    maison = move(maison, -2, 1)

            # buildings rechtsonder
            if (maison.left_bottom[0] > district.width / 2) and (maison.left_bottom[1] <= district.height / 2) and olap:
                while maison.right_bottom[0] <= district.width and maison.right_bottom[1] >= 0:
                    maison = move(maison, 1, 1)
                    maison = move(maison, -2, 1)

            # buildings rechtsboven
            if (maison.left_bottom[0] > district.width / 2) and (maison.left_bottom[1] > district.height / 2) and olap:
                while maison.right_top[0] <= district.width and maison.right_top[1] <= district.height:
                    maison = move(maison, 1, 1)
                    maison = move(maison, 2, 1)


        district.buildings.append(maison)

    return district

def expand(building, buildings, steps, stepsize):

    for i in range(steps):

        # negative horizontal axis
        if (building.right_top[0] < (district.width / 2)) \
        and (building.right_top[1] >= (district.height / 2)) \
        and (building.right_bottom[1] <= (district.height / 2)):
            a = abs(building.right_bottom[0] - (district.width / 2))
            exp_stepsize = stepsize * (a / 100)
            # possible, move_score = check_move(building, buildings, -1, exp_stepsize)
            if True:
                building = move(building, -1, exp_stepsize)

        # positive vertical axis
        if (building.left_bottom[1] > (district.height / 2)) \
        and (building.left_bottom[0] <= (district.width / 2)) \
        and (building.right_bottom[0] >= (district.width / 2)):
            c = building.left_top[1] - (district.height / 2)
            exp_stepsize = stepsize * (c / 100)
            # possible, move_score = check_move(building, buildings, 2, exp_stepsize)
            if True:
                building = move(building, 2, exp_stepsize)

        # positive horizontal axis
        if (building.left_top[0] > (district.width / 2)) \
        and (building.left_top[1] >= (district.height / 2)) \
        and (building.left_bottom[1] <= (district.height / 2)):
            a = building.left_bottom[0] - (district.width / 2)
            exp_stepsize = stepsize * (a / 100)
            # possible, move_score = check_move(building, buildings, 1, exp_stepsize)
            if True:
                building = move(building, 1, exp_stepsize)

        # negative vertical axis
        if (building.left_top[1] < (district.height / 2)) \
        and (building.left_top[0] <= (district.width / 2)) \
        and (building.right_top[0] >= (district.width / 2)):
            c = abs(building.left_bottom[1] - (district.height / 2))
            exp_stepsize = stepsize * (c / 100)
            # possible, move_score = check_move(building, buildings, -2, exp_stepsize)
            if True:
                building = move(building, -2, exp_stepsize)

        # buildings in top-right area, move rigth up
        if (building.left_bottom[0] >= district.width / 2) \
        and (building.left_bottom[1] >= district.height / 2):
            a = building.left_bottom[0] - (district.width / 2)
            c = building.left_bottom[1] - (district.height / 2)
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, 2, 1, dy, dx)
            if True:
                building = move(building, 2, dy)
                building = move(building, 1, dx)

        # buildings in lower-right area, move rigth down
        if (building.left_top[0] >= district.width / 2) \
        and (building.left_top[1] <= district.height / 2):
            a = building.left_top[0] - (district.width / 2)
            c = abs(building.left_top[1] - (district.height / 2))
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, -2, 1, dy, dx)
            if True:
                building = move(building, -2, dy)
                building = move(building, 1, dx)

        # buildings in down-left area, move left down
        if (building.right_top[0] <= district.width / 2) \
        and (building.right_top[1] <= district.height / 2):
            a = abs(building.left_top[0] - (district.width / 2))
            c = abs(building.left_top[1] - (district.height / 2))
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, -2, -1, dy, dx)
            if True:
                building = move(building, -2, dy)
                building = move(building, -1, dx)

        # buildings in left-up area, move left up
        if (building.right_bottom[0] <= district.width / 2) \
        and (building.right_bottom[1] >= district.height / 2):
            a = abs(building.right_bottom[0] - (district.width / 2))
            c = building.right_bottom[1] - (district.height / 2)
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, 2, -1, dy, dx)
            if True:
                building = move(building, 2, dy)
                building = move(building, -1, dx)


    return building

def main(total_houses):

    district = set_initial_map(total_houses)

    # for building in district.buildings:
    #     expand(building, district.buildings, 10, 1)

    # for building in buildings:
    #     if building.name == "maison":
    #         expand(building, 20)
    #
    # for building in buildings:
    #     if building.name == "bungalow":
    #         expand(building, 20)
    #
    # for building in buildings:
    #     if building.name == "house":
    #         expand(building, 20)

    return district
