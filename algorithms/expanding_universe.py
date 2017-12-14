# import files
from classes import *
from helpers import overlap, move, check_position, check_move

import math
import matplotlib.pyplot as plt

# import visualisation
# from classes import *
# from helpers import *

X_DIMENSION = 360
Y_DIMENSION = 320

def set_initial_map(total_houses):

    # create list of buildings
    buildings = []

    # set number of each building type
    h_number = int(0.6 * total_houses)
    b_number = int(0.25 * total_houses)
    m_number = int(0.15 * total_houses)

    # build houses in middle of map
    grid_size = int(math.ceil(math.sqrt(h_number)))
    counter = 0
    for i in range(grid_size):

        x = (X_DIMENSION - (House.width * (grid_size - (2.2 * i)))) / 2


        for j in range(grid_size):

            if counter == h_number:
                break

            y = (Y_DIMENSION + (House.length * (grid_size - 2.2 - (2 * j)))) / 2

            counter += 1
            house = House(x, y)
            buildings.append(house)

    # place bungalows around houses
    r = (House.width / 2) * (grid_size + 1)
    t = ((2 * math.pi) / (b_number))

    for i in range(b_number):

        x = ((X_DIMENSION - Bungalow.width) / 2) + r * math.cos(t * i)
        y = ((Y_DIMENSION - Bungalow.length) / 2) + r * math.sin(t * i)

        bungalow = Bungalow(x, y)
        for building in buildings:
            olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] <= X_DIMENSION / 2) and (bungalow.left_bottom[1] >= Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = move(bungalow, -1 , 1)
                    bungalow = move(bungalow, 2, 1)
                    olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] <= X_DIMENSION / 2) and (bungalow.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = move(bungalow, -1, 1)
                    bungalow = move(bungalow, -2, 1)
                    olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] > X_DIMENSION / 2) and (bungalow.left_bottom[1] <= Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = move(bungalow, 1, 1)
                    bungalow = move(bungalow, -2, 1)
                    olap = overlap(bungalow, building)

            if (bungalow.left_bottom[0] > X_DIMENSION / 2) and (bungalow.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = move(bungalow, 1, 1)
                    bungalow = move(bungalow, 2, 1)
                    olap = overlap(bungalow, building)

        buildings.append(bungalow)

    # place maisons around bungalows
    r = (House.width / 2) * (grid_size + 1) + Bungalow.width
    t = ((2 * math.pi) / (m_number))
    for i in range(m_number):

        x = ((X_DIMENSION - Maison.width) / 2) + r * math.cos(t * i)
        y = ((Y_DIMENSION - Maison.length) / 2) + r * math.sin(t * i)

        maison = Maison(x, y)
        for building in buildings:
            olap = overlap(maison, building)

            if (maison.left_bottom[0] <= X_DIMENSION / 2) and (maison.left_bottom[1] >= Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = move(maison, -1, 1)
                    maison = move(maison, 2, 1)
                    olap = overlap(maison, building)

            if (maison.left_bottom[0] <= X_DIMENSION / 2) and (maison.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = move(maison, -1, 1)
                    maison = move(maison, -2, 1)
                    olap = overlap(maison, building)

            if (maison.left_bottom[0] > X_DIMENSION / 2) and (maison.left_bottom[1] <= Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = move(maison, 1, 1)
                    maison = move(maison, -2, 1)
                    olap = overlap(maison, building)

            if (maison.left_bottom[0] > X_DIMENSION / 2) and (maison.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = move(maison, 1, 1)
                    maison = move(maison, 2, 1)
                    olap = overlap(maison, building)

        buildings.append(maison)


    return buildings

def expand(building, buildings, steps, stepsize):

    for i in range(steps):

        # negative horizontal axis
        if (building.right_top[0] < (X_DIMENSION / 2)) \
        and (building.right_top[1] >= (Y_DIMENSION / 2)) \
        and (building.right_bottom[1] <= (Y_DIMENSION / 2)):
            a = abs(building.right_bottom[0] - (X_DIMENSION / 2))
            exp_stepsize = stepsize * (a / 100)
            # possible, move_score = check_move(building, buildings, -1, exp_stepsize)
            if True:
                building = move(building, -1, exp_stepsize)

        # positive vertical axis
        if (building.left_bottom[1] > (Y_DIMENSION / 2)) \
        and (building.left_bottom[0] <= (X_DIMENSION / 2)) \
        and (building.right_bottom[0] >= (X_DIMENSION / 2)):
            c = building.left_top[1] - (Y_DIMENSION / 2)
            exp_stepsize = stepsize * (c / 100)
            # possible, move_score = check_move(building, buildings, 2, exp_stepsize)
            if True:
                building = move(building, 2, exp_stepsize)

        # positive horizontal axis
        if (building.left_top[0] > (X_DIMENSION / 2)) \
        and (building.left_top[1] >= (Y_DIMENSION / 2)) \
        and (building.left_bottom[1] <= (Y_DIMENSION / 2)):
            a = building.left_bottom[0] - (X_DIMENSION / 2)
            exp_stepsize = stepsize * (a / 100)
            # possible, move_score = check_move(building, buildings, 1, exp_stepsize)
            if True:
                building = move(building, 1, exp_stepsize)

        # negative vertical axis
        if (building.left_top[1] < (Y_DIMENSION / 2)) \
        and (building.left_top[0] <= (X_DIMENSION / 2)) \
        and (building.right_top[0] >= (X_DIMENSION / 2)):
            c = abs(building.left_bottom[1] - (Y_DIMENSION / 2))
            exp_stepsize = stepsize * (c / 100)
            # possible, move_score = check_move(building, buildings, -2, exp_stepsize)
            if True:
                building = move(building, -2, exp_stepsize)

        # buildings in top-right area, move rigth up
        if (building.left_bottom[0] >= X_DIMENSION / 2) \
        and (building.left_bottom[1] >= Y_DIMENSION / 2):
            a = building.left_bottom[0] - (X_DIMENSION / 2)
            c = building.left_bottom[1] - (Y_DIMENSION / 2)
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, 2, 1, dy, dx)
            if True:
                building = move(building, 2, dy)
                building = move(building, 1, dx)

        # buildings in lower-right area, move rigth down
        if (building.left_top[0] >= X_DIMENSION / 2) \
        and (building.left_top[1] <= Y_DIMENSION / 2):
            a = building.left_top[0] - (X_DIMENSION / 2)
            c = abs(building.left_top[1] - (Y_DIMENSION / 2))
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, -2, 1, dy, dx)
            if True:
                building = move(building, -2, dy)
                building = move(building, 1, dx)

        # buildings in down-left area, move left down
        if (building.right_top[0] <= X_DIMENSION / 2) \
        and (building.right_top[1] <= Y_DIMENSION / 2):
            a = abs(building.left_top[0] - (X_DIMENSION / 2))
            c = abs(building.left_top[1] - (Y_DIMENSION / 2))
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, -2, -1, dy, dx)
            if True:
                building = move(building, -2, dy)
                building = move(building, -1, dx)

        # buildings in left-up area, move left up
        if (building.right_bottom[0] <= X_DIMENSION / 2) \
        and (building.right_bottom[1] >= Y_DIMENSION / 2):
            a = abs(building.right_bottom[0] - (X_DIMENSION / 2))
            c = building.right_bottom[1] - (Y_DIMENSION / 2)
            dy = ((math.sqrt(a**2 + c**2) / 100) * stepsize) / (1 + math.sqrt((a**2) / (c**2)))
            dx = (a / c) * dy
            # possible, move_score = check_position(building, buildings, 2, -1, dy, dx)
            if True:
                building = move(building, 2, dy)
                building = move(building, -1, dx)


    return building

def main(total_houses):

    buildings = set_initial_map(total_houses)

    for building in buildings:
        expand(building, buildings, 25, 1)

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


    return buildings
