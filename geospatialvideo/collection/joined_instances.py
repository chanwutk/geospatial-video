from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, Protocol

from mypy_extensions import VarArg

if TYPE_CHECKING:
    from geospatialvideo.collection.instances import Instances
    from geospatialvideo.instance import Instance


class JoinPredicate(Protocol):
      def __call__(self, *args: "Instance") -> bool: ...


@dataclass
class JoinedInstances:
    joined_instances: list[tuple["Instance"]]

    def join(self, *others: tuple["Instances"]) -> "JoinedInstances":
        pass

    def filter(self, predicate: JoinPredicate) -> "JoinedInstances":
        pass

    def overlay() -> None:
        pass
