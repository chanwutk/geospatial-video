from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geospatialvideo.annotation import Annotation
    from geospatialvideo.video import Video


@dataclass
class Instance:
    video: "Video"
    annotations: list["Annotation"]
    property: dict
