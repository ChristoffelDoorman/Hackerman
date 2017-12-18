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

    # initialize a new class for what will be the best district
    best_district = classes.Map(360, 320, water_type)

    total_score = map_score

    # start a timer to calculate the runningtime of the algorithm
    start_time = time.time()

    # loop for as many iterations are put in
    for i in range(iterations):

        # choose a random building
        building = random.choice(district.buildings)

        # 0 = move, 1 = rotate, 2 = swap
        choice = random.randint(0, 2)

        if choice == 0:

            # only improves if no overlap is found and map score was equal or increased
            map_score = hill_move(building, district, map_score)

        # a house rotation has no effect so this is excluded
        elif choice == 1 and not building.name == 'house':

            # rotate building and improve map score if no overlap is found
            building.rotate()
            map_score = check_rotate(building, district, map_score)

        elif choice == 2:

            # choose two random buildings
            building1 = random.choice(district.buildings)
            building2 = random.choice(district.buildings)

            # check if it is the same building
            if building1 != building2:

                # move building and get the map score of that move
                possible, move_score = check_swap(building1, building2, district)

                # if no overlap is found and move_score is equal or better, change score
                if possible == True and (move_score >= map_score):
                    map_score = move_score

                else:
                    # swap values back to normal
                    swap(building1, building2)

        # only change best buildings if value this iteration has increased
        if map_score > total_score:
            total_score = map_score
            best_district.buildings = district.buildings

    end_time = time.time() - start_time

    # if no improvements are found after all iterations return last best district
    if not best_district.buildings:
        return district, map_score, end_time

    return best_district, total_score, end_time

def hill_move(building, district, map_score):

    # move in random direction
    direction = random.randint(-2, 2)

    # gives True if move is possible and corresponding score
    possible, move_score = check_move(building, district, direction, 0.5)

    if possible and move_score >= map_score:
        map_score = move_score

    else:
        # move back in the opposite direction
        move(building, -direction, 0.5)

    return map_score

def check_rotate(building, district, map_score):

    # check if building is in canvas
    if overlap_canvas(building):
        # rotate building 90 degrees clockwise
        building.rotate()
        return map_score

    olap = True
    for water in district.waters:
        # check for overlap with water
        olap = overlap(building, water)

        if olap:
            # rotate buiding back
            building.rotate()
            return map_score

    olap = True

    for build in district.buildings:
        # if building in the list is the same as we want to check, skip this
        if build == building:
            continue

        # check overlap with other buildings
        olap = overlap(build, building)

        if olap:
            # rotate back
            building.rotate()
            return map_score

    if not olap:
        # calculate score and evaluate if score is higher
        move_score = district.score()
        if move_score >= map_score:
            map_score = move_score

        else:
            # rotate back
            building.rotate()

        return map_score

def check_swap(building1, building2, district):

    # swap buildings
    swap(building1, building2)

    # check if the buildings overlap with eachother after swap
    olap = overlap(building1, building2)
    if olap:
        return False, 0

    # check if the buildings are inside the map
    if overlap_canvas(building1) or overlap_canvas(building2):
        return False, 0

    olap1 = True
    olap2 = True

    # check overlap with water
    for water in district.waters:
        olap1 = overlap(building1, water)
        olap2 = overlap(building2, water)

        if olap1 or olap2:
            return False, 0

    if not olap1 and not olap2:

        olap1 = True
        olap2 = True

        # check for overlap with buildings
        for building in district.buildings:

            # if building in the list is the same as we want to check, skip this
            if building == building1 or building == building2:
                continue

            olap1 = overlap(building, building1)
            olap2 = overlap(building, building2)

            if olap1 or olap2:
                return False, 0

        # only when neither overlap, calculate the new score and return True
        if not olap1 and not olap2:

            move_score = district.score()
            return True, move_score

def swap(building1, building2):

    # simultanious change the x values of building 1 and two, idem for the y values
    building1.left_bottom[0], building2.left_bottom[0] = building2.left_bottom[0], building1.left_bottom[0]
    building1.left_bottom[1], building2.left_bottom[1] = building2.left_bottom[1], building1.left_bottom[1]

    # update the corners of the buildings with new x and y values
    building1.update(building1.left_bottom[0], building1.left_bottom[1])
    building2.update(building2.left_bottom[0], building2.left_bottom[1])
