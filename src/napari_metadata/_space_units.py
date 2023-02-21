from enum import Enum, auto
from typing import List, Optional


class SpaceUnits(Enum):
    """Supported units for a spatial axis."""

    NONE = auto()
    NANOMETERS = auto()
    MICROMETERS = auto()
    MILLIMETERS = auto()
    CENTIMETERS = auto()
    METERS = auto()

    def __str__(self) -> str:
        return self.name.lower()

    @classmethod
    def from_name(cls, name: str) -> Optional["SpaceUnits"]:
        for m in cls:
            if str(m) == name:
                return m
        return None

    @classmethod
    def names(cls) -> List[str]:
        return [str(m) for m in cls]
