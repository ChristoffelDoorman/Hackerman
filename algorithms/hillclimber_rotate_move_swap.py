# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file rotates, moves and swaps two houses randomly to check if score
# has improved.

# import files
from helpers import move, overlap, check_move, overlap_canvas
import classes
import visualisation.canvas_visualisation as visualisation

# import files
import random
import copy
import time

def main(iterations, district, map_score, water_type):

    best_district = classes.Map(360, 320, water_type)
    total_score = map_score
    start_time = time.time()

    for i in range(iterations):
        # print i

        building = random.choice(district.buildings)

        # 0 = move 1 = rotate 2 = swap random.randint(2)
        choice = random.randint(0, 2)
        #
        if choice == 0:
            map_score = hill_move(building, district, map_score)

        elif choice == 1 and not building.name == 'house':

            building.rotate()
            building, map_score = check_rotate(building, district, map_score)

        elif choice == 2:
            # print "keuze is 2"
            building1 = random.choice(district.buildings)
            building2 = random.choice(district.buildings)
            # print building1, building2
            if building1 != building2:

                # print "dit is de ongemovede score", district.score()
                # print "ze zijn niet hetzelfde"
                possible, move_score = check_swap(building1, building2, district)

                if possible == True and (move_score >= map_score):
                    map_score = move_score
                    # visualisation.print_canvas(district, 'swaptest')

                    # print "swap complete"
                else:
                    # visualisation.print_canvas(district, 'swaptest')
                    swap(building1, building2)
                    # building1.width, building2.width = building2.width, building1.width
                    # building1.length, building2.length = building2.length, building1.length
                    # print "geen hogere score"

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

    if possible and move_score >= map_score:
        map_score = move_score

    else:
        move(building, -direction, 0.5)

    return map_score

def check_rotate(building, district, map_score):

    if overlap_canvas(building):
        building.rotate()
        return building, map_score

    olap = True
    for water in district.waters:
        olap = overlap(building, water)

        if olap:
            building.rotate()
            return building, map_score

    olap = True
    for build in district.buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            building.rotate()
            return building, map_score

    if not olap:
        move_score = district.score()
        if move_score >= map_score:
            map_score = move_score

        else:
            building.rotate()

        return building, map_score

def check_swap(building1, building2, district):
    # print "1", district.buildings
    # district.buildings.remove(building1)
    # district.buildings.remove(building2)
    # print "2", district.buildings
    # oldxy1 = copy.deepcopy(building1)
    # oldxy2 = copy.deepcopy(building2)
    # building1.update(oldxy2.left_bottom[0], oldxy2.left_bottom[1])
    # building2.update(oldxy1.left_bottom[0], oldxy1.left_bottom[1])
    # print "1", district.buildings
    # print building1, building2
    # print building1, building2, district
    # print building1, building2, district
    # building1.width, building2.width = building2.width, building1.width
    # building1.length, building2.length = building2.length, building1.length
    # print building1, building2
    swap(building1, building2)

    olap = overlap(building1, building2)
    if olap:
        # print "overlap met elkaar"
        return False, 0
    # print "ZE OVERLAPPEN MET ELKAAR", olap

    if overlap_canvas(building1) or overlap_canvas(building2):
        # print "buiten canvas"
        return False, 0

    # print "2", district.buildings
    # print "dit is de gemovede score", district.score()

    # olap = overlap(building1, building2)
    # if olap:
    #     print "ze overlappen met elkaar", olap
    #     return False, 0
    olap1 = True
    olap2 = True

    for water in district.waters:
        # print water
        olap1 = overlap(building1, water)
        olap2 = overlap(building2, water)

        if olap1 or olap2:
            # print "overlap met water"
            return False, 0

    if not olap1 and not olap2:

        olap1 = True
        olap2 = True

        for building in district.buildings:

            if building == building1 or building == building2:
                continue

            olap1 = overlap(building, building1)
            olap2 = overlap(building, building2)
            # print overlap2

            if olap1 or olap2:
                # print "overlap met gebouw"
                return False, 0

        if not olap1 and not olap2:
            # print "GEEN OVERLAP"
            move_score = district.score()
            # print "dit is de gemovede score", move_score
            # print "swapping"
            return True, move_score

def swap(building1, building2):
    building1.left_bottom[0], building2.left_bottom[0] = building2.left_bottom[0], building1.left_bottom[0]
    building1.left_bottom[1], building2.left_bottom[1] = building2.left_bottom[1], building1.left_bottom[1]
    building1.update(building1.left_bottom[0], building1.left_bottom[1])
    building2.update(building2.left_bottom[0], building2.left_bottom[1])
