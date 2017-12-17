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

def main():

 ###############
    with open('greedy-40.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        words = line.split()
        build = words[0]
        x = int(words[1])
        y = int(words[2])

        if build == 'mais':
            maison = classes.Maison(x, y)
            district.buildings.append(maison)
        elif build == 'bung':
            bungalow = classes.Bungalow(x, y)
            district.buildings.append(bungalow)
        elif build == 'hous':
            house = classes.House(x, y)
            district.buildings.append(house)
##############
    # visualisation.print_canvas(district.buildings, "Jaap")

    value = district.score()
    
    return district.buildings, value
