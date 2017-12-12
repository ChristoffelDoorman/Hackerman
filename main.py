import random_algoritm
import expanding_universe
import visualisation
import hillclimber_algoritm
import hillclimber_random

import helpers


if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")

    while total_houses < 7:
        total_houses = input("Choose number bigger than 7: ")

    algoritm_choice = input("Which algoritm? [1: random], [2: hillclimber], [3: expanding universe], [4: hillclimber random] ")

    if algoritm_choice == 1:
        algoritm = "random"
        iterations = input("How many iterations?: ")

        buildings, best_iteration = random_algoritm.main(total_houses, iterations)
    	# stop = timeit.default_timer()
    	# print "De tijd is: ", stop - start
        # print ("best iteration is", best_iteration)

        # visualisation.main(buildings, algoritm, 0, 0, False)
        visualisation.main(buildings, algoritm, total_houses, best_iteration, True)


    elif algoritm_choice == 2:
        algoritm = "hillclimber"

        iterations = input("How many iterations random first?: ")

        best_buildings_random, best_iteration = random_algoritm.main(total_houses, iterations)

        visualisation.print_canvas (best_buildings_random, 'random')

        print best_iteration

        iterations_hill = input("How many iterations for hillclimber: ")

        best_buildings_hill, map_score = hillclimber_algoritm.main(iterations_hill, best_buildings_random, best_iteration)

        print map_score

        visualisation.print_canvas(best_buildings_hill, 'hill')

    elif algoritm_choice == 3:
        algoritm = "expanding_universe"

        buildings = expanding_universe.main(total_houses)

        map_score = helpers.calculate_score(buildings)

        iterations_hill = input("How many iterations for hillclimber: ")

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
