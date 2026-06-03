#!/usr/bin/python3
"""
Module for calculating retained rainwater
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Args:
        walls: list of non-negative integers representing wall heights

    Returns:
        Integer: total amount of rainwater retained
    """
    if not walls:
        return 0

    n = len(walls)
    total = 0

    for i in range(1, n - 1):
        left_max = max(walls[:i + 1])
        right_max = max(walls[i:])
        water = min(left_max, right_max) - walls[i]
        if water > 0:
            total += water

    return total
