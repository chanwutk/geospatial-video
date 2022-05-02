from geospatialvideo.instance import Instance

from .dist import dist

# Checks for all instances that ever move away from another instance,
# or have another instance move away from them


def move_away(i1: "Instance", i2: "Instance") -> bool:
    annotations = []
    for a1 in i1.annotations:
        for a2 in i2.annotations:
            if a1.frame == a2.frame:
                annotations.append([a1, a2])

    distances = []
    for a1, a2 in annotations:
        x = [a1.property["x_loc"], a1.property["y_loc"], a1.property["z_loc"]]
        y = [a2.property["x_loc"], a2.property["y_loc"], a2.property["z_loc"]]
        distances.append(dist(x, y))

    check = [False] * len(distances)
    for l in range(len(distances) - 1):
        if distances[l] > distances[l + 1]:
            check[l], check[l + 1] = True, True

    return any(check)
