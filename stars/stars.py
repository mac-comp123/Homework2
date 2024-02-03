"""
This script draws generic start

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

# TODO: add your function here


def grid_of_stars(ted):
    """
    Takes in a turtle as input, and displays a turtle graphics screen. The turtle
    in it draws 9 star shapes in a grid
    """
    ted.speed(0)
    for coord in [(0, 0), (-200, 0), (-200, -200),
                  (0, -200), (200, -200), (200, 0),
                  (200, 200), (0, 200), (-200, 200)]:
        ted.up()
        ted.goto(coord)
        ted.down()
        star_outline(ted, 60)


def spiral_of_stars(tad, angle):
    """
    Takes in a turtle and an angle as inputs.  Displays a turtle graphics screen.
    It then draws a series of star shapes, each one rotated by the input angle,
    and a bit bigger than the previous
    """
    tad.speed(0)
    for size in range(20, 200, 10):
        star_outline(tad, size)
        tad.left(angle)
