import math
import matplotlib.pyplot as plt

import visualisation
import classes
import helpers
import hillclimber_algoritm

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

        x = (X_DIMENSION - (classes.House.width * (grid_size - (2.7 * i)))) / 2


        for j in range(grid_size):

            if counter == h_number:
                break

            y = (Y_DIMENSION + (classes.House.length * (grid_size - 2 - (2.7 * j)))) / 2

            counter += 1
            house = classes.House(x, y)
            buildings.append(house)

    # place bungalows around houses
    r = (classes.House.width / 2) * (grid_size + 1)
    t = ((2 * math.pi) / (b_number))

    for i in range(b_number):

        x = ((X_DIMENSION - classes.Bungalow.width) / 2) + r * math.cos(t * i)
        y = ((Y_DIMENSION - classes.Bungalow.length) / 2) + r * math.sin(t * i)

        bungalow = classes.Bungalow(x, y)
        for building in buildings:
            olap = helpers.overlap(bungalow, building)

            if (bungalow.left_bottom[0] <= X_DIMENSION / 2) and (bungalow.left_bottom[1] >= Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'left', 10)
                    bungalow = helpers.move(bungalow, 'up', 10)
                    olap = helpers.overlap(bungalow, building)

            if (bungalow.left_bottom[0] <= X_DIMENSION / 2) and (bungalow.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'left', 10)
                    bungalow = helpers.move(bungalow, 'down', 10)
                    olap = helpers.overlap(bungalow, building)

            if (bungalow.left_bottom[0] > X_DIMENSION / 2) and (bungalow.left_bottom[1] <= Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'right', 10)
                    bungalow = helpers.move(bungalow, 'down', 10)
                    olap = helpers.overlap(bungalow, building)

            if (bungalow.left_bottom[0] > X_DIMENSION / 2) and (bungalow.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'right', 10)
                    bungalow = helpers.move(bungalow, 'up', 10)
                    olap = helpers.overlap(bungalow, building)

        buildings.append(bungalow)

    # place maisons around bungalows
    r = (classes.House.width / 2) * (grid_size + 1) + classes.Bungalow.width
    t = ((2 * math.pi) / (m_number))
    for i in range(m_number):

        x = ((X_DIMENSION - classes.Maison.width) / 2) + r * math.cos(t * i)
        y = ((Y_DIMENSION - classes.Maison.length) / 2) + r * math.sin(t * i)

        maison = classes.Maison(x, y)
        for building in buildings:
            olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] <= X_DIMENSION / 2) and (maison.left_bottom[1] >= Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'left', 15)
                    maison = helpers.move(maison, 'up', 15)
                    olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] <= X_DIMENSION / 2) and (maison.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'left', 15)
                    maison = helpers.move(maison, 'down', 15)
                    olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] > X_DIMENSION / 2) and (maison.left_bottom[1] <= Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'right', 15)
                    maison = helpers.move(maison, 'down', 15)
                    olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] > X_DIMENSION / 2) and (maison.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'right', 15)
                    maison = helpers.move(maison, 'up', 15)
                    olap = helpers.overlap(maison, building)

        buildings.append(maison)


    return buildings

def expand(building, steps):

    for i in range(steps):

        if (building.name == building.name) and (building.left_top[0] < X_DIMENSION / 2) and (building.left_top[1] > Y_DIMENSION / 2):
            r_middle = helpers.pythagoras((X_DIMENSION / 2), building.right_bottom[0], building.right_bottom[1], (Y_DIMENSION / 2))
            building = helpers.move(building, 'left', r_middle / 80)
            building = helpers.move(building, 'up', r_middle / 80)

        if (building.name == building.name) and (building.left_bottom[0] < X_DIMENSION / 2) and (building.left_bottom[1] < Y_DIMENSION / 2):
            r_middle = helpers.pythagoras((X_DIMENSION / 2), building.right_top[0], building.right_top[1], (Y_DIMENSION / 2))
            building = helpers.move(building, 'left', r_middle / 80)
            building = helpers.move(building, 'down', r_middle / 80)

        if (building.name == building.name) and (building.right_top[0] > X_DIMENSION / 2) and (building.right_top[1] > Y_DIMENSION / 2):
            r_middle = helpers.pythagoras((X_DIMENSION / 2), building.left_bottom[0], building.left_bottom[1], (Y_DIMENSION / 2))
            building = helpers.move(building, 'up', r_middle / 80)
            building = helpers.move(building, 'right', r_middle / 80)

        if (building.name == building.name) and (building.right_bottom[0] > X_DIMENSION / 2) and (building.right_bottom[1] < Y_DIMENSION / 2):
            r_middle = helpers.pythagoras((X_DIMENSION / 2), building.left_top[0], building.left_top[1], (Y_DIMENSION / 2))
            building = helpers.move(building, 'right', r_middle / 80)
            building = helpers.move(building, 'down', r_middle / 80)

    return building

def main(total_houses):

    buildings = set_initial_map(total_houses)

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
