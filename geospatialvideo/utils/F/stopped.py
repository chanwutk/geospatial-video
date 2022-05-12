from geospatialvideo.frame import Frame
from geospatialvideo.instance import Instance

from .dist import dist

# Checks if an instance is stopped.
# 'tol' parameter allows us to consider an object stopped even if there is slight movement,
# with default tolerance of 0.5 distance units
# Input should be the result of a sliding operation.


def stopped(i: "Instance", f1: "Frame", f2: "Frame", tol: float = 0.5) -> bool:
    loc1 = []
    loc2 = []

    for a in i.annotations:
        if a.frame == f1:
            loc1 = [a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]]
        elif a.frame == f2:
            loc2 = [a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]]

    return dist(loc1, loc2) <= 0.5
