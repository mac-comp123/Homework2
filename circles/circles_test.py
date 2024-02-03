"""
This script tests the functions in the circles script

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

from circles import *
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


def random_circles_test():
    """Tests the randomCircles function"""
    print()
    print("=== Testing randomCircles === CHECK VISUALLY ===")
    screen = turtle.Screen()
    sp = get_turtle()
    sp.speed(0)

    print("> First: Weird cases: just one circle!")
    res = random_circles(sp, 1, False)
    assert res is None
    time.sleep(2)
    screen.reset()

    sp.speed(0)
    res = random_circles(sp, 1, True)
    assert res is None
    time.sleep(2)
    screen.reset()

    print("> Second: four circles")
    sp.speed(0)
    res = random_circles(sp, 4, False)
    assert res is None
    time.sleep(2)
    screen.reset()

    sp.speed(0)
    res = random_circles(sp, 4, True)
    assert res is None
    time.sleep(2)
    screen.reset()

    print("> Third: twenty circles")
    sp.speed(0)
    res = random_circles(sp, 20, False)
    assert res is None
    time.sleep(2)
    screen.reset()

    sp.speed(0)
    res = random_circles(sp, 20, True)
    assert res is None
    time.sleep(2)
    screen.reset()

    print("> Fourth: 75 circles")
    sp.speed(0)
    res = random_circles(sp, 75, False)
    assert res is None
    time.sleep(2)
    screen.reset()

    sp.speed(0)
    res = random_circles(sp, 75, True)
    assert res is None
    time.sleep(2)
    screen.reset()

    print("*** all assertions passed *** check correctness visually ***")


if __name__ == "__main__":
    random_circles_test()
