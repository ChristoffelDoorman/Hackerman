import random_algoritm
import expanding_universe
import hillclimber_algoritm


if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")
    algoritm = raw_input("Which algoritm?: ")

    if algoritm == "random":
        iterations = input("How many iterations?: ")

        random_algoritm.main(total_houses, iterations)

    elif algoritm == "hillclimber":

        iterations = input("How many iterations random first?: ")

        buildings = random_algoritm.main(total_houses, iterations)

        iterations_hill = input("How many iterations for hillclimber: ")

        hillclimber_algoritm.main(total_houses, iterations_hill, buildings)


    elif algoritm == "expanding universe":

        expanding_universe.main(total_houses)
