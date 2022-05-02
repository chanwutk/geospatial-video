from geospatialvideo.instance import Instance

# Checks if an instance is stopped.
# 'tol' parameter allows us to consider an object stopped even if there is slight movement,
# with default tolerance of 0.5 distance units


def stopped(i: "Instance", tol: float = 0.5) -> bool:
    locations = []
    for a in i.annotations:
        locations.append([a.property["x_loc"], a.property["y_loc"], a.property["z_loc"]])

    check = [False] * len(locations)
    for l in range(len(locations) - 1):
        if locations[l] - locations[l + 1] <= 0.5:
            check[l], check[l + 1] = True, True

    return any(check)
