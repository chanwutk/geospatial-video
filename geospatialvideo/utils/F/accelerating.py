from geospatialvideo.instance import Instance
from geospatialvideo.frame import Frame

from .dist import dist

# Checks if an instance is accelerating.
# Assumes that frames are isochronous; that is, they are recorded at regular time intervals.
# Input should be the result of two sliding operations.

def accelerating(i: "Instance", f1: "Frame", f2: "Frame", f3: "Frame") -> bool:
    loc1 = []
    loc2 = []
    loc3 = []

    for a in i.annotations:
        if a.frame == f1:
            loc1 = [a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]]
        elif a.frame == f2:
            loc2 = [a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]]
        elif a.frame == f3:
            loc3 = [a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]]

    return dist(loc1, loc2) < dist(loc2, loc3)
