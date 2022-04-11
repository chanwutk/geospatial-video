from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame
    from geospatialvideo.instance import Instance


@dataclass
class Video:
    video_file: Optional[str]
    frames: list["Frame"]
    instances: list["Instance"]
