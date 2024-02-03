"""
This script tests the functions in the squares script

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

from squares import *
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


def square_main_test():
    """
    Test the square_main function
    """
    print()
    print("=== Testing square_main === CHECK VISUALLY ===")

    screen = turtle.Screen()
    screen.reset()
    sp = get_turtle()
    sp.speed(0)

    res = square_main(sp, ['cyan', 'purple', 'pink', 'blue'], 100)
    assert res is None
    time.sleep(2.0)
    screen.reset()

    sp.speed(0)
    res = square_main(sp, ['red', 'orange', 'yellow', 'green', 'blue'], 50)
    assert res is None
    time.sleep(2.0)
    screen.reset()

    sp.speed(0)
    cols1 = ["#922B21", "#C0392B", "#E6B0AA", "#922B21", "#C0392B", "#E6B0AA",
             "#922B21", "#C0392B", "#E6B0AA"]
    cols2 = ["#C0392B", "#E6B0AA", "#922B21", "#C0392B", "#E6B0AA", "#922B21",
             "#C0392B", "#E6B0AA", "#922B21"]
    cols3 = ["#E6B0AA", "#922B21", "#C0392B", "#E6B0AA", "#922B21", "#C0392B",
             "#E6B0AA", "#922B21", "#C0392B"]
    all_cols = [cols1, cols2, cols3, cols1, cols2, cols3, cols1, cols2, cols3]
    sq_size = 75
    for i in range(9):
        vert_dist = (sq_size * (9 - i - 1)) - (4 * sq_size)
        col_list = all_cols[i]
        sp.up()
        sp.goto(0, vert_dist)
        sp.down()
        res = square_main(sp, col_list, sq_size)
        assert res is None
    time.sleep(2.0)

    print("*** all assertions passed *** check correctness visually ***")


if __name__ == "__main__":
    square_main_test()
