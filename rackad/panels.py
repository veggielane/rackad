import cadquery as cq
from rackad.lib import Part

class Blank(Part):
    def __init__(self, u:int):
        super(Part, self).__init__(f'PANEL-19-{u}U-BLANK', f'BLANK PANEL {u}U')

    def build(self):
        return (cq.Workplane('XY')
        .box(3, 3, 0.5)
        .edges("|Z")
        .fillet(0.125)
        )