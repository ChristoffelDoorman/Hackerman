
from algorithms import *
import visualisation.canvas_visualisation as visualisation
from helpers import calculate_score
from classes import Map


if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")

    while total_houses < 7:
        total_houses = input("Choose number bigger than 7: ")

    algorithm_choice = input("Which algorithm? [1: random], [2: hillclimber], [3: expanding universe], [4: hillclimber random] ")

    if algorithm_choice == 1:
        algorithm = "random"
        iterations = input("How many iterations?: ")

        buildings, best_iteration = random_algorithm.main(total_houses, iterations)
    	# stop = timeit.default_timer()
    	# print "De tijd is: ", stop - start
        # print ("best iteration is", best_iteration)

        # visualisation.main(buildings, algorithm, 0, 0, False)
        visualisation.main(buildings, algorithm, total_houses, best_iteration, True)

        print "Volgens nieuwe Map.score= ", Map.score

    elif algorithm_choice == 2:
        algorithm = "hillclimber"

        iterations = input("How many iterations random first?: ")

        best_buildings_random, best_iteration = random_algorithm.main(total_houses, iterations)

        visualisation.print_canvas (best_buildings_random, 'random')

        print best_iteration

        iterations_hill = input("How many iterations for hillclimber: ")


        best_buildings_hill, map_score = hillclimber_algorithm.main(iterations_hill, best_buildings_random, best_iteration)

        print map_score

        visualisation.print_canvas(best_buildings_hill, 'hill')

    elif algorithm_choice == 3:
        algorithm = "expanding_universe"

        buildings = expanding_universe.main(total_houses)

        map_score = calculate_score(buildings)

        # iterations_hill = input("How many iterations for hillclimber: ")
        #
        # buildings, map_score = hillclimber_algorithm.main(iterations_hill, buildings, 0)

        visualisation.print_canvas(buildings, 'expanding 60')
        # visualisation.main(buildings, algorithm, total_houses, map_score, False)
        visualisation.main(buildings, algorithm, total_houses, map_score, False)

    elif algorithm_choice == 4:
        algorithm = "hillclimber_random"

        iterations = input("How many iterations random first?: ")

        best_buildings_random, best_iteration = random_algorithm.main(total_houses, iterations)

        visualisation.print_canvas (best_buildings_random, 'random_2')

        print best_iteration

        iterations_hill = input("How many iterations for hillclimber: ")

        best_buildings_hill, map_score = hillclimber_random.main(iterations_hill, best_buildings_random, best_iteration)

        print map_score
