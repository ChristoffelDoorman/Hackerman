# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file moves buildings left, right, top and bottom to check if score
# has improved.

# import files
from helpers.helper_functions import move, overlap, check_move
import classes

# import modules
import time

def main(iterations_hill, district, map_score, water_type):

    # left, up, right, down
    directions = [-1, 2, 1, -2]

    total_score = map_score

    # initialize a new class for what will be the best district
    best_district = classes.Map(360, 320, water_type)

    # start a timer to calculate the runningtime of the algorithm
    start_time = time.time()

    # loop for as many iterations are put in
    for i in range(iterations_hill):

        for building in district.buildings:

            # reset best direction zo none for every building
            best_direction = None

            for direction in directions:

                # move building and improve map score if no overlap is found
                possible, move_score = check_move(building, district, direction, 0.5)

                # move back for the next direction
                move(building, -direction, 0.5)

                # if move is possible and the move gives a better or same result
                # this way more possible solutions can be found
                if possible and move_score >= map_score:
                    best_direction = direction
                    map_score = move_score

            # when an improvement is found move building in that direction
            if best_direction != None:
                move(building, best_direction, 0.5)

        # only change best buildings if value this iteration has increased
        if map_score > total_score:
            total_score = map_score
            best_district.buildings = district.buildings

    # calculate end time of algorithm
    end_time = time.time() - start_time

    # if no improvements are found after all iterations return last best district
    if not best_district.buildings:
        return district, map_score, end_time

    return best_district, total_score, end_time
