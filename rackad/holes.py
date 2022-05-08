import cadquery as cq

def panel_hole(wp: cq.Workplane) -> cq.Workplane:
    def _panel_hole_callback(loc):
        hole = cq.Solid.makeCylinder(10.4 / 2.0, 100, cq.Vector(0, 0, 0), cq.Vector(0, 0, -1))
        
        return hole.move(loc) 

    return wp.cutEach(_panel_hole_callback, True, True)


cq.Workplane.panel_hole = panel_hole

if "show_object" in locals():
    result = cq.Workplane("XY").box(10, 10, 1)
    result = result.flange(lambda wp: wp.faces("|Y"), lambda wp: wp.edges(">Z"), distance=3)
