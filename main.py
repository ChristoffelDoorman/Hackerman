import random_algoritm
import expanding_universe
import visualisation
import hillclimber_algoritm

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

        print ("best iteration is", best_iteration)

        # visualisation.main(buildings, algoritm, 0, 0, False)
        visualisation.main(buildings, algoritm, total_houses, best_iteration, True)


    elif algoritm_choice == 2:
        algoritm = "hillclimber"

        iterations = input("How many iterations random first?: ")

        buildings, best_iteration = random_algoritm.main(total_houses, iterations)

        iterations_hill = input("How many iterations for hillclimber: ")

        hillclimber_algoritm.main(total_houses, iterations_hill, buildings)


    elif algoritm_choice == 3:
        algoritm = "expanding_universe"

        buildings = expanding_universe.main(total_houses)

        print "score is: ", helpers.calculate_score(buildings)

        visualisation.main(buildings, algoritm, total_houses, 0, False)
