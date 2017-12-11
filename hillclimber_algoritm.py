# import files
import classes
import main
import helpers
import visualisation
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy


def main(total_houses, iterations_hill, buildings):

    directions = ['left', 'up', 'right', 'down']

    for building in buildings:

        map_score = helpers.calculate_score(buildings)

        print "map score = ", map_score

        for direction in directions:

            possible = check_overlap(building, buildings, direction)

            # print "possible = ", possible

            if direction == 'left' and possible:
                score_left = moved_score(building, buildings, direction)
                # print "score left: {}".format(score_left)

            if direction == 'up' and possible:
                score_up = moved_score(building, buildings, direction)
                # print "score up: {}".format(score_up)

            if direction == 'right' and possible:
                score_right = moved_score(building, buildings, direction)
                # print "score right: {}".format(score_right)


            if direction == 'down' and possible:
                score_down = moved_score(building, buildings, direction)
                # print "score down: {}".format(score_down)

            print map_score


def check_overlap(building, buildings, direction):

    old_building = copy.deepcopy(building)
    new_building = helpers.move(old_building, direction)

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

    if direction == 'left':
        helpers.move(building, direction)
        score_left = helpers.calculate_score(buildings)
        # visualisation.print_canvas(buildings, '1')
        helpers.move(building, 'right')
        return score_left

    if direction == 'up':
        building = helpers.move(building, direction)
        score_up = helpers.calculate_score(buildings)
        # visualisation.print_canvas(buildings, '2')
        helpers.move(building, 'down')
        return score_up

    if direction == 'right':
        building = helpers.move(building, direction)
        score_right = helpers.calculate_score(buildings)
        # visualisation.print_canvas(buildings, '3')
        helpers.move(building, 'left')
        return score_right

    if direction == 'down':
        building = helpers.move(building, direction)
        score_down = helpers.calculate_score(buildings)
        # visualisation.print_canvas(buildings, '4')
        helpers.move(building, 'up')
        return score_down
