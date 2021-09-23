#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program is a random number guessing game

import random


def main():
    # this function is the game

    # input
    guessed_number_as_string = input("Guess a number between 0-9: ")
    some_variable = random.randint(0, 9)  # a number between 0-9

    # process & output
    try:
        guessed_number = int(guessed_number_as_string)

        if guessed_number == some_variable:
            print("You guessed correctly!")
        else:
            print("You guessed wrong!")
            print("")
            print("The correct answer was {0}.".format(some_variable))

    except Exception:
        print("Invalid number guessed, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
