import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import os
from os import path

def draw_canvas():

    # initialize the figure for plot
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.set_xlim(0, 360)
    ax1.set_ylim(0, 320)

    return ax1, fig1

def drawBuilding(ax1, building, x, y, edgecolor):

    # draw building as transparent rectangle in plot with unique color for each building type
	ax1.add_patch(
	    patches.Rectangle(
	        (x, y),
	        building.width,
	        building.length,
			linewidth = 1,
			edgecolor = edgecolor,
			facecolor = 'none'
	    )
	)

def main(district, algorithm, total_houses, best_iteration, end_time, iterations, variation, name):

    # initialize canvas
    ax1, fig1 = draw_canvas()

    # upper title of plot is the value of the map
    plt.suptitle("The total value is: ${:,}".format(best_iteration))

    # sub titles are the runningtime of the algorithm and the amount of iterations
    plt.title("{} seconds".format(end_time), loc='left')
    plt.title("{} iterations".format(iterations), loc='right')

    # if no varation is applicable to this plot do not add it to the outpath
    if variation == 0:
        outpath = ("output/{}/{}".format(algorithm, total_houses))

    # add varation of algorithm to outpath
    else:
        outpath = ("output/{}/{}/{}".format(algorithm, variation, total_houses))

    # if no folder is made for the plot, make it
    if not os.path.exists(outpath):
        os.makedirs(outpath)

    # draw all waters
    for water in district.waters:
        drawBuilding(ax1, water, water.left_bottom[0], water.left_bottom[1], 'blue')

    # draw all buildings
    for building in district.buildings:
        if building.name == 'house':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'red')
        if building.name == 'bungalow':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'black')
        if building.name == 'maison':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'green')

    # add timestamp to file name to order them in the folder
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    # save the figure
    fig1.savefig(path.join(outpath,"{}_{}_{}_{}.png".format(algorithm, total_houses, timestamp, name)), dpi=90, bbox_inches='tight')
