# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file saves results from runned algorithms in a .txt file.
# This way, the results can be used for further purposes, like
# extra hillclimber treatments.

# import modules
import classes
import time
import os
from os import path

def main():

    # initialize map class
    district = classes.Map(360, 320, 0)

    # outputfile
    outpath = 'input_files'

<<<<<<< HEAD
    with open(path.join(outpath,'60.txt'), 'r') as f:
=======
    with open(path.join(outpath,'hillclimber_20_2017-12-21-11-30-13_random.txt'), 'r') as f:
>>>>>>> 8aac176e29c09a8d772db26bbfc39f327423377d
        data = f.readlines()

    # manipulate data to format
    for line in data:
        words = line.split()
        build = words[0]
        x = float(words[1])
        y = float(words[2])

        if build == 'maison':
            maison = classes.Maison(x, y)
            district.buildings.append(maison)
        elif build == 'bungalow':
            bungalow = classes.Bungalow(x, y)
            district.buildings.append(bungalow)
        elif build == 'house':
            house = classes.House(x, y)
            district.buildings.append(house)

    value = district.score()

    return district, value
