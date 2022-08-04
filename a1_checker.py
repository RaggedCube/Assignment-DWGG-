"""CSC108: Summer 2022 -- Assignment 1: Where's That Word?

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

DO NOT MAKE CHANGES TO THIS FILE.

All of the files in this folder are:
Copyright (c) 2022 the University of Toronto CSC108 Teaching Team.
"""

from typing import Any, Dict
import sys
import os
import checker_generic
import unittest

sys.path.insert(0, os.getcwd())
import puzzle_functions as pf

sys.path.insert(0, "pyta")
import python_ta

PYTA_CONFIG = "pyta/a1_pyta.txt"
FILENAME = "puzzle_functions.py"
TARGET_LEN = 79
SEP = "="

CONSTANTS = {
    "FORWARD_FACTOR": 1,
    "DOWN_FACTOR": 2,
    "BACKWARD_FACTOR": 3,
    "UP_FACTOR": 4,
    "THRESHOLD": 5,
    "BONUS": 12,
}


def run_pyta(filename: str, config_file: str) -> None:
    """Run PYTA with configuration config_file on the file named filename."""
    error_message = (
        "\nCould not install or run the style checker correctly.\n"
        "Please try to re-run the checker once more.\n\n"
        "If you have already tried to re-run it, please go to office hours\n"
        "in order to resolve this. "
        "For now, you may upload your code to MarkUs and run the self-test\n"
        "to see the style checker results."
    )

    try:
        python_ta.check_all(filename, config=config_file)
    except:
        print(error_message)


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test_get_current_player(self) -> None:
        """Function get_current_player"""
        self._check(pf.get_current_player, [True], str)

    def test_get_winner(self) -> None:
        """Function get_winner"""
        self._check(pf.get_winner, [17, 32], str)

    def test_reverse(self) -> None:
        """Function reverse"""
        self._check(pf.reverse, ["hello"], str)

    def test_get_row(self) -> None:
        """Function get_row"""
        self._check(pf.get_row, ["abcd\nefgh\nijkl\n", 1], str)

    def test_get_factor(self) -> None:
        """Function get_factor"""
        self._check(pf.get_factor, ["forward"], int)

    def test_get_points(self) -> None:
        """Function get_points"""
        self._check(pf.get_points, ["up", 7], int)

    def test_check_guess(self) -> None:
        """Function check_guess"""
        self._check(pf.check_guess, ["abcd\nefgh\nijkl\n", "forward", "bcd", 2, 4], int)

    def test_check_constants(self) -> None:
        """Values of constants."""

        print("\nChecking that constants refer to their original values ... ", end="")
        self._check_constants(CONSTANTS, pf)
        print("check complete")

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print("\nChecking {} ... ".format(func.__name__), end="")
        result = checker_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print("check complete")

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = "The value of constant {} should be {} but is {}.".format(
                name, expected, actual
            )
            self.assertEqual(expected, actual, msg)


print("".center(TARGET_LEN, SEP))
print(" Start: checking coding style ".center(TARGET_LEN, SEP))
run_pyta(FILENAME, PYTA_CONFIG)
print(" End checking coding style ".center(TARGET_LEN, SEP))

print(" Start: checking type contracts ".center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(" End checking type contracts ".center(TARGET_LEN, SEP))

print("\nScroll up to see ALL RESULTS:")
print("  - checking coding style")
print("  - checking type contract\n")
