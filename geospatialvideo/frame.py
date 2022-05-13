import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional

if TYPE_CHECKING:
    from geospatialvideo.annotation import Annotation
    from geospatialvideo.video import Video


@dataclass
class Frame:
    video: Optional["Video"]
    order: int
    timestamp: datetime.datetime
    annotations: List["Annotation"]
    property: Dict[str, Any]

    @staticmethod
    def from_db(id: str, order: int) -> "Frame":
        frame_annotations = Annotation.from_db(scene_id=id, frame_order=order)
        timestamp = frame_annotations['timestamp']
        properties = frame_annotations.property

        return Frame(None, order, timestamp, frame_annotations, properties)
