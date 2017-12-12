import algorithms
import random_algoritm
import expanding_universe
import hillclimber_algoritm
import visualisation
import classes
import helpers



if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")

    while total_houses < 7:
        total_houses = input("Choose number bigger than 7: ")

    algoritm_choice = input("Which algoritm? [1: random], [2: hillclimber], [3: expanding universe]: ")

    if algoritm_choice == 1:
        algoritm = "random"
        iterations = input("How many iterations?: ")

        buildings, best_iteration = random_algoritm.main(total_houses, iterations)
    	stop = timeit.default_timer()
    	print "De tijd is: ", stop - start
        print ("best iteration is", best_iteration)

        # visualisation.main(buildings, algoritm, 0, 0, False)
        visualisation.main(buildings, algoritm, total_houses, best_iteration, True)


    elif algoritm_choice == 2:
        algoritm = "hillclimber"

        iterations = input("How many iterations random first?: ")

        buildings1, best_iteration = random_algoritm.main(total_houses, iterations)

        visualisation.print_canvas(buildings1, 'random')

        print best_iteration

        iterations_hill = input("How many iterations for hillclimber: ")

        buildings2, map_score = hillclimber_algoritm.main(total_houses, iterations_hill, buildings1)

        print map_score

        visualisation.print_canvas(buildings2, 'hill')


    elif algoritm_choice == 3:
        algoritm = "expanding_universe"

        buildings = expanding_universe.main(total_houses)

        map_score = helpers.calculate_score(buildings)

        # iterations_hill = input("How many iterations for hillclimber: ")
        #
        # buildings, map_score = hillclimber_algoritm.main(total_houses, iterations_hill, buildings)

        visualisation.main(buildings, algoritm, total_houses, map_score, False)
