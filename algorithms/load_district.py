
# import modules
import classes
import time
import os
from os import path

def main():

 ###############
    district = classes.Map(360, 320, 0)

    outpath = 'input_files'

    with open(path.join(outpath,'20.txt'), 'r') as f:
        data = f.readlines()

    for line in data:
        words = line.split()
        build = words[0]
        x = int(words[1])
        y = int(words[2])

        if build == 'maison':
            maison = classes.Maison(x, y)
            district.buildings.append(maison)
        elif build == 'bungalow':
            bungalow = classes.Bungalow(x, y)
            district.buildings.append(bungalow)
        elif build == 'house':
            house = classes.House(x, y)
            district.buildings.append(house)
##############
    # visualisation.print_canvas(district.buildings, "Jaap")

    value = district.score()

    return district, value
