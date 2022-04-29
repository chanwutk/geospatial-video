from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, List

if TYPE_CHECKING:
    from geospatialvideo.annotation import Annotation
    from geospatialvideo.frame import Frame


@dataclass
class AnnotationCollection:
    annotations: List["Annotation"]

    def filter(self, predicate: Callable[["Annotation"], bool]) -> "AnnotationCollection":
        return AnnotationCollection([])

    def overlay(self) -> None:
        pass

    @staticmethod
    def from_frame(frame: "Frame") -> "AnnotationCollection":
        return AnnotationCollection(frame.annotations)
