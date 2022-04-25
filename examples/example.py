from ..geospatialvideo.collection import AnnotationCollection, FrameCollection, InstanceCollection, JoinedInstanceCollection, VideoCollection
from ..geospatialvideo import Annotation, Frame, Instance, Video

videos = VideoCollection([])


cars = videos \
    .flatten_instances() \
    .filter(lambda i: i.property["type"] == "car")
cars.overlay()


########################################################################

twocars = videos \
    .flatten_frames() \
    .filter(lambda frame:
        len(
            AnnotationCollection
                .from_frame(frame)
                .filter(lambda a: a.instance.property["type"] == "car")
        ) >= 2
    )
twocars.overlay()


########################################################################

def move_away(i1: "Instance", i2: "Instance") -> bool:
    pass

away = videos \
    .flatten_instances() \
    .crossproduct(videos.flatten_instances(), on="video") \
    .filter(lambda i1, i2: move_away(i1, i2))
away.overlay()
