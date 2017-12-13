# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

# import files
from classes import Map
from helpers import h_build, b_build, m_build, calculate_score
import visualisation

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import locale
import timeit
import math

district = Map(320, 360)


def main(total_houses, iterations):

    #best_iteration = 0

    #for i in range(iterations):

        # fill building array with a house at a random point
        buildings = []
        top_value = 0
        direction = 1

        # set number of each building type
        h_number = 12   # 0.6 * total_houses
        b_number = 5    # 0.25 * total_houses
        m_number = 3    # 0.15 * total_houses

        # create counters to count number of each building
        # h_counter, b_counter, m_counter = 0, 0, 0


        # bouw het eerste huis random.
        buildings, m_counter = m_build(buildings, m_counter)

        # plaats het huis helemaal onderin de kaart met de linkerhoek op (0,0)
        # ook hier nog een loop nodig voor alle maison's
        maison = classes.Maison(0,0)
        buildings.append(maison)

        # check hem de eerste keer, voordat je hem gaat bewegen, in de while-loop
        value(buildings, top_value, maison)

        while True:
            helpers.move(maison, direction, 1)
            value(buildings, top_value, maison)

        # Als einde x-as bereikt met rechterkant huis, een stapje omhoog en naar links gaan bewegen, dus direction == -1
            if maison.right_bottom[0] == X_DIMENSION
                # zet 1 stap naar boven
                helpers.move(maison, 2, 1)
                # check de waarde van deze locatie
                value(buildings, top_value, maison)
                # -1 want moet naar links gaan lopen
                direction = -1

        # Als begin X-as bereikt met linkerkant huis, 1 stapje omhoog en weer naar recht dus direction == 1
            if maison.left_bottom[0] = 0
                # zet 1 stap naar boven
                helpers.move(maison, 2, 1)
                # check de waarde van deze locatie
                value(buildings, top_value, maison)
                # 1, want hij moet naar rechts gaan lopen
                direction = 1

            # if-statement, om te bepalen wanneer de while-true loop gebroken moet worden,







def value(buildings, top_value, maison):

    for building in buildings:
        olap = helpers.overlap(maison,building)

        if oplap:
            break

    if not oplap:
        value = helpers.calculate_score(buildings)

        if value > top_value:
            top_value = value
            best_x = x
            best_y = y

    return top_value, best_x, best_y
