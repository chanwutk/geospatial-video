from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame


@dataclass
class FrameCollection:
    frames: list["Frame"]

    def filter(self, predicate: Callable[["Frame"], bool]) -> "FrameCollection":
        pass

    def overlay(self) -> None:
        pass