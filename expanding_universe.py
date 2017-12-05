import math
import matplotlib.pyplot as plt

import visualisation
import classes

X_DIMENSION = 360
Y_DIMENSION = 320

def main(total_houses):

    # create list of buildings
    buildings = []

    # set number of each building type
    h_number = 0.6 * total_houses
    b_number = 0.25 * total_houses
    m_number = 0.15 * total_houses

    grid_size = int(math.ceil(math.sqrt(h_number)))
    print grid_size
    counter = 0
    for i in range(grid_size):
        x = (X_DIMENSION / 2) + classes.House.width * (i - (grid_size / 2))

        for j in range(grid_size):

            if counter == h_number:
                break

            y = (Y_DIMENSION / 2) + (classes.House.length * ((grid_size / 2) - j))

            counter += 1
            house = classes.House(x, y)
            buildings.append(house)

    

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.set_xlim(0, 360)
    ax1.set_ylim(0, 320)

    for building in buildings:
        visualisation.drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'red')

    # safe figure
    fig1.savefig('expanding_universe.png', dpi=90, bbox_inches='tight')
