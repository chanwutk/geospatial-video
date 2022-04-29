from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, List

if TYPE_CHECKING:
    from geospatialvideo.collection.joined_instance import \
        JoinedInstanceCollection
    from geospatialvideo.instance import Instance


@dataclass
class InstanceCollection:
    instances: List["Instance"]

    def crossproduct(self, *others: "InstanceCollection", on: str = "frame") -> "JoinedInstanceCollection":
        pass

    def filter(self, predicate: Callable[["Instance"], bool]) -> "InstanceCollection":
        pass

    def overlay() -> None:
        pass
