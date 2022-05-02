import cadquery as cq
from typing import Callable


def extrude_face(wp: cq.Workplane, distance: float) -> cq.Workplane:
    def _extrude_face_callback(f: cq.Face):

        return (
            cq.Workplane(
                cq.Plane(
                    f.Center(),
                    f.normalAt()
                    .add(
                        cq.Vector(
                            f.normalAt().x + 1, f.normalAt().y + 1, f.normalAt().z + 1
                        )
                    )
                    .cross(f.normalAt()),
                    f.normalAt(),
                ),
                origin=f.Center(),
                obj=f,
            )
            .wires()
            .toPending()
            .extrude(distance)
            .val()
        )

    return wp.union(wp.each(_extrude_face_callback))


cq.Workplane.extrude_face = extrude_face


def flange(
    wp: cq.Workplane,
    face_selector: Callable[[cq.Workplane], cq.Workplane],
    edge_selector: Callable[[cq.Workplane], cq.Workplane],
    angle: float,
    radius: float,
    distance: float,
    flip: bool = False,
) -> cq.Workplane:
    def _flange_callback(face):
        face_wp = cq.Workplane(face)
        long_edge = edge_selector(face_wp).first()
        long_edge_axis = long_edge.val().endPoint() - long_edge.val().startPoint()
        
        #Calculate thickness
        short_edge = face_wp.edges(cq.selectors.PerpendicularDirSelector(long_edge_axis)).first()
        thickness = short_edge.val().Length()

        center = face.Center()
        zaxis = -face.normalAt()

        a = long_edge.val().startPoint()
        b = long_edge.val().endPoint()
        long_edge_mid = cq.Vector((a.x+b.x)/2.0,(a.y+b.y)/2.0,(a.z+b.z)/2.0)
        log(center - long_edge_mid)

        xaxis = (long_edge_mid).cross(face.normalAt())
        
        if flip:
            xaxis = -xaxis
        
        bend = (
            cq.Workplane(cq.Plane(center, xaxis, zaxis), origin=center, obj=face)
            .wires()
            .toPending()
            .revolve(
                angle,
                (-1, radius + thickness / 2.0, 0),
                (1, radius + thickness / 2.0, 0),
            )
        )

        flat = bend.faces(
            cq.selectors.AndSelector(
                cq.selectors.AndSelector(
                    cq.selectors.InverseSelector(
                        cq.selectors.ParallelDirSelector(xaxis)
                    ),
                    cq.selectors.InverseSelector(
                        cq.selectors.ParallelDirSelector(zaxis)
                    ),
                ),
                cq.selectors.TypeSelector("PLANE"),
            )
        ).extrude_face(distance - thickness - radius)
        return flat.val()

    return wp.union(face_selector(wp).each(_flange_callback))


cq.Workplane.flange = flange

result = cq.Workplane("XY").box(10, 10, 1)

result = result.flange(lambda wp: wp.faces("|Y"), lambda wp: wp.edges(">Z"), 90, 1, 5)
show_object(result)
# result = result.flange(
#    lambda wp: wp.faces("<Y"), lambda wp: wp.edges(">Z"), 90, 1, 5, True
# )
