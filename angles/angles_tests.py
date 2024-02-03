"""
This script tests the functions in the angles script

@author: Amin Alhashim (aalhashi@macalester.edu)
@author: Susan Fox
"""

from angles import *


def interior_angle_test():
    """
    Test the interior_angle function

    :return: None
    """
    print()
    print("=== Testing interior_angle ===")
    test_sides = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 45, 53, 100, 360]
    correct_angles = [60.0, 90.0, 108.0, 120.0, 128.57, 135.0, 140.0, 144.0,
                      156.0, 162.0, 172.0, 173.21, 176.4, 179.0]

    for i in range(len(test_sides)):
        num_sides = test_sides[i]
        exp_ans = correct_angles[i]
        res = interior_angle(num_sides)
        print("exterior_angle(" + str(num_sides) + ") returned", res,
              "| correct answer =", exp_ans)
        assert type(res) == float
        assert res == exp_ans

    print("*** all assertions passed ***")


def exterior_angle_test():
    """
    Test the exterior_angle function

    :return: None
    """
    print()
    print("=== Testing exterior_angle ===")

    test_sides = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 45, 53, 100, 360]
    correct_angles = [120.0, 90.0, 72.0, 60.0, 51.43, 45.0, 40.0, 36.0, 24.0,
                      18.0, 8.0, 6.79, 3.6, 1.0]

    for i in range(len(test_sides)):
        num_sides = test_sides[i]
        exp_ans = correct_angles[i]
        res = exterior_angle(num_sides)
        print("exterior_angle(" + str(num_sides) + ") returned", res,
              "| correct answer =", exp_ans)
        assert type(res) == float
        assert res == exp_ans

    print("*** all assertions passed ***")


if __name__ == "__main__":
    interior_angle_test()
    exterior_angle_test()
