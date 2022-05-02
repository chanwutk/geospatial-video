from geospatialvideo.instance import Instance

from .dist import dist

# Checks if an instance is decelerating.
# Assumes that frames are isochronous; that is, they are recorded at regular time intervals.


def decelerating(i: "Instance") -> bool:
    locations = []
    for a in i.annotations:
        locations.append([a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]])

    distance = 0.0
    for ix in range(len(locations) - 1):
            d = dist(locations[ix], locations[ix + 1])
            if ix > 0:
                if d - distance > 0:
                    return False
            distance = d

    return True
