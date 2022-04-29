from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Union

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame
    from geospatialvideo.instance import Instance


@dataclass
class Video:
    video_file: Union[str, List[str]]
    frames: List["Frame"]
    instances: List["Instance"]
    property: Dict[str, Any]

    @staticmethod
    def from_db(id: str) -> "Video":
        return Video("", [], [], {})
