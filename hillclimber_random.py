# import files
import classes
import main
import helpers
import random
import copy
import time

X_DIMENSION = 360
Y_DIMENSION = 320

def main(iterations, buildings, map_score):

    directions = [-1, 2, 1, -2]

    start_time = time.time()
    print "begin score: ", map_score
    for i in range(iterations):

        building = random.choice(buildings)

        direction = random.randint(-2, 2)

        possible, move_score = check_move2(building, buildings, direction)

        if possible and move_score > map_score:
            print 'move score: ', move_score
            map_score = move_score
            best_buildings = copy.deepcopy(buildings)
        else:
            helpers.move(building, -direction, 0.5)

    print "%s seconds" % (time.time() - start_time)
    return best_buildings, map_score


def check_move2(building, buildings, direction):

    helpers.move(building, direction, 0.5)

    if (building.left_bottom[0] < 0) or (building.left_bottom[1] < 0) or (building.right_top[0] > X_DIMENSION) or (building.right_top[1] > Y_DIMENSION):
        return False, 0

    olap = True
    for build in buildings:

        if build == building:
            continue

        olap = helpers.overlap(build, building)

        if olap:
            return False, 0

    if not olap:
        score = helpers.calculate_score(buildings)
        return True, score
