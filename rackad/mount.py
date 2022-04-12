import cadquery as cq
from rackad.lib import RackSize, panel_height, panel_width
from rackad.part import Part


class Switch8(Part):
    def __init__(self):
        super(Part, self).__init__(f"MOUNT-SWITCH8-10", f"SWITCH 8 MOUNT")

    def build(self):
        base = (
            cq.Workplane("XY")
            .rect(15, 70)
            .extrude(-15)
            .faces(">Z")
            .workplane()
            .rect(15, 50)
            .extrude(-45)
        )

        spacing = (0.625 + 0.5) * 25.4
        base = base.pushPoints([(0, spacing), (0, -spacing)]).circle(3).cutThruAll()

        pts = [(0, 21), (7.5, 21), (7.5, -21), (0, -21)]
        base = base.faces(">Z").workplane(offset=-2).polyline(pts).close().cutBlind(-50)

        base = (
            base.faces("<X")
            .workplane(origin=(0, 0, -25))
            .rect(25, 25, forConstruction=True)
            .vertices()
            .cskHole(4, 8, 90)
        )
        return base
