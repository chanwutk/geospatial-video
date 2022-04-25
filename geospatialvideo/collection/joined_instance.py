from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from geospatialvideo.collection.instance import InstanceCollection
    from geospatialvideo.instance import Instance


class JoinPredicate(Protocol):
      def __call__(self, *args: "Instance") -> bool: ...


@dataclass
class JoinedInstanceCollection:
    joined_instances: list[tuple["Instance"]]

    def join(self, *others: tuple["InstanceCollection"]) -> "JoinedInstanceCollection":
        pass

    def filter(self, predicate: JoinPredicate) -> "JoinedInstanceCollection":
        pass

    def overlay() -> None:
        pass
