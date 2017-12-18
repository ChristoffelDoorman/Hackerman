# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file moves buildings randomly to check if score has improved.

# import files
from helpers.helper_functions import move, overlap, check_move
import classes

# import files
import random
import time

def main(iterations_hill, district, map_score, water_type):

    # initialize a new class for what will be the best district
    best_district = classes.Map(360, 320, water_type)

    # start a timer to calculate the runningtime of the algorithm
    start_time = time.time()

    for i in range(iterations_hill):

        # choose random building and random direction
        building = random.choice(district.buildings)
        direction = random.randint(-2, 2)

        # move building and improve map score if no overlap is found
        possible, move_score = check_move(building, district, direction, 0.5)

        # only change best buildings if value has increased
        if possible and move_score >= map_score:
            map_score = move_score
            best_district = district

        # otherwise move back in opposite direction
        else:
            move(building, -direction, 0.5)

    # calculate end time of algorithm
    end_time = time.time() - start_time

    # if no improvements are found after all iterations return last best district
    if not best_district.buildings:
        return district, map_score, end_time

    return best_district, map_score, end_time
