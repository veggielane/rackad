import cadquery as cq
from enum import Enum


class RackSize(Enum):
    NINETEEN = 19
    TEN_PNT_FIVE = 10.5
    TEN = 10
    NINE_PNT_FIVE = 9.5

panel_thickness = 2
panel_fillet = 2

def panel_height(u):
    return round(44.45 * u - 0.794, 1)


def panel_width(size: RackSize):
    return round(size.value * 25.4, 1)
