"""
This script tests the functions in the stars script

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

from stars import *
import turtle
import time


def get_turtle():
    """
    This is a helper function for testing with the turtle module. It takes no inputs,
    and it returns existing turtle if there is one, otherwise makes a  new
    turtle object and returns it.
    """
    existing_turts = turtle.turtles()

    if not existing_turts:    # if list of existing turtles is empty  (~= False)
        return turtle.Turtle()
    else:
        return existing_turts[0]


def star_outline_test():
    """
    Testing program for the starOutline program, must be visually checked
    """
    print()
    print("=== Testing star_outline === CHECK VISUALLY ===")

    screen = turtle.Screen()
    screen.reset()
    sp = get_turtle()
    sp.speed(0)

    print("> Test 1: two star shapes, small back one in middle, large red one "
          "to left.")
    sp.speed(0)
    assert star_outline(sp, 50) is None
    sp.up()
    sp.goto(-300, 0)
    sp.color('red')
    sp.down()
    assert star_outline(sp, 90) is None
    time.sleep(2.0)
    screen.reset()

    print("> Test 2: grid of star shapes")
    assert grid_of_stars(sp) is None
    time.sleep(2.0)
    screen.reset()

    sp.speed(0)
    print("> Test 3: spiral of star shapes with angle 5")
    assert spiral_of_stars(sp, 5) is None
    time.sleep(2.0)
    screen.reset()

    sp.speed(0)
    print("> Test 4: spiral of star shapes with angle 15")
    assert spiral_of_stars(sp, 15) is None
    time.sleep(2.0)
    screen.reset()

    sp.speed(0)
    print("> Test 5: spiral of star shapes with angle 2")
    assert spiral_of_stars(sp, 2) is None
    time.sleep(2.0)
    screen.reset()

    sp.speed(0)
    print("> Test 6: spiral of star shapes with angle 90")
    assert spiral_of_stars(sp, 90) is None
    time.sleep(2.0)
    screen.reset()

    print("*** all assertions passed *** check correctness visually ***")


if __name__ == "__main__":
    star_outline_test()
