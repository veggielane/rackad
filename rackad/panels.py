import cadquery as cq
from rackad.lib import (
    RackSize,
    panel_height,
    panel_width,
    panel_thickness,
    panel_fillet,
    panel_hole_centre,
    panel_hole_pitch,
    panel_hole_positions
)
from rackad.holes import panel_hole
from rackad.part import Part
from rackad.sheet import *


class PanelFlat(Part):
    def __init__(self, width: RackSize, u: int):
        self.u = u
        self.rack_size = width
        self.width = panel_width(width)
        self.height = panel_height(u)
        super(Part, self).__init__(
            f"{u}U{width.value}-PANEL-FLAT", f'FLAT PANEL {u}U {width.value}"'
        )

    def build(self):
        return (
            cq.Workplane("XY")
            .box(self.width, self.height, panel_thickness)
            .edges("|Z")
            .fillet(panel_fillet)
            .faces(">Z")
            .workplane()
            .pushPoints(panel_hole_positions(self.rack_size, self.u))
            .panel_hole()
        )


class PanelFormed(Part):
    def __init__(self, width: RackSize, u: int):
        self.width = panel_width(width)
        self.height = panel_height(u)
        super(Part, self).__init__(
            f"{u}U{width.value}-PANEL-FORMED", f'FORMED PANEL {u}U {width.value}"'
        )

    def build(self):
        return (
            cq.Workplane("XY")
            .box(self.width, self.height, panel_thickness)
            .flange(lambda wp: wp.faces("|Y"), lambda wp: wp.edges(">Z"), distance=5)
        )


FLAT_1U19 = PanelFlat(RackSize.NINETEEN, 1)
FLAT_2U19 = PanelFlat(RackSize.NINETEEN, 2)
FLAT_1U10 = PanelFlat(RackSize.TEN, 1)
FLAT_2U10 = PanelFlat(RackSize.TEN, 2)
FLAT_3U10 = PanelFlat(RackSize.TEN, 3)
FLAT_4U10 = PanelFlat(RackSize.TEN, 4)
FORMED_1U19 = PanelFormed(RackSize.NINETEEN, 1)
FORMED_2U19 = PanelFormed(RackSize.NINETEEN, 2)
FORMED_1U10 = PanelFormed(RackSize.TEN, 1)
FORMED_2U10 = PanelFormed(RackSize.TEN, 2)

if __name__ == "__main__":
    print(__name__)
