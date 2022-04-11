from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geospatialvideo.video import Video
    from geospatialvideo.collection.instances import Instances
    from geospatialvideo.collection.frames import Frames


@dataclass
class Videos:
    videos: list["Video"]

    def flatmap_frames(self) -> "Frames":
        pass

    def flatmap_instances(self) -> "Instances":
        pass
