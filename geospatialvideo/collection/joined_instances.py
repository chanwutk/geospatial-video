from __future__ import annotations
from dataclasses import dataclass
from enum import auto, Enum
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from geospatialvideo.collection.instances import Instances
    from geospatialvideo.instance import Instance


@dataclass
class JoinedInstances:
    joined_instances: list[tuple["Instance"]]

    def join(self, *others: tuple["Instances"]) -> "JoinedInstances":
        pass

    def filter(self, predicate: Callable[["Instance"], bool]) -> "JoinedInstances":
        pass

    def overlay() -> None:
        pass
