import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from geospatialvideo.annotation import Annotation
    from geospatialvideo.video import Video


@dataclass
class Frame:
    video: "Video"
    order: int
    timestamp: datetime.datetime
    annotations: List["Annotation"]
    propperty: Dict[str, Any]

    @staticmethod
    def from_db(id: str) -> "Frame":
        pass
