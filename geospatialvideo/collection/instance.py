from __future__ import annotations

from dataclasses import dataclass
import itertools
from typing import TYPE_CHECKING, Callable, List, Tuple

from geospatialvideo.collection.joined_instance import JoinedInstanceCollection

if TYPE_CHECKING:
    from geospatialvideo.instance import Instance


@dataclass
class InstanceCollection:
    instances: List["Instance"]

    def crossproduct(
        self, *others: "InstanceCollection", on: str = "frame"
    ) -> "JoinedInstanceCollection":
        def properties_match(tup: Tuple["Instance", ...]):
            first_prop = tup[0].property[on]
            for i in tup[1:]:
                if i.property[on] != first_prop:
                    return False
            return True

        return JoinedInstanceCollection([
            p for p in itertools.product(self.instances, *[o.instances for o in others])
            if properties_match(p)
        ])

    def filter(self, predicate: Callable[["Instance"], bool]) -> "InstanceCollection":
        return InstanceCollection([i for i in self.instances if predicate(i)])

    def overlay(self) -> None:
        pass
