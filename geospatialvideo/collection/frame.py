from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, List

if TYPE_CHECKING:
    from geospatialvideo.frame import Frame


@dataclass
class FrameCollection:
    frames: List["Frame"]

    def filter(self, predicate: Callable[["Frame"], bool]) -> "FrameCollection":
        return FrameCollection([f for f in self.frames if predicate(f)])

    def overlay(self) -> None:
        pass
