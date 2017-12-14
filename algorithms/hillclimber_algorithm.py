# import files
from helpers import calculate_score, move, overlap

# import modules
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy

X_DIMENSION = 360
Y_DIMENSION = 320

def main(iterations_hill, buildings, map_score):

    print "banaan"
    # left, up, right, down
    directions = [-1, 2, 1, -2]
    best_direction = None
    total_score = map_score
    best_buildings = buildings

    print "total score begin: ", total_score
    for i in range(iterations_hill):

        for building in buildings:

            best_direction = None

            for direction in directions:

                possible, move_score = check_move(building, buildings, direction)

                if possible and move_score > map_score:
                    print 'move score: ', move_score
                    best_direction = direction
                    map_score = move_score

                else:
                    continue

                move(building, best_direction, 0.5)

        print i

        if map_score > total_score:
            best_buildings = copy.deepcopy(buildings)


    return best_buildings, total_score

def check_move(building, buildings, direction):

    move(building, direction, 0.5)

    if (building.left_bottom[0] < 0) or (building.left_bottom[1] < 0) or (building.right_top[0] > X_DIMENSION) or (building.right_top[1] > Y_DIMENSION):
        return False, 0

    olap = True
    for build in buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            move(building, -direction, 0.5)
            return False, 0

    if not olap:
        score = calculate_score(buildings)
        move(building, -direction, 0.5)
        return True, score
