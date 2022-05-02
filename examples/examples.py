from __future__ import annotations
from math import sqrt
from ..geospatialvideo.collection import AnnotationCollection, FrameCollection, InstanceCollection, JoinedInstanceCollection, VideoCollection
from ..geospatialvideo import Annotation, Frame, Instance, Video

v1 = Video.from_db(id="v1")
v2 = Video.from_db(id="v2")
v3 = Video.from_db(id="v3")
v4 = Video.from_db(id="v4")
v5 = Video.from_db(id="v5")
videos = VideoCollection([v1, v2, v3, v4, v5])


result = videos \
    .flatten_instances() \
    .filter(lambda i: i.property["type"] == "car")

result.overlay()

"""
English Translation:
We find all the instances (objects) across all the videos,
and filter for all the instances (objects) that are cars
"""


########################################################################

result = videos \
    .flatten_frames() \
    .filter(lambda frame:
        len(
            AnnotationCollection
                .from_frame(frame)
                .filter(lambda a: a.instance.property["type"] == "car")
        ) >= 2
    )

result.overlay()

"""
English Translation:
We take all the frames across all the videos,
and filter for frames that have at least 2 cars in them.

"""


########################################################################

# Helper function to calculate distance for custom functions
def dist(loc1: list, loc2: list) -> float:
    assert(len(loc1) == len(loc2))
    d = 0
    for x, y in zip(loc1, loc2):
        d += (x - y) ** 2
    return sqrt(d)

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
    for i in range(len(distances) - 1):
        if distances[i] > distances[i+1]:
            check[i], check[i+1] = True, True

    return any(check)

result = videos \
    .flatten_instances() \
    .crossproduct(videos.flatten_instances(), on="frame") \
    .filter(lambda i1, i2: move_away(i1, i2))

result.overlay()

"""
English Translation:
We filter for all instances that move away from another instance,
or have another instance move away from them.
"""


########################################################################

people = videos \
    .flatten_instances() \
    .filter(lambda i: i.property["type"] == "person")

car = videos \
    .flatten_instances() \
    .filter(lambda i: i.property["type"] == "car")

result = people \
    .crossproduct(car, on="frame") \
    .filter(lambda i1, i2: move_away(i1, i2))

result.overlay()

"""
English Translation:
We filter for all people who are moving away from a car or have a car moving away from them.
"""


########################################################################

result = videos \
    .flatten_instances() \
    .filter(lambda i: i.property["type"] == "car") \
    .filter(lambda i: i.property["relative-x"] < 0)

result.overlay()

"""
English Translation:
We filter for all cars that are to the left of the camera
"""
