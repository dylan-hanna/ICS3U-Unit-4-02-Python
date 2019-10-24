#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Oct 2019
# This program uses a while loop

import constants

def main():
    # this function uses a while loop
    loop_counter = 1
    loop_sum = 1

    # input
    positive_integer = int(input("Enter how many times to repeat: "))
    print("")

    # process & output
    while loop_counter < (positive_integer + 1):
        loop_sum = loop_counter * loop_sum
        loop_counter = loop_counter + 1
        
    print(loop_sum)


if __name__ == "__main__":
    main()
    