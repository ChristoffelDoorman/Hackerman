# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file contains the greedy algorithm.



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


# House's 24
# Bungalow's 10
# Maison' s 6


district = classes.Map(360, 320, 0)

maison = classes.Maison(0, 286)
district.buildings.append(maison)

maison = classes.Maison(327, 0)
district.buildings.append(maison)

maison = classes.Maison(327, 286)
district.buildings.append(maison)

###
maison = classes.Maison(180, 286)
district.buildings.append(maison)

maison = classes.Maison(327, 190)
district.buildings.append(maison)

maison = classes.Maison(150, 150)
district.buildings.append(maison)
###

house = classes.House(0,0)
district.buildings.append(house)

house = classes.House(22,0)
district.buildings.append(house)

house = classes.House(44,0)
district.buildings.append(house)

house = classes.House(66,0)
district.buildings.append(house)

house = classes.House(88,0)
district.buildings.append(house)

house = classes.House(110,0)
district.buildings.append(house)
###

house = classes.House(0,22)
district.buildings.append(house)

house = classes.House(22,22)
district.buildings.append(house)

house = classes.House(44,22)
district.buildings.append(house)

house = classes.House(66,22)
district.buildings.append(house)

house = classes.House(88,22)
district.buildings.append(house)

house = classes.House(110,22)
district.buildings.append(house)

####

house = classes.House(0,44)
district.buildings.append(house)

house = classes.House(22,44)
district.buildings.append(house)

house = classes.House(44,44)
district.buildings.append(house)

house = classes.House(66,44)
district.buildings.append(house)

house = classes.House(88,44)
district.buildings.append(house)

house = classes.House(110,44)
district.buildings.append(house)

####

house = classes.House(0,66)
district.buildings.append(house)

house = classes.House(22,66)
district.buildings.append(house)

house = classes.House(44,66)
district.buildings.append(house)

house = classes.House(66,66)
district.buildings.append(house)

house = classes.House(88,66)
district.buildings.append(house)

house = classes.House(110,66)
district.buildings.append(house)

###

bungalow = classes.Bungalow(0, 90)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(30, 90)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(60,90)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(0, 115)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(30, 115)
district.buildings.append(bungalow)
##
bungalow = classes.Bungalow(60, 115)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(0, 140)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(30 ,140)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(60, 140)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(135, 0)
district.buildings.append(bungalow)
###

value = district.score()

visualisation.main(district, "testen", "40", value, 0, "1", 0, 0)

# print_txt(district.buildings)
