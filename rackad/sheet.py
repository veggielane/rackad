import cadquery as cq
from typing import Callable
import math


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
        xaxis = long_edge.val().endPoint() - long_edge.val().startPoint()
        short_edge = face_wp.edges(cq.selectors.PerpendicularDirSelector(xaxis)).first()
        thickness = short_edge.val().Length()

        center = face.Center()
        zaxis = -face.normalAt()
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

        flat = (
            bend.faces(
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
            )
            .tag("end")
            .workplane()
            .faces(tag="end")
            .wires()
            .toPending()
            .extrude(distance - thickness - radius)
        )
        return flat.val()

    return wp.union(face_selector(wp).each(_flange_callback))


cq.Workplane.flange = flange

result = cq.Workplane("XY").box(10, 10, 1)
result = result.flange(lambda wp: wp.faces(">Y"), lambda wp: wp.edges(">Z"), 90, 1, 5)
result = result.flange(
    lambda wp: wp.faces("<Y"), lambda wp: wp.edges(">Z"), 90, 1, 5, True
)
