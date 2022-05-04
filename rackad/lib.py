import cadquery as cq
from enum import Enum


class RackSize(Enum):
    NINETEEN = 19
    TEN_PNT_FIVE = 10.5
    TEN = 10
    NINE_PNT_FIVE = 9.5


panel_thickness = 2
panel_fillet = 2


def panel_height(u: int):
    return round(44.45 * u - 0.794, 1)


def panel_width(size: RackSize):
    return round(size.value * 25.4, 1)

def panel_hole_centre(size: RackSize) -> float:
    if size == RackSize.NINETEEN:
        return 465.12
    elif size == RackSize.TEN_PNT_FIVE:
        return 254
    elif size == RackSize.TEN:
        return 236.525
    elif size == RackSize.NINE_PNT_FIVE:
        return 223

def panel_hole_pitch(u: int) -> float:
   # match u:
    #    case 1:
    return 1.25*25.4