import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import os
from os import path

def draw_canvas():

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.set_xlim(0, 360)
    ax1.set_ylim(0, 320)

    return ax1, fig1

def drawBuilding(ax1, building, x, y, edgecolor):

    # add building to map
	ax1.add_patch(
	    patches.Rectangle(
	        (x, y),   			# (x,y)
	        building.width,    # length
	        building.length,     # width	# color
			linewidth = 1,
			edgecolor = edgecolor,
			facecolor = 'none'
	    )
	)

def print_canvas(buildings, file_name):
    ax1, fig1 = draw_canvas()

    outpath =  "test/"

    for building in buildings:
        if building.name == 'house':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'red')
        if building.name == 'bungalow':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'black')
        if building.name == 'maison':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'green')

    fig1.savefig(path.join(outpath,"test_{}.png".format(file_name)), dpi=90, bbox_inches='tight')

def main(district, algorithm, total_houses, best_iteration, end_time, iterations, variation, name):

    ax1, fig1 = draw_canvas()
    plt.suptitle("The total value is: ${:,}".format(best_iteration))
    plt.title("{} seconds".format(end_time), loc='left')
    plt.title("{} iterations".format(iterations), loc='right')

    if variation == 0:
        outpath = ("output/{}/{}".format(algorithm, total_houses))

    else:
        outpath = ("output/{}/{}/{}".format(algorithm, variation, total_houses))

    if not os.path.exists(outpath):
        os.makedirs(outpath)

    print district.waters
    for water in district.waters:
        drawBuilding(ax1, building, water.left_bottom[0], water.left_bottom[1], 'blue')

    for building in district.buildings:
        if building.name == 'house':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'red')
        if building.name == 'bungalow':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'black')
        if building.name == 'maison':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'green')

    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    fig1.savefig(path.join(outpath,"{}_{}_{}_{}.png".format(algorithm, total_houses, timestamp, name)), dpi=90, bbox_inches='tight')
