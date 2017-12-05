import random_algoritm


if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")
    algoritm = raw_input("Which algoritm?: ")

    if algoritm == "random":
        iterations = input("How many iterations?: ")

        random_algoritm.main(total_houses, iterations)
