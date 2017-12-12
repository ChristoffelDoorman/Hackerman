# import files
import classes
import main
import helpers
import visualisation
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy

X_DIMENSION = 360
Y_DIMENSION = 320

def main(total_houses, iterations_hill, buildings):

    directions = ['left', 'up', 'right', 'down']

    for i in range(iterations_hill):

        for building in buildings:

            map_score = helpers.calculate_score(buildings)

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

                helpers.move(building, best_direction, 3)

    return buildings, map_score


def check_overlap(building, buildings, direction):

    old_building = copy.deepcopy(building)
    new_building = helpers.move(old_building, direction, 1)

    if (new_building.left_bottom[0] < 0) or (new_building.left_bottom[1] < 0) or (new_building.right_top[0] > X_DIMENSION) or (new_building.right_top[1] > Y_DIMENSION):
        return False

    olap = True
    for build in buildings:

        if build == building:
            continue

        olap = helpers.overlap(build, new_building)

        if olap:
            # print "this overlaps"
            return False
            # print 'false: ', buildings

    if not olap:
        # print "no overlap"
        # print "moved building: {}".format(building)
        return True
        # print 'true: ', buildings


def moved_score(building, buildings, direction):

    old_building = copy.deepcopy(building)
    helpers.move(building, direction, 3)
    score = helpers.calculate_score(buildings)

    if direction == 'left':
        helpers.move(building, 'right', 3)

    if direction == 'up':
        helpers.move(building, 'down', 3)

    if direction == 'right':
        helpers.move(building, 'left', 3)

    if direction == 'down':
        helpers.move(building, 'up', 3)

    return score
