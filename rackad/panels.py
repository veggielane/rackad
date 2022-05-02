import cadquery as cq
from rackad.lib import (
    RackSize,
    panel_height,
    panel_width,
    panel_thickness,
    panel_fillet,
)
from rackad.part import Part
import rackad.sheet

class PanelFlat(Part):
    def __init__(self, width: RackSize, u: int):
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
            .flange(lambda wp: wp.faces("|Y"), lambda wp: wp.edges(">Z"), 90, 1, 5)
            
        )


FLAT_1U19 = PanelFlat(RackSize.NINETEEN, 1)
FLAT_2U19 = PanelFlat(RackSize.NINETEEN, 2)
FLAT_1U10 = PanelFlat(RackSize.TEN, 1)
FLAT_2U10 = PanelFlat(RackSize.TEN, 2)

FORMED_1U19 = PanelFormed(RackSize.NINETEEN, 1)
FORMED_2U19 = PanelFormed(RackSize.NINETEEN, 2)
FORMED_1U10 = PanelFormed(RackSize.TEN, 1)
FORMED_2U10 = PanelFormed(RackSize.TEN, 2)

if __name__ == "__main__":
    print(__name__)
