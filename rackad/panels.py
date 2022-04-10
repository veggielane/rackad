import cadquery as cq
from rackad.lib import RackSize, panel_height, panel_width
from rackad.part import Part


class Blank(Part):
    def __init__(self, width: RackSize, u: int):
        self.width = panel_width(width)
        self.height = panel_height(u)
        print(self.width)
        print(self.height)
        super(Part, self).__init__(
            f"PANEL-{u}U{width.value}-BLANK", f"{width.value} BLANK PANEL {u}U"
        )

    def build(self):
        return cq.Workplane("XY").box(3, 3, 0.5).edges("|Z").fillet(0.125)
