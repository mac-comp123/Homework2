"""
This script tests the functions in the sled script

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

from sled import *
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


def draw_sledding_hill_test():
    """
    Test the draw_sledding_hill function
    """

    print()
    print("=== Testing drawSleddingHill === CHECK VISUALLY ===")
    print()
    print("> Test 1: draw a big blue sled on the left with pose 1, and a big "
          "orange sled on the right with pose 2")

    screen = turtle.Screen()
    sp = get_turtle()
    sp.speed(0)
    sp.up()
    sp.backward(400)
    sp.down()
    assert draw_sled(sp, "blue", 300, 1) is None
    sp.up()
    sp.goto(0, 0)
    sp.setheading(0)
    sp.forward(200)
    sp.down()
    assert draw_sled(sp, "orange", 300, 2) is None
    time.sleep(12)
    screen.reset()

    # sp.hideturtle()

    print("> Test 2: draw the whole hillside scene")
    assert draw_sledding_hill(screen, sp, 1000, 1000) is None

    time.sleep(12)
    screen.reset()

    print("*** all assertions passed *** check correctness visually ***")


if __name__ == "__main__":
    draw_sledding_hill_test()
