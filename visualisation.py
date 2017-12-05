import matplotlib.pyplot as plt
import matplotlib.patches as patches


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
