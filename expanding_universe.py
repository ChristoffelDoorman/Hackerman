import math
import matplotlib.pyplot as plt

import visualisation
import classes
import helpers

X_DIMENSION = 360
Y_DIMENSION = 320

def main(total_houses):

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

        x = (X_DIMENSION - (classes.House.width * (grid_size - (2 * i)))) / 2


        for j in range(grid_size):

            if counter == h_number:
                break

            y = (Y_DIMENSION + (classes.House.length * (grid_size - 2 - (2 * j)))) / 2

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

            if (bungalow.left_bottom[0] < X_DIMENSION / 2) and (building.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'left')
                    bungalow = helpers.move(bungalow, 'up')
                    olap = helpers.overlap(bungalow, building)

            if (bungalow.left_bottom[0] < X_DIMENSION / 2) and (building.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'left')
                    bungalow = helpers.move(bungalow, 'down')
                    olap = helpers.overlap(bungalow, building)

            if (bungalow.left_bottom[0] > X_DIMENSION / 2) and (building.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'right')
                    bungalow = helpers.move(bungalow, 'down')
                    olap = helpers.overlap(bungalow, building)

            if (bungalow.left_bottom[0] > X_DIMENSION / 2) and (building.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    bungalow = helpers.move(bungalow, 'right')
                    bungalow = helpers.move(bungalow, 'up')
                    olap = helpers.overlap(bungalow, building)

        buildings.append(bungalow)


    r = (classes.House.width / 2) * (grid_size + 1) + classes.Bungalow.width
    t = ((2 * math.pi) / (m_number))
    for i in range(m_number):

        x = ((X_DIMENSION - classes.Maison.width) / 2) + r * math.cos(t * i)
        y = ((Y_DIMENSION - classes.Maison.length) / 2) + r * math.sin(t * i)

        maison = classes.Maison(x, y)
        for building in buildings:
            olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] < X_DIMENSION / 2) and (building.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'left')
                    maison = helpers.move(maison, 'up')
                    olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] < X_DIMENSION / 2) and (building.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'left')
                    maison = helpers.move(maison, 'down')
                    olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] > X_DIMENSION / 2) and (building.left_bottom[1] < Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'right')
                    maison = helpers.move(maison, 'down')
                    olap = helpers.overlap(maison, building)

            if (maison.left_bottom[0] > X_DIMENSION / 2) and (building.left_bottom[1] > Y_DIMENSION / 2) and olap:
                while olap == True:
                    maison = helpers.move(maison, 'right')
                    maison = helpers.move(maison, 'up')
                    olap = helpers.overlap(maison, building)

        buildings.append(maison)


    # for building in buildings:
    #     if building.name == 'bungalow':
    #
    #         bungalow = building
    #
    #         for building in buildings:
    #             olap = True
    #
    #             while olap:
    #                 olap = helpers.overlap(bungalow, building)
    #
    #                 if (bungalow.left_bottom[0] < X_DIMENSION / 2) and (building.left_bottom[1] > Y_DIMENSION / 2) and olap:
    #
    #                         bungalow1 = helpers.move(bungalow, 'left')
    #                         bungalow = helpers.move(bungalow1, 'up')
    #
    #                 else:
    #                     break



    # while len(buildings) < (h_number + b_number):
    #
    #     for building in buildings:
    #         if building.right_top[0] > (X_DIMENSION / 2)

    # b_side = int(math.ceil(b_number / 4.0))
    #
    # r = (grid_size / 2) * math.sqrt(2) * classes.House.width + 30
    # t = ((2 * math.pi) / (b_number))
    # xlist = []
    # ylist = []
    # print b_number
    # for i in range(b_side):
    #     angle = math.atan(math.tan(t * i - (math.pi / 4)))
    #     x = (X_DIMENSION + classes.House.width * grid_size) / 2
    #     y = (Y_DIMENSION + (math.tan(angle) * classes.House.width * grid_size)) / 2
    #
    #     # r = math.sqrt(((grid_size / 2) * classes.House.width)**2 + (i * classes.House.length)**2)
    #
    #     # x = ((X_DIMENSION - classes.House.width) / 2) + r * math.cos(t * i)
    #     # y = ((Y_DIMENSION - classes.House.length) / 2) + r * math.sin(t * i)
    #
    #     bungalow = classes.Bungalow(x, y)
    #     buildings.append(bungalow)
    #
    #     # x = math.cos(t * i - (math.pi / 4))
    #     # y = math.sin(t * i - (math.pi / 4))
    #     print "x=", x, "y=", y, "angle=", math.tan(angle)
    #     angle =  math.atan(abs(y / x)) * 57.2
    #     print "angle=", angle
    #     b = math.atan(math.tan(t * i - (math.pi / 4)))
    #     print "andere angle=", b
    #     xlist.append(x)
    #     ylist.append(y)

        # print b

    # plt.plot(xlist, ylist, 'ro')
    # plt.axis([min(xlist), max(xlist), min(ylist), max(ylist)])
    # plt.show()





    return buildings
