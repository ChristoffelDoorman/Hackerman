# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file runs all the algoritms, from input of user

from algorithms import *
from helpers.helper_functions import calculate_score, print_txt
from helpers import load_district
import visualisation.canvas_visualisation as visualisation


if __name__ == "__main__":

    total_houses = eval(input("Total number of houses?: "))

    water_type = eval(input("Choose your water type? [0: no water], [1: one big pool], [2: two horizontal strokes], [3: two horizontal and two vertical strokes]"))

    while total_houses < 7:

        total_houses = eval(input("Choose an integer number greater than 7: "))

    algorithm_choice = eval(input("Which algorithm? [0: own input file] [1: random], [2: hillclimber], [3: expanding universe], [4: greedy algorithm], [5: collapsing universe]: "))

    if algorithm_choice == 0:

        district, map_score = load_district.main()
        algorithm = "hillclimber"

        choice = eval(input("Which hillclimber method do you want: [1: random], [2: systematic], [3: Move, rotate, swap]"))
        iterations_hill = eval(input("How many iterations for hillclimber: "))

        if choice == 1:
            variation = "random"

            visualisation.main(district, algorithm, total_houses, map_score, 0, 0, variation, "loaded_district")

            best_district_hill, best_map_score, end_time = hillclimber_random.main(iterations_hill, district, map_score, 0)

        elif choice == 2:
            variation = "systematic"

            visualisation.main(district, algorithm, total_houses, map_score, 0, 0, variation, "loaded_district")

            best_district_hill, best_map_score, end_time = hillclimber_algorithm.main(iterations_hill, district, map_score, 0)

        elif choice == 3:
            variation = "Move_rotate_swap"

            visualisation.main(district, algorithm, total_houses, map_score, 0, 0, variation, "loaded_district")

            best_district_hill, best_map_score, end_time = hillclimber_rotate_move_swap.main(iterations_hill, district, map_score, 0)

        else:
            print("choose a valid option")

        visualisation.main(best_district_hill, algorithm, total_houses, best_map_score, end_time, iterations_hill, variation, "result")
        print_txt(best_district_hill, algorithm, total_houses, variation)


    elif algorithm_choice == 1:
        algorithm = "random"
        iterations = eval(input("How many iterations?: "))

        best_district, best_iteration, end_time = random_algorithm.main(total_houses, iterations, water_type)

        visualisation.main(best_district, algorithm, total_houses, best_iteration, end_time, iterations, 0, 0)

        print_txt(best_district, algorithm, total_houses, 0)


    elif algorithm_choice == 2:
        algorithm = "hillclimber"

        choice = eval(input("Which hillclimber method do you want: [1: random], [2: systematic], [3: Move, rotate, swap]"))

        iterations = eval(input("How many iterations random first?: "))

        iterations_hill = eval(input("How many iterations for hillclimber: "))

        best_district_random, best_iteration, end_time = random_algorithm.main(total_houses, iterations, water_type)

        if choice == 1:
            variation = "random"

            visualisation.main(best_district_random, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_random.main(iterations_hill, best_district_random, best_iteration, water_type)

        elif choice == 2:
            variation = "systematic"

            visualisation.main(best_district_random, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_algorithm.main(iterations_hill, best_district_random, best_iteration, water_type)

        elif choice == 3:
            variation = "Move_rotate_swap"

            visualisation.main(best_district_random, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_rotate_move_swap.main(iterations_hill, best_district_random, best_iteration, water_type)

        else:
            print("choose a valid option")

        visualisation.main(best_district_hill, algorithm, total_houses, best_map_score, end_time, iterations_hill, variation, "result")
        print_txt(best_district_hill, algorithm, total_houses, variation)


    elif algorithm_choice == 3:
        algorithm = "expanding_universe"

        district = expanding_universe.main(total_houses)

        map_score = calculate_score(district.buildings)

        iterations_hill = eval(input("How many iterations for hillclimber: "))

        best_district, total_score, end_time = hillclimber_random.main(iterations_hill, district, map_score, water_type)

        visualisation.main(best_district, algorithm, total_houses, total_score, end_time, iterations_hill, 0, "exp with hill")

        print_txt(best_district, algorithm, total_houses, 0)


    elif algorithm_choice == 4:

        algorithm = "greedy"

        district, total_score, end_time = greedy_algorithm.main(total_houses)

        visualisation.main(district, algorithm, total_houses, total_score, end_time, 0, 0, "greedy")
        print_txt(district, algorithm, total_houses, 0)


    elif algorithm_choice == 5:

        algorithm = "collapsing_universe"

        district = collapsing_universe.main(total_houses)

        map_score = calculate_score(district.buildings)

        iterations_hill = eval(input("How many iterations for hillclimber: "))

        best_district, total_score, end_time = hillclimber_random.main(iterations_hill, district, map_score, 0)

        visualisation.main(best_district, algorithm, total_houses, total_score, end_time, iterations_hill, 0, "collaps with hill")

        print_txt(best_district, algorithm, total_houses, 0)
    else:
        print("choose a valid option")
