# import files
from classes import Map
from helpers import h_build, b_build, m_build, calculate_score
import visualisation
import visualisation.canvas_visualisation as visualisation

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import locale
import timeit
import math
import copy
import classes
import time
import helpers

district = Map(320, 360)


def main(total_houses):
    buildings = []
    m_number = 0.15 * total_houses
    m_counter = 0
    top_value = 0
    best_x = 0
    best_y = 0

    buildings, m_counter = m_build(buildings, m_counter)

    plaatje(buildings)
    time.sleep(0.5)

    maison = classes.Maison(0,0)
    buildings.append(maison)
    plaatje(buildings)
    time.sleep(0.5)
    direction = 'right'

    while True:
        helpers.move(maison, direction, 1)
        # top_value, best_x, best_y = value(buildings, top_value, maison, best_x, best_y)

        #### de functie

        for building in buildings:
            overlapping = helpers.overlap(maison,building)

            if overlapping:
                break

            if not overlapping:
                value = helpers.calculate_score(buildings)

            if value > top_value:
                top_value = value
                best_x = maison.left_bottom[0]
                best_y = maison.left_bottom[1]
                print top_value, best_x, best_y

        # hier gebleven, top_value lijkt niet te kloppen, hij vind er maar twee, en altijd op de y = 0 lijn,
        # dus aan het begin, oplossing vinden, dan: deze functie in functie zetten, dan onpersoonlijkmaken,
        # zodat ook huizen en bugalow die functie kunnen gebruiken,
        # dan functie die huis neerzet op zijn beste plek
        # wellicht ook het stappeen zetten in een functie omzetten,
        # dan als dat voor de maison werkt pas bungalow en huizen!! maar dat is dan appel-eitje

        #### de functie

        if maison.right_top[0] == 360:
            helpers.move(maison, 'up', 1)
            helpers.move(maison, 'left', 1)
            direction = 'left'

        if maison.left_bottom[0] == 0:
            helpers.move(maison, 'up', 1)
            helpers.move(maison, 'right', 1)
            direction = 'right'

        # bij 360, pakt hij hem niet. Later naar kijken, voor nu 359
        if maison.left_top[1] == 320 and maison.right_bottom[0] == 359:
            break

    print("")
    print top_value, best_x, best_y
    plaatje(buildings)


def plaatje(buildings):
    visualisation.print_canvas(buildings, 'try_greedy')
