# type: ignore
from __future__ import annotations
from math import sqrt
from geospatialvideo.collection import AnnotationCollection, FrameCollection, InstanceCollection, JoinedInstanceCollection, VideoCollection
from geospatialvideo import Annotation, Frame, Instance, Video

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

result = videos \
    .flatten_instances() \
    .crossproduct(videos.flatten_instances(), on="frame") \
    .sliding(2) \
    .filter(lambda i1, i2, f1, f2: move_away(i1, i2, f1, f2))

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
