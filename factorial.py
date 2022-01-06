#!/usr/bin/env python3
# Created by: Logan S
# Created on: Jan. 6, 2021
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the
# factorial.


def main():

    # initializations
    loop_counter = 0
    factorial_answer = 1

    # get the user number as string
    user_number_as_string = input("Enter a positive number: ")
    print("")

    try:
        user_number_as_int = int(user_number_as_string)
    except ValueError:
        print("{} is not a number.". format(user_number_as_string))
    else:
        if (user_number_as_int > 0):

            # replicates a do..while loop
            # calculate the factorial of the user number using a loop

            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through loop.".format(loop_counter))
                if loop_counter >= user_number_as_int:
                    break

            print("")
            print("{} = {}!".format(user_number_as_int, factorial_answer))
        elif (user_number_as_int == 0):
            print("0 = 1!")
        else:
            print("{} is not a positive number.". format(user_number_as_int))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
