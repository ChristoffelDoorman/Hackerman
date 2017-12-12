<<<<<<< HEAD
import random_algoritm
import expanding_universe
import visualisation
import hillclimber_algoritm
import hillclimber_random

import helpers
=======
from algorithms import *
import visualisation.canvas_visualisation as visualisation
from helpers import calculate_score
>>>>>>> 1eaed68488a0aed0bdbbeb312df3ac3945b3ca15


if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")

    while total_houses < 7:
        total_houses = input("Choose number bigger than 7: ")

<<<<<<< HEAD
    algoritm_choice = input("Which algoritm? [1: random], [2: hillclimber], [3: expanding universe], [4: hillclimber random] ")
=======
    algorithm_choice = input("Which algorithm? [1: random], [2: hillclimber], [3: expanding universe]: ")
>>>>>>> 1eaed68488a0aed0bdbbeb312df3ac3945b3ca15

    if algorithm_choice == 1:
        algorithm = "random"
        iterations = input("How many iterations?: ")

<<<<<<< HEAD
        buildings, best_iteration = random_algoritm.main(total_houses, iterations)
    	# stop = timeit.default_timer()
    	# print "De tijd is: ", stop - start
        # print ("best iteration is", best_iteration)
=======
        buildings, best_iteration = random_algorithm.main(total_houses, iterations)
    	stop = timeit.default_timer()
    	print "De tijd is: ", stop - start
        print ("best iteration is", best_iteration)
>>>>>>> 1eaed68488a0aed0bdbbeb312df3ac3945b3ca15

        # visualisation.main(buildings, algorithm, 0, 0, False)
        visualisation.main(buildings, algorithm, total_houses, best_iteration, True)


    elif algorithm_choice == 2:
        algorithm = "hillclimber"

        iterations = input("How many iterations random first?: ")

<<<<<<< HEAD
        best_buildings_random, best_iteration = random_algoritm.main(total_houses, iterations)
=======
        buildings1, best_iteration = random_algorithm.main(total_houses, iterations)
>>>>>>> 1eaed68488a0aed0bdbbeb312df3ac3945b3ca15

        visualisation.print_canvas (best_buildings_random, 'random')

        print best_iteration

        iterations_hill = input("How many iterations for hillclimber: ")

<<<<<<< HEAD
        best_buildings_hill, map_score = hillclimber_algoritm.main(iterations_hill, best_buildings_random, best_iteration)
=======
        buildings2, map_score = hillclimber_algorithm.main(total_houses, iterations_hill, buildings1)
>>>>>>> 1eaed68488a0aed0bdbbeb312df3ac3945b3ca15

        print map_score

        visualisation.print_canvas(best_buildings_hill, 'hill')

    elif algorithm_choice == 3:
        algorithm = "expanding_universe"

        buildings = expanding_universe.main(total_houses)

        map_score = calculate_score(buildings)

<<<<<<< HEAD
        buildings, map_score = hillclimber_algoritm.main(total_houses, iterations_hill, buildings, 0)

        visualisation.print_canvas(buildings, 'expanding 60')
        # visualisation.main(buildings, algoritm, total_houses, map_score, False)

    elif algoritm_choice == 4:
        algoritm = "hillclimber_random"

        iterations = input("How many iterations random first?: ")

        best_buildings_random, best_iteration = random_algoritm.main(total_houses, iterations)

        visualisation.print_canvas (best_buildings_random, 'random_2')

        print best_iteration

        iterations_hill = input("How many iterations for hillclimber: ")

        best_buildings_hill, map_score = hillclimber_random.main(iterations_hill, best_buildings_random, best_iteration)

        print map_score
=======
        # iterations_hill = input("How many iterations for hillclimber: ")
        #
        # buildings, map_score = hillclimber_algorithm.main(total_houses, iterations_hill, buildings)

        visualisation.main(buildings, algorithm, total_houses, map_score, False)
>>>>>>> 1eaed68488a0aed0bdbbeb312df3ac3945b3ca15
