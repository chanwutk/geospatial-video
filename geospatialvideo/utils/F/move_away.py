from geospatialvideo.instance import Instance
from geospatialvideo.frame import Frame

from .dist import dist

# Checks for all instances that ever move away from another instance,
# or have another instance move away from them.
# Input should be the result of a sliding operation.

def move_away(i1: "Instance", i2: "Instance", f1: "Frame", f2: "Frame") -> bool:
    i1_loc1 = []
    i1_loc2 = []
    i2_loc1 = []
    i2_loc2 = []

    for a, b in zip(i1.annotations, i2.annotations):
        if a.frame == f1:
            i1_loc1 = [a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]]
            i2_loc1 = [b.property["x_loc"], b.property["y_loc"], b.property["z_loc"]]
        elif a.frame == f2:
            i1_loc2 = [a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]]
            i2_loc2 = [b.property["x_loc"], b.property["y_loc"], b.property["z_loc"]]

    return dist(i1_loc1, i2_loc1) < dist(i1_loc2, i2_loc2)
    