import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
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

def main(buildings, output_file, total_houses, best_iteration, save_in_file):

    ax1, fig1 = draw_canvas()
    plt.suptitle("The total value is: {:,}".format(best_iteration))

    outpath = ("output/{}/{}".format(output_file, total_houses))

    for building in buildings:
        if building.name == 'house':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'red')
        if building.name == 'bungalow':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'black')
        if building.name == 'maison':
            drawBuilding(ax1, building, building.left_bottom[0], building.left_bottom[1], 'green')

    # safe figure
    if save_in_file:
        fig1.savefig(path.join(outpath,"{}_{}.png".format(output_file, total_houses)), dpi=90, bbox_inches='tight')

    else:
        fig1.savefig(output_file, dpi=90, bbox_inches='tight')
