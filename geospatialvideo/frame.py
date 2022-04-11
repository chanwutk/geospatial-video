import datetime
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
  from geospatialvideo.annotation import Annotation
  from geospatialvideo.video import Video


@dataclass
class Frame:
    video: "Video"
    frame_file: Optional[str]
    order: int
    timestamp: datetime.datetime
    annotations: list["Annotation"]
