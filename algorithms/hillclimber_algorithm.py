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
    best_district = classes.Map(360, 320, water_type)
    start_time = time.time()

    # print "total score begin: ", total_score
    for i in range(iterations_hill):

        for building in district.buildings:

            best_direction = None

            for direction in directions:

                possible, move_score = check_move(building, district, direction, 0.5)
                move(building, -direction, 0.5)

                if possible and move_score >= map_score:
                    # print 'move score: ', move_score
                    best_direction = direction
                    map_score = move_score

            if best_direction != None:
                move(building, best_direction, 0.5)

        if map_score > total_score:
            total_score = map_score
            best_district.buildings = district.buildings

    end_time = time.time() - start_time
    return best_district, total_score, end_time
