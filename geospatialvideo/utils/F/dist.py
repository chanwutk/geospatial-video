from math import sqrt

# Helper function to calculate distance for custom functions


def dist(loc1: list, loc2: list) -> float:
    assert len(loc1) == len(loc2)
    d = 0
    for x, y in zip(loc1, loc2):
        d += (x - y) ** 2
    return sqrt(d)
