from geospatialvideo.instance import Instance

from .dist import dist

# Checks if an instance is accelerating.
# Assumes that frames are isochronous; that is, they are recorded at regular time intervals.


def accelerating(i: "Instance") -> bool:
    locations = []
    for a in i.annotations:
        locations.append([a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]])

    distance = 0.0
    for l in range(len(locations) - 1):
        d = dist(locations[l], locations[l + 1])
        if l > 0:
            if d - distance < 0:
                return False
        distance = d

    return True
