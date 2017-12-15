from algorithms import *
import visualisation.canvas_visualisation as visualisation

if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")

    while total_houses < 7:
        total_houses = input("Choose number bigger than 7: ")

    algorithm_choice = input("Which algorithm? [1: random], [2: hillclimber], [3: expanding universe], [4: greedy algorithm]")

    if algorithm_choice == 1:
        algorithm = "random"
        iterations = input("How many iterations?: ")

        best_district, best_iteration, end_time = random_algorithm.main(total_houses, iterations)
        visualisation.main(best_district.buildings, algorithm, total_houses, best_iteration, end_time, iterations, 0)

    elif algorithm_choice == 2:
        algorithm = "hillclimber"

        choice = input("Which hillclimber method do you want: [1: random], [2: systematic], [3: Move, rotate, swap]")

        iterations = input("How many iterations random first?: ")

        iterations_hill = input("How many iterations for hillclimber: ")

        best_district_random, best_iteration, end_time = random_algorithm.main(total_houses, iterations)

        if choice == 1:
            variation = "random"

            visualisation.main(best_district_random.buildings, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_random.main(iterations_hill, best_district_random, best_iteration)

        elif choice == 2:
            variation = "systematic"

            visualisation.main(best_district_random.buildings, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_algorithm.main(iterations_hill, best_district_random, best_iteration)

        elif choice == 3:
            variation = "Move_rotate_swap"

            visualisation.main(best_district_random.buildings, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_rotate_move_swap.main(iterations_hill, best_district_random, best_iteration)

        visualisation.main(best_district_hill.buildings, algorithm, total_houses, best_map_score, end_time, iterations_hill, variation, "result")

    elif algorithm_choice == 3:
        algorithm = "expanding_universe"

        buildings = expanding_universe.main(total_houses)

        map_score = calculate_score(buildings)

        iterations_hill = input("How many iterations for hillclimber: ")

        buildings, total_score = hillclimber_algorithm.main(iterations_hill, buildings, 0)

        # visualisation.main(buildings, algorithm, total_houses, map_score, False)
        visualisation.main(buildings, algorithm, total_houses, best_iteration, end_time, iterations)

    elif algorithm_choice == 4:

        algorithm = "try_greedy"

        try_greedy.main(total_houses)
