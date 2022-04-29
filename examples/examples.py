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

def move_away(i1: "Instance", i2: "Instance") -> bool:
    pass

result = videos \
    .flatten_instances() \
    .crossproduct(videos.flatten_instances(), on="frame") \
    .filter(lambda i1, i2: move_away(i1, i2))

result.overlay()

"""
English Translation:
We filter for all instances who are moving away from an instance,
or have another instance moving away from them.
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
