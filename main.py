from algorithms import *
import visualisation.canvas_visualisation as visualisation
from helpers import calculate_score


if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")

    while total_houses < 7:
        total_houses = input("Choose number bigger than 7: ")

    algorithm_choice = input("Which algorithm? [1: random], [2: hillclimber], [3: expanding universe]: ")

    if algorithm_choice == 1:
        algorithm = "random"
        iterations = input("How many iterations?: ")

        buildings, best_iteration = random_algorithm.main(total_houses, iterations)
    	stop = timeit.default_timer()
    	print "De tijd is: ", stop - start
        print ("best iteration is", best_iteration)

        # visualisation.main(buildings, algorithm, 0, 0, False)
        visualisation.main(buildings, algorithm, total_houses, best_iteration, True)


    elif algorithm_choice == 2:
        algorithm = "hillclimber"

        iterations = input("How many iterations random first?: ")

        buildings1, best_iteration = random_algorithm.main(total_houses, iterations)

        visualisation.print_canvas(buildings1, 'random')

        print best_iteration

        iterations_hill = input("How many iterations for hillclimber: ")

        buildings2, map_score = hillclimber_algorithm.main(total_houses, iterations_hill, buildings1)

        print map_score

        visualisation.print_canvas(buildings2, 'hill')


    elif algorithm_choice == 3:
        algorithm = "expanding_universe"

        buildings = expanding_universe.main(total_houses)

        map_score = calculate_score(buildings)

        # iterations_hill = input("How many iterations for hillclimber: ")
        #
        # buildings, map_score = hillclimber_algorithm.main(total_houses, iterations_hill, buildings)

        visualisation.main(buildings, algorithm, total_houses, map_score, False)
