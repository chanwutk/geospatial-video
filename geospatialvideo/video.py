from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame
    from geospatialvideo.instance import Instance


@dataclass
class Video:
    video_file: str | list[str]
    frames: list["Frame"]
    instances: list["Instance"]
