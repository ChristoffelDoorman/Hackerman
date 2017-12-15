# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

# import files
from helpers import h_build, b_build, m_build
import visualisation

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
import helpers

X_DIMENSION = 360
Y_DIMENSION = 320

def main(total_houses):

    #best_iteration = 0

    #for i in range(iterations):

    # de lijst voor de buildings
    buildings = []

    # set number of each building type
    h_number = 0.6 * total_houses
    b_number = 0.25 * total_houses
    m_number = 0.15 * total_houses

    # create counters to count number of each building
    h_counter, b_counter, m_counter = 0, 0, 0

    # bouw het eerste huis random (Masoin, want die heeft de meeste waarde)
    buildings, m_counter = m_build(buildings, m_counter)

    # bouw alle Maison's,
    maison = classes.Maison(0,0)
    while (m_counter < m_number):
        buildings = greedy_check(maison, buildings)
        m_counter += 1

    # bouw alle Bungalow's
    while (b_counter < b_number):
        buildings = greedy_check(classes.Bungalow, buildings)
        b_counter += 1

    # bouw alle House's
    while (h_counter < h_number):
        buildings = greedy_check(classes.House, buildings)
        h_counter += 1


    #return top_value


    # functie die checkt of de building niet op een andere building staat, zo niet check de waarde,
    # is die het grootst? (tot nu toe), sla die waarde, plus de coordinaten op.
    # met gebruik van helpers.overlap en helpers.calculate
def value(buildings, top_value, edifice):

    olap = True
    for building in buildings:
        olap = helpers.overlap(edifice,building)

    #if oplap:
        #break

    if not oplap:
        value = helpers.calculate_score(buildings)

    if value > top_value:
        top_value = value
        best_x = x
        best_y = y

    return top_value, best_x, best_y

def greedy_check(edifice, buildings):

    buildings = buildings

    # bouw en plaats het huis helemaal onderin de kaart met de linkerhoek op (0,0)
    buildings.append(edifice)

    # de hoogste waarde van het gebouw
    top_value = 0

    # check hem de eerste keer, voordat je hem gaat bewegen, in de while-loop
    top_value, best_x, best_y = value(buildings, top_value, edifice)

    # zet de direction op 1 ofwel: naar rechts, want het huis begint links
    # begin met bewegen, check hem bij elke stop
    direction = 1
    while True:
        helpers.move(edifice, direction, 1)
        top_value, best_x, best_y = value(buildings, top_value, edifice)

    # Als einde x-as bereikt met rechterkant huis, een stapje omhoog en naar links gaan bewegen, dus direction == -1
        if edifice.right_bottom[0] == X_DIMENSION:
            # zet 1 stap naar boven
            helpers.move(edifice, 2, 1)
            # check de waarde van deze locatie
            top_value, best_x, best_y = value(buildings, top_value, edifice)
            # -1 want moet naar links gaan lopen
            direction = -1

    # Als begin X-as bereikt met linkerkant huis, 1 stapje omhoog en weer naar recht dus direction == 1
        if edifice.left_bottom[0] == 0:
            # zet 1 stap naar boven
            helpers.move(edifice, 2, 1)
            # check de waarde van deze locatie
            top_value, best_x, best_y = value(buildings, top_value, edifice)
            # 1, want hij moet naar rechts gaan lopen
            direction = 1

        # de hoogste waarde op de map is 320, dat is een even getal, hij bereikt de even getallen aan de linkerkant (x = 0 kant)
        # of wel de eerste keer dat hij 320 bereikt is aan de linkerkant niet aan de rechter!
        # dus als hij op 320 is, moet hij nog naar de x = 360 kant om alles gehad te hebben.
        # dus als y = 320 en x = 360, dan heeft hij alles gehad
        if edifice.left_top[0] == 320 and edifice.right_top[0] == 360:
            top_value, best_x, best_y = value(buildings, top_value, edifice)
            break

    # verplaats huis naar best_x, best_y

    return buildings
