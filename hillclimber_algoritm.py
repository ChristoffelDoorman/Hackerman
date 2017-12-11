# import files
import classes
import main
import helpers
import visualisation
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy


def main(total_houses, iterations_hill, buildings):

    directions = ['left', 'top', 'right', 'bottom']

    for building in buildings:

        map_score = helpers.calculate_score(buildings)
        print "map score = ", map_score

        for direction in directions:

            old_building = copy.deepcopy(building)
            # tijdelijke oplossing
            buildings.remove(building)
            new_building = helpers.move(building, direction)

            possible = check_overlap(new_building, old_building, buildings, direction)

            print "possible = ", possible
            if direction == 'left' and possible:
                score_left = helpers.calculate_score(buildings)
                buildings.append(old_building)

            if direction == 'top' and possible:
                score_top = helpers.calculate_score(buildings)
                print "score top: {}".format(score_top)
                buildings.append(old_building)

            if direction == 'right' and possible:
                score_right = helpers.calculate_score(buildings)
                print "score right: {}".format(score_right)
                buildings.append(old_building)

            if direction == 'down' and possible:
                score_down = helpers.calculate_score(buildings)
                print "score down: {}".format(score_down)
                buildings.append(old_building)
        #
        # if score_left or score_top or score_right or score_down > map_score:
        #     map_score = ......


def check_overlap(new_building, old_building, buildings, direction):


    olap = True
    for building in buildings:
        olap = helpers.overlap(building, new_building)

        if olap:
            print "this overlaps"
            return False
            # print 'false: ', buildings

    if not olap:
        print "no overlap"
        # print "moved building: {}".format(building)
        return True
        # print 'true: ', buildings
