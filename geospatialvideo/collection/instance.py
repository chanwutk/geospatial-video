from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from geospatialvideo.collection.joined_instance import (
        JoinedInstanceCollection,
    )
    from geospatialvideo.instance import Instance


@dataclass
class InstanceCollection:
    instances: list["Instance"]

    def crossproduct(self, *others: tuple["InstanceCollection"]) -> "JoinedInstanceCollection":
        pass

    def filter(self, predicate: Callable[["Instance"], bool]) -> "InstanceCollection":
        pass

    def overlay() -> None:
        pass
