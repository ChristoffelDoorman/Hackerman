# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file rotates, moves and swaps two houses randomly to check if score
# has improved.

# import files
from helpers import move, overlap, check_move
import classes

# import files
import random
import copy
import time

def main(iterations, district, map_score, water_type):

    best_district = classes.Map(360, 320, water_type)
    total_score = map_score
    start_time = time.time()

    for i in range(iterations):

        building = random.choice(district.buildings)

        # 0 = move 1 = rotate 2 = swap random.randint(2)
        choice = random.randint(0, 2)

        if choice == 0 and building.name == 'house':
            map_score = hill_move(building, district, map_score)

        elif choice == 1 and not building.name == 'house':
            map_score = check_rotate(building, district, map_score)

        elif choice == 2:
            print "keuze is 2"
            building1 = random.choice(district.buildings)
            building2 = random.choice(district.buildings)
            if building1 != building2:

                print "dit is de ongemovede score", district.score()
                print "ze zijn niet hetzelfde"
                possible, move_score = check_swap(building1, building2, district)

                if possible:
                    print "MOGELIJK"
                else:
                    print "xx"

                if possible and move_score > map_score:
                    map_score = move_score

                    # print "building 1 na", building1
                    # print "building 2 na", building2
                    print "swap complete"
                else:
                    building1.left_bottom[0], building2.left_bottom[0] = building2.left_bottom[0], building1.left_bottom[0]
                    building1.left_bottom[1], building2.left_bottom[1] = building2.left_bottom[1], building1.left_bottom[1]
                    print "geen hogere score"

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

def check_rotate(building, district, map_score):

    building.rotate()

    for water in district.waters:
		olap = overlap(building, water)

		if olap:
			building.rotate()
			return map_score

    for build in district.buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            building.rotate()
            return map_score

    if not olap:

        move_score = district.score()
        if move_score > map_score:
            map_score = move_score

        else:
            building.rotate()

        return map_score

def check_swap(building1, building2, district):
    # print "1", district.buildings
    # district.buildings.remove(building1)
    # district.buildings.remove(building2)
    # print "2", district.buildings
    # oldxy1 = copy.deepcopy(building1)
    # oldxy2 = copy.deepcopy(building2)
    #
    # building1.update(oldxy2.left_bottom[0], oldxy2.left_bottom[1])
    # building2.update(oldxy1.left_bottom[0], oldxy1.left_bottom[1])
    print "1", district.buildings
    building1.left_bottom[0], building2.left_bottom[0] = building2.left_bottom[0], building1.left_bottom[0]
    building1.left_bottom[1], building2.left_bottom[1] = building2.left_bottom[1], building1.left_bottom[1]
    print "2", district.buildings

    if (building1.left_bottom[0] < 0) or (building1.left_bottom[1] < 0)	or (building1.right_top[0] > district.width) or (building1.right_top[1] > district.height):
        print "buiten canvas"
        return False, 0


    if (building2.left_bottom[0] < 0) or (building2.left_bottom[1] < 0)	or (building2.right_top[0] > district.width) or (building2.right_top[1] > district.height):
        print "buiten canvas"
        return False, 0

    for water in district.waters:
        olap1 = overlap(building1, water)
        olap2 = overlap(building2, water)

        if olap1 or olap2:
            print "overlap met water"
            return False, 0

    overlap3 = overlap(building1, building2)
    print "ze overlappen met elkaar"

    for building in district.buildings:

        if building == building1 or building == building2:
            continue

        overlap1 = overlap(building, building1)
        print overlap1
        overlap2 = overlap(building, building2)
        print overlap2

        if overlap1 or overlap2 or overlap3:
            print "overlap met gebouw"
            return False, 0

    if not overlap1 or overlap2:
        print "GEEN OVERLAP"
        move_score = district.score()
        print "dit is de gemovede score", move_score
        # print "swapping"
        return True, move_score
# def swap(building1, building2):
#
#     building1.update(building2.left_bottom[0], building2.left_bottom[1])
#     building2.update(building1.left_bottom[0], building1.left_bottom[1])
