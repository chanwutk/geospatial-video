from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional
import pandas as pd


if TYPE_CHECKING:
    from geospatialvideo.annotation import Annotation
    from geospatialvideo.video import Video


@dataclass
class Instance:
    video: Optional["Video"]
    annotations: Annotation
    category: str
    property: Dict[str, Any]

    @staticmethod
    def from_db(scene_id: str, frame_order: int, instance_token: str) -> "Instance":
        annotations = Annotation.from_db(scene_id, frame_order)
        frame_properties = pd.DataFrame.from_dict(annotations.property, orient='index')
        instance_properties = frame_properties.loc[instance_token]
        category = instance_properties['category']

        return Instance(None, annotations, category, instance_properties.to_dict())
