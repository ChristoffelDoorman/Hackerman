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

    for i in range(iterations):

        building = random.choice(buildings)

        if not building.name == 'house':


def hill_move(buildings, map_score):

    # start_time = time.time()
    # print "begin score: ", map_score

    building = random.choice(buildings)

    direction = random.randint(-2, 2)

    possible, move_score = check_move(building, buildings, direction)

    if possible and move_score > map_score:
        print 'move score: ', move_score
        map_score = move_score
        # best_buildings = copy.deepcopy(buildings)
    else:
        helpers.move(building, -direction, 0.5)
    #
    # print "%s seconds" % (time.time() - start_time)
    return buildings, map_score

def rotate(building, buildings, map_score):

	building.length, building.width = building.width, building.length
	building.left_top[1] = yrandom + building.length
	building.right_top = [xrandom + building.width, yrandom + building.length]
	building.right_bottom[0] = xrandom + building.width

    olap = True
    for build in buildings:

        if build == building:
            continue

        olap = helpers.overlap(build, building)

        if olap:
            return None

    if not olap:

        return building, map_score


def check_move(building, buildings, direction):

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
