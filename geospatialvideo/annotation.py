from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame
    from geospatialvideo.instance import Instance


@dataclass
class Annotation:
    instance: "Instance"
    frame: "Frame"
    property: Dict[str, Any]

    def from_db(id: str) -> "Annotation":
        pass
