import cadquery as cq
from typing import Callable
from enum import Enum, auto

class FlangeType(Enum):
    EDGE = auto()
    INSIDE= auto()
    OUTSIDE= auto()

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
    distance: float = 10,
    angle: float = 90,
    radius: float = None,
    flip: bool = False,

    offset_a: float = None,
    offset_b: float = None,

    relief_type: FlangeType = FlangeType.EDGE,
    relief_width: float = None,
    relief_depth: float = None,
    relief_remnant: float = None,

) -> cq.Workplane:

    def _flange_callback(face):
        nonlocal radius,relief_width,relief_depth,relief_remnant
        face_wp = cq.Workplane(face)
        long_edge = edge_selector(face_wp).first()
        long_edge_axis = long_edge.val().endPoint() - long_edge.val().startPoint()

        # Calculate thickness
        short_edge = face_wp.edges(
            cq.selectors.PerpendicularDirSelector(long_edge_axis)
        ).first()
        thickness = short_edge.val().Length()

        center = face.Center()
        zaxis = -face.normalAt()

        # calculate the vector from the center of face to long_edge and use that to calculate xaxis
        long_edge_mid = cq.Vector(
            (long_edge.val().startPoint().x + long_edge.val().endPoint().x) / 2.0,
            (long_edge.val().startPoint().y + long_edge.val().endPoint().y) / 2.0,
            (long_edge.val().startPoint().z + long_edge.val().endPoint().z) / 2.0,
        )
        xaxis = (long_edge_mid).cross(face.normalAt())

        if flip:
            xaxis = -xaxis

        if radius is None:
            radius = thickness

        if relief_width is None:
            relief_width = thickness

        if relief_depth is None:
            relief_depth = thickness * 0.5
        
        if relief_remnant is None:
            relief_remnant = thickness * 2.0

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
if 'show_object' in locals():
    result = cq.Workplane("XY").box(10, 10, 1)
    result = result.flange(lambda wp: wp.faces("|Y"), lambda wp: wp.edges(">Z"), distance=3)
#if __name__ == "__main__":
#    result = cq.Workplane("XY").box(10, 10, 1)
#    result = result.flange(lambda wp: wp.faces("|Y"), lambda wp: wp.edges(">Z"), 90, 1, 5)
#    show_object(result)