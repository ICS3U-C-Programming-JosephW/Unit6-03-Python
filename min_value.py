#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 24, 2025
# This program generates and displays ten
# random numbers from 0 to 100 with lists
# and then displays the minimum number.

# Import the constants module for useful constants.
import constants

# Import the random module for the random integer function.
import random


# Define a function to get the minimum
# number out of a number list.
def find_min_value(num_list):
    # Initialize the current minimum
    # number to zero to use it later.
    current_min_value = 0

    # Use a for..in loop to loop over
    # every number in the list.
    for number in num_list:
        # Check if the number is lesser
        # than the current minimum number.
        if number < current_min_value:
            # Set the current minimum
            # value to the number.
            current_min_value = number

    # Return the resulting minimum value.
    return current_min_value


# Define the main function.
def main():
    # Print an empty space to format text.
    print("")
    # Initialize a list of integers as
    # an empty list to be used later.
    list_of_int = []

    # Use a for loop to loop over the maximum array
    # size to generate the ten random numbers.
    for index in range(constants.MAX_ARRAY_SIZE):
        # Generate a random number from the minimum number
        # size, 0, to the maximum number size, 100.
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Populate the list by appending the random number.
        list_of_int.append(random_number)

        # Display information about the random
        # number and its current position.
        print(f"{random_number} added to the list at position {index}.")

    # Determine the minimum number by assigning
    # it to the minimum value function.
    min_number = find_min_value(list_of_int)
    # Display the minimum number.
    print(f"\nThe min value is: {min_number}.\n")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
