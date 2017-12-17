# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file moves buildings randomly to check if score has improved.

# import files
from helpers import move, overlap, check_move
import classes

# import files
import random
import time

def main(iterations_hill, district, map_score, water_type):

    best_district = classes.Map(360, 320, water_type)

    start_time = time.time()

    for i in range(iterations_hill):

        building = random.choice(district.buildings)

        direction = random.randint(-2, 2)

        possible, move_score = check_move(building, district, direction, 0.5)

        if possible and move_score >= map_score:
            map_score = move_score
            best_district = district

        else:
            move(building, -direction, 0.5)

    end_time = time.time() - start_time
    if not best_district.buildings:
        return district, map_score, end_time

    print best_district
    return best_district, map_score, end_time
