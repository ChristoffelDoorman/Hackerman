# import files
from helpers import h_build, b_build, m_build, print_txt
import visualisation.canvas_visualisation as visualisation
import classes

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import locale
import time
import math
import copy
import math

district = classes.Map(360, 320, 0)

maison = classes.Maison(0, 286)
district.buildings.append(maison)

maison = classes.Maison(327, 0)
district.buildings.append(maison)

maison = classes.Maison(327, 286)
district.buildings.append(maison)

house = classes.House(0,0)
district.buildings.append(house)

house = classes.House(22,0)
district.buildings.append(house)

house = classes.House(44,0)
district.buildings.append(house)

house = classes.House(66,0)
district.buildings.append(house)

house = classes.House(0,22)
district.buildings.append(house)

house = classes.House(22,22)
district.buildings.append(house)

house = classes.House(44,22)
district.buildings.append(house)

house = classes.House(66,22)
district.buildings.append(house)

house = classes.House(0,44)
district.buildings.append(house)

house = classes.House(22,44)
district.buildings.append(house)

house = classes.House(44,44)
district.buildings.append(house)

house = classes.House(66,44)
district.buildings.append(house)

bungalow = classes.Bungalow(89, 0)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(89, 29)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(0, 69)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(34, 69)
district.buildings.append(bungalow)

bungalow = classes.Bungalow(89, 69)
district.buildings.append(bungalow)

value = district.score()

visualisation.main(district, "testen", "20", value, 0, "1", 0, 0)

print_txt(district.buildings)
