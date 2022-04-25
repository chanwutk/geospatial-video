from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geospatialvideo.video import Video
    from geospatialvideo.collection.instance import InstanceCollection
    from geospatialvideo.collection.frame import FrameCollection


@dataclass
class VideoCollection:
    videos: list["Video"]

    def flatten_frames(self) -> "FrameCollection":
        pass

    def flatten_instances(self) -> "InstanceCollection":
        pass
