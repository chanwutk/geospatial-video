from __future__ import annotations

from dataclasses import dataclass
import itertools
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
    on_key: str

    def join(self, *others: "InstanceCollection") -> "JoinedInstanceCollection":
        def properties_match(tup: Tuple["Instance", ...]):
            first_prop = tup[0].property[self.on_key]
            for i in tup[1:]:
                if i.property[self.on_key] != first_prop:
                    return False
            return True

        return JoinedInstanceCollection([
            (*j, *p)
            for p in itertools.product(*[o.instances for o in others])
            for j in self.joined_instances
            if p[0].property[self.on_key] == j[0].property[self.on_key] and properties_match(p)
        ], self.on_key)

    def filter(self, predicate: JoinPredicate) -> "JoinedInstanceCollection":
        return JoinedInstanceCollection([i for i in self.joined_instances if predicate(*i)], self.on_key)

    def overlay(self) -> None:
        pass
