from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from geospatialvideo.collection.joined_instances import (
        JoinedInstances,
    )
    from geospatialvideo.instance import Instance


@dataclass
class Instances:
    instances: list["Instance"]

    def crossproduct(self, *others: tuple["Instances"]) -> "JoinedInstances":
        pass

    def filter(self, predicate: Callable[["Instance"], bool]) -> "Instances":
        pass

    def overlay() -> None:
        pass
