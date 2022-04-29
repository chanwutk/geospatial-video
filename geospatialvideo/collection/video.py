import itertools
from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from geospatialvideo.collection.frame import FrameCollection
from geospatialvideo.collection.instance import InstanceCollection

if TYPE_CHECKING:
    from geospatialvideo.video import Video


@dataclass
class VideoCollection:
    videos: List["Video"]

    def flatten_frames(self) -> "FrameCollection":
        return FrameCollection([*itertools.chain(*[v.frames for v in self.videos])])

    def flatten_instances(self) -> "InstanceCollection":
        return InstanceCollection([*itertools.chain(*[v.instances for v in self.videos])])
