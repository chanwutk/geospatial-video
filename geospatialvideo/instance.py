from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional

if TYPE_CHECKING:
    from geospatialvideo.annotation import Annotation
    from geospatialvideo.video import Video


@dataclass
class Instance:
    video: Optional["Video"]
    annotations: List["Annotation"]
    property: Dict[str, Any]

    @staticmethod
    def from_db(id: str) -> "Instance":
        return Instance(None, [], {})
