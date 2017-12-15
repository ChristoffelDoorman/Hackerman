# import files
from helpers import move, overlap, check_move
import classes

# import files
import random
import copy
import time

def main(iterations, district, map_score):

    best_district = classes.Map(360, 320)
    total_score = map_score
    start_time = time.time()

    for i in range(iterations):

        for building in district.buildings:

            # 0 = move 1 = rotate 2 = swap
            choice = random.randint(0, 2)

            if building.name == 'house' and choice == 0:
                map_score = hill_move(building, district, map_score)

            elif choice == 1:
                map_score = rotate(building, district, map_score)

            elif choice == 2:
                building1 = random.choice(district.buildings)
                building2 = random.choice(district.buildings)
                if not building1 == building2:

                    old_building1 = copy.deepcopy(building1)
                    old_building2 = copy.deepcopy(building2)

                    possible, move_score = check_swap(building1, building2, old_building1, old_building2, district)

                    if possible and move_score > map_score:
                        map_score = move_score
                        # print "swap complete"
                    else:
                        # print 'restore'
                        building1.update(old_building1.left_bottom[0], old_building1.left_bottom[1])
                        building2.update(old_building2.left_bottom[0], old_building2.left_bottom[1])

        if map_score > total_score:
            total_score = map_score
            best_district.buildings = district.buildings

    end_time = time.time() - start_time
    return best_district, total_score, end_time

def hill_move(building, district, map_score):

    # start_time = time.time()
    # print "begin score: ", map_score

    direction = random.randint(-2, 2)

    possible, move_score = check_move(building, district, direction, 0.5)

    if possible and move_score > map_score:
        map_score = move_score

    else:
        move(building, -direction, 0.5)

    return map_score

def rotate(building, district, map_score):

    building.length, building.width = building.width, building.length
    building.update(building.left_bottom[0], building.left_bottom[1])

    olap = True
    for build in district.buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            building.length, building.width = building.width, building.length
            building.update(building.left_bottom[0], building.left_bottom[1])

    if not olap:

        move_score = district.score()
        if move_score > map_score:
            map_score = move_score

        else:
            building.length, building.width = building.width, building.length
            building.update(building.left_bottom[0], building.left_bottom[1])

        return map_score

def check_swap(building1, building2, old_building1, old_building2, district):

    building1.update(old_building2.left_bottom[0], old_building2.left_bottom[1])
    building2.update(old_building1.left_bottom[0], old_building1.left_bottom[1])


    for building in district.buildings:

        overlap1 = overlap(building, building1)
        overlap2 = overlap(building, building2)
        overlap3 = overlap(building1, building2)
        overlap4 = overlap(building2, building1)
        overlap5 = overlap(building, old_building1)
        overlap6 = overlap(building, old_building2)

        if (building1.left_bottom[0] < 0) or (building1.left_bottom[1] < 0)	or (building1.right_top[0] > district.width) or (building1.right_top[1] > district.height):
            return False, 0

        if (building2.left_bottom[0] < 0) or (building2.left_bottom[1] < 0)	or (building2.right_top[0] > district.width) or (building2.right_top[1] > district.height):
        	return False, 0

        if overlap1 or overlap2 or overlap3 or overlap4 or overlap5 or overlap6:
            return False, 0

        else:
            move_score = district.score()
            # print "swapping"
            return True, move_score
# def swap(building1, building2):
#
#     building1.update(building2.left_bottom[0], building2.left_bottom[1])
#     building2.update(building1.left_bottom[0], building1.left_bottom[1])
