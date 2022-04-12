from ..geospatialvideo.collection import Annotations, Frames, Instances, JoinedInstances, Videos
from ..geospatialvideo import Annotation, Frame, Instance, Video

videos = Videos([])


cars = (videos
    .flatmap_instances()
    .filter(lambda i: i.property["type"] == "car")
)
cars.overlay()


########################################################################

twocars = (videos
    .flatten_frames()
    .filter(lambda frame:
        len(Annotations
            .from_frame(frame)
            .filter(lambda a: a.instance.property["type"] == "car")
        ) >= 2
    )
)
twocars.overlay()


########################################################################

def move_away(i1: "Instance", i2: "Instance") -> bool:
    pass

away = (videos
    .flatmap_instances()
    .crossproduct(videos.flatmap_instances(), on="video")
    .filter(lambda i1, i2: move_away(i1, i2))
)
away.overlay()
