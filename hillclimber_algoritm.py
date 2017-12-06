# import files
import classes
import main
import helpers
import visualisation
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def main(total_houses, iterations_hill, buildings):

    directions = ['left', 'top', 'right', 'bottom']

    for building in buildings:

        for direction in directions:
            check(building, direction)




def move(building, direction):

    if direction == 'left':
        building.left_bottom[0] -= 1
        building.left_top[0] -= 1
        building.right_top[0] -= 1
        building.right_bottom[0] -= 1

    if direction == 'up':
        building.left_bottom[1] += 1
        building.left_top[1] += 1
        building.right_top[1] += 1
        building.right_bottom[1] += 1

    if direction == 'right':
        building.left_bottom[0] += 1
        building.left_top[0] += 1
        building.right_top[0] += 1
        building.right_bottom[0] += 1

    if direction == 'down':
        building.left_bottom[1] -= 1
        building.left_top[1] -= 1
        building.right_top[1] -= 1
        building.right_bottom[1] -= 1

    return building

def check_overlap(building, direction):

    print "current building: {}".format(building)

    old_building = building
    new_building = move(building, 'direction')
    buildings.remove(building)

    olap = True
    for building2 in buildings:
        olap = helpers.overlap(building2, new_building)

        if olap:
            print "this overlaps"
            buildings.append(old_building)
            break

    if not olap:
        buildings.append(new_building)
        print "moved building: {}".format(building)
        return
