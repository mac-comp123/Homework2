"""
This script draws a sledding scene

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

import turtle
import random


def sledding_hill_main(win_wid=1000, win_hgt=1000):
    """
    Sets up the screen and turtle and then calls the real main,
    draw_sledding_hill.  Note that winWid is the total width in pixels of the
    screen, and win_hgt is the total height in pixels of the screen.  The
    default values are 1000 by 1000: if you don't pass any inputs to this
    function that will be the values. Thus, the screen's coordinates will run
    from -500 to 500 by default.
    """
    screen = turtle.Screen()
    sh_turt = turtle.Turtle()
    draw_sledding_hill(screen, sh_turt, win_wid, win_hgt)
    screen.exitonclick()


def draw_sledding_hill(screen, sled_t, win_wid, win_hgt):
    """
    Takes in a screen object, a turtle, and the width and height for the
    overall window, and draws the overall scene. It sets up the screen to
    have the specified size, sets up the turtle to draw fast, draws the hillside,
    and then draws all the randomized sledders.
    """
    screen.setup(win_wid, win_hgt)
    min_wid = -win_wid // 2
    max_wid = win_wid // 2
    min_hgt = -win_hgt // 2
    max_hgt = win_hgt // 2

    sled_t.speed(0)
    # sled_t.hideturtle()

    # Draw hillside and sky
    screen.bgcolor("snow")
    draw_sky(sled_t, max_wid, max_hgt)

    # Draws a total of 16 sleds scattered across the scene, with larger ones
    # at the bottom left, smaller at the upper right
    wid_quarter = int(win_wid / 4)
    hgt_quarter = int(win_hgt / 4)
    for cellX in range(min_wid, max_wid, wid_quarter):
        for cellY in range(max_hgt, min_hgt, -hgt_quarter):
            sled_t.up()
            col = random.choice(['hot pink', 'lightcoral', 'deep sky blue',
                                 'mediumorchid', 'medium sea green', 'coral'])
            curr_x = cellX + random.randint(0, wid_quarter // 2)
            curr_y = cellY - random.randint(0, hgt_quarter // 2)
            if (curr_x < 0) and (curr_y < 0):
                rand_len = random.randrange(100, 150, 5)
            elif (curr_x > 0) and (curr_y > 0):
                rand_len = random.randrange(25, 75, 5)
            else:
                rand_len = random.randrange(75, 100, 5)
            sled_t.goto(curr_x, curr_y)
            rand_head = random.randint(-30, 30)
            sled_t.setheading(rand_head)
            sled_t.down()
            pose = random.choice([1, 2])
            print("Sled:", curr_x, curr_y, rand_len, rand_head, pose)
            draw_sled(sled_t, col, rand_len, pose)


def draw_sky(hill_t, wid, hgt):
    """
    Draws the edge of the hill with blue sky beyond
    """
    wid_q = wid / 2

    hill_t.color("light cyan")
    hill_t.up()
    hill_t.goto(-wid_q, hgt)
    hill_t.down()

    hill_t.begin_fill()
    hill_t.goto(wid, 0)
    hill_t.goto(wid, hgt)
    hill_t.goto(-wid_q, hgt)
    hill_t.end_fill()

    hill_t.up()
    hill_t.goto(0, 0)
    hill_t.down()


def draw_sled(turt, color, size, which_pose):
    """
    Takes in a turtle object, a color for the sled, and a size for the
    sled,  and which of the two poses to draw, and it draws a cartoon sled
    with a person on it, either sitting upright or lying down. The sled is
    draw at the turtle's current location and with the turtle's current heading.
    """

    # Print the original coordinates and heading so we can verify that the turtle returns to this spot
    # between drawing the sled and drawing the person
    # print("START POSE", dot_turt.pos(), dot_turt.heading())

    # Setup initial values (color, pen width, location, and sizes, proportional to the input size
    turt.color(color)
    turt.width(int(0.08 * size))
    (start_x, start_y) = turt.pos()
    base_len = 0.2 * size
    stub_len = 0.16 * size

    # Draw runner of sled
    turt.right(20)
    turt.forward(size)
    turt.right(20)
    turt.forward(base_len)
    turt.left(90)
    turt.forward(base_len)

    # Go back to the start and face the same direction as originally facing
    turt.up()
    turt.goto(start_x, start_y)
    turt.right(90)
    turt.down()
    # print("MID POSE", dot_turt.pos(), dot_turt.heading())

    # Draw the supports for the seat
    turt.right(20)
    for dist in [base_len, 3 * base_len]:
        turt.forward(dist)
        turt.left(90)
        turt.forward(stub_len)
        turt.backward(stub_len)
        turt.right(90)

    # Move to the front of the seat, ready to draw it
    turt.up
    turt.forward(0.1 * size)
    turt.left(90)
    turt.forward(stublen)
    turt.left(90)
    turt.down()

    # Draw the sled's seat
    turt.forward(0.8 * size)

    # Move back to the original position and heading
    turt.up()
    turt.goto(start_x, start_y)
    turt.right(16)
    turt.down()

    # print("END POSE", dot_turt.pos(), dot_turt.heading())

    # Draw person on sled in one of two poses, based on input
    if which_pose == 1:
        draw_pose1(turt, size)
    else:
        draw_pose1(turt, size)


def draw_pose1(turt, size):
    """
    Takes in a turtle and a size, and it draws a person sitting upright
    and leaning forward on the sled. It assumes that the turtle is in the
    location and facing the same direction as it was when it started
    to draw the sled.
    """
    # Set up some standard sizes to use, proportional to the original size
    stub_len = 0.26 * size
    head_gap = 0.3 * size
    body_width = 0.25 * size
    body_height = 0.4 * size
    leg_width = 0.15 * size

    # Get ready to draw the body
    turt.width(body_width)

    # Move to where the bottom of the torso will be
    turt.up()
    turt.right(20)
    turt.forward(body_width)
    turt.left(90)
    turt.forward(stub_len)
    turt.down()
    (x, y) = turt.pos()

    # Draw the person's body
    turt.right(15)
    turt.forward(body_height)

    # Move forward leaving a gap for the neck
    turt.up()
    turt.forward(head_gap)
    turt.down()

    # Draw the head, slightly wider than the body
    turt.dot(body_width+5)

    # Get ready to draw the legs
    turt.width(leg_width)

    # Move back to the bottom of the torso and shift to where legs start
    turt.up()
    turt.goto(x, y)
    turt.right(75)
    turt.forward(body_width/2)
    turt.down()

    # Draw the upper leg and then the lower leg
    turt.left(35)
    turt.forward(body_width)
    turt.right(90)
    turt.forward(body_width)


def draw_pose2(turt, size):
    """
    Takes in a turtle and a size, and it draws the person lying on the
    sled  and holding on to the front.  It assumes that the turtle is in the
    location and facing the same direction as it was when it started
    to draw the sled.
    """

    # Set up some lengths for the parts, proportional to the size
    stub_len = 0.26 * size
    head_gap = 0.2 * size
    body_width = 0.25 * size
    body_height = 0.35 * size
    leg_width = 0.15 * size

    # Move to the bottom of the torso
    turt.up()
    turt.right(20)
    turt.forward(body_width)
    turt.left(90)
    turt.forward(stub_len)
    turt.down()

    # Draw the legs flying up into the air, returning to the bottom of the torso afterwards
    turt.left(60)
    turt.width(leg_width)
    turt.forward(2 * body_height)
    turt.backward(2 * body_height)
    turt.right(60)

    # Draw the torso of the body
    turt.width(body_width)
    turt.right(90)
    turt.forward(body_height)

    # Move to where the head should be
    turt.up()
    turt.forward(head_gap)
    turt.left(90)
    turt.forward(head_gap)
    turt.down()

    # Draw the head
    turt.dot(body_width + 5)

    # Move to the shoulder where the arm should start
    turt.up()
    turt.backward(head_gap)
    turt.right(90)
    turt.backward(head_gap)
    turt.down()

    # Draw upper and then lower arm holding sled
    turt.width(leg_width)
    turt.right(20)
    turt.forward(stub_len)
    turt.left(40)
    turt.forward(stub_len)
