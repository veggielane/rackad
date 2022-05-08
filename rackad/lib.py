import cadquery as cq
from enum import Enum
from typing import Iterable

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
        return 465
    elif size == RackSize.TEN_PNT_FIVE:
        return 249
    elif size == RackSize.TEN:
        return 236.5
    elif size == RackSize.NINE_PNT_FIVE:
        return 224

def panel_hole_pitch(u: int) -> float:
   # match u:
    #    case 1:
    return 1.25*25.4

def panel_hole_positions(size: RackSize, u: int):

    positions = []



    offset = 0
    if u % 2 == 0:
        offset += (0.25+0.625)*25.4
        offset += (u-1) * 1.75 * 25.4
    else:
        offset += (u-1) * 1.75 * 25.4

    y = panel_hole_pitch(u)
    x = panel_hole_centre(size)

    for _ in range(u):
        positions.extend([(x/2.0, y/2.0+offset), (x/2.0, -y/2.0+offset), (-x/2.0, -y/2.0+offset), (-x/2.0, y/2.0+offset), (-x/2.0, 0+offset), (+x/2.0, 0+offset)])
        offset -=  1.75 * 25.4
    return positions
   # match u:
    #    case 1:
    #return 1.25*25.4