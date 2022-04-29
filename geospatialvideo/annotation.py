from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame
    from geospatialvideo.instance import Instance


@dataclass
class Annotation:
    instance: Optional["Instance"]
    frame: Optional["Frame"]
    property: Dict[str, Any]

    @staticmethod
    def from_db(id: str) -> "Annotation":
        return Annotation(None, None, {})
