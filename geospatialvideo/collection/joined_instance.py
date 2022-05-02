from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Protocol, Tuple

if TYPE_CHECKING:
    from geospatialvideo.collection.instance import InstanceCollection
    from geospatialvideo.instance import Instance


class JoinPredicate(Protocol):
    def __call__(self, *args: "Instance") -> bool:
        ...


@dataclass
class JoinedInstanceCollection:
    joined_instances: List[Tuple["Instance", ...]]

    def join(self, *others: "InstanceCollection", on: str = "frame") -> "JoinedInstanceCollection":
        return JoinedInstanceCollection([])

    def filter(self, predicate: JoinPredicate) -> "JoinedInstanceCollection":
        return JoinedInstanceCollection([])

    def overlay(self) -> None:
        pass
