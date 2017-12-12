# import files
from classes import Map
from helpers import calculate_score, move, overlap

# import modules
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy

# create map class as district
district = Map(320, 360)

def main(total_houses, iterations_hill, buildings):


    directions = ['left', 'up', 'right', 'down']

    for i in range(iterations_hill):

        for building in buildings:

            map_score = calculate_score(buildings)

            # print map_score

            for direction in directions:

                possible = check_overlap(building, buildings, direction)

                best_direction = None

                if direction == 'left' and possible:
                    score_left = moved_score(building, buildings, direction)
                    if score_left > map_score:
                        map_score = score_left
                        best_direction = direction

                if direction == 'up' and possible:
                    score_up = moved_score(building, buildings, direction)
                    if score_up > map_score:
                        map_score = score_up
                        best_direction = direction

                if direction == 'right' and possible:
                    score_right = moved_score(building, buildings, direction)
                    if score_right > map_score:
                        map_score = score_right
                        best_direction = direction

                if direction == 'down' and possible:
                    score_down = moved_score(building, buildings, direction)
                    if score_down > map_score:
                        map_score = score_down
                        best_direction = direction

                move(building, best_direction, 1)


    return buildings, map_score


def check_overlap(building, buildings, direction):

    old_building = copy.deepcopy(building)
    new_building = move(old_building, direction, 1)

    if (new_building.left_bottom[0] < 0) or (new_building.left_bottom[1] < 0) or (new_building.right_top[0] > district.width) or (new_building.right_top[1] > district.height):
        return False

    olap = True
    for build in buildings:

        if build == building:
            continue

        olap = overlap(build, new_building)

        if olap:
            return False

    if not olap:
        return True


def moved_score(building, buildings, direction):

    old_building = copy.deepcopy(building)
    move(building, direction, 3)
    score = calculate_score(buildings)

    if direction == 'left':
        move(building, 'right', 3)

    if direction == 'up':
        move(building, 'down', 3)

    if direction == 'right':
        move(building, 'left', 3)

    if direction == 'down':
        move(building, 'up', 3)

    return score
