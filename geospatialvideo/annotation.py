from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geospatialvideo.instance import Instance
    from geospatialvideo.frame import Frame


@dataclass
class Annotation:
    instance: "Instance"
    frame: "Frame"
    property: dict
