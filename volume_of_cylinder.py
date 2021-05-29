#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sat/May29/2021
# This program calculates the volume of a cylinder


import math


def volume_cylinder(radius_int, height_int):
    # this function calculates the volume of a cylinder using return
    # process
    volume = (math.pi*radius_int**2) * height_int
    # return
    return volume


def main():
    # this function this function call other functions
    print("Starting ...")
    print("\nThis program calculates the volume of a cylinder.")
    print("please enter the radius and height")
    print("\n")
    # input
    radius_from_user = input("The radius is (mm): ")
    height_from_user = input("The height is (mm): ")
    try:
        radius_int = int(radius_from_user)
        height_int = int(height_from_user)
        # call function
        volume_cylinder(radius_int, height_int)
        # output
        print(
            "\nvolume of this cylinder with radius {0}mm and height {1}mm is {2}㎟"
            .format(radius_int, height_int,
                    volume_cylinder(radius_int, height_int)))
    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
