import cadquery as cq
result = cq.Workplane("XY").box(40,40, 0.5)



def flange(
    wp: cq.Workplane,
    selector: str,
) -> cq.Workplane:

    def _flange_callback(face):

        

        face_wp = cq.Workplane(face)
        long_edge = face_wp.edges(selector).first()
        
        center = face.Center()
        zaxis = -face.normalAt()
        
        
        
        xaxis = long_edge.val().endPoint() - long_edge.val().startPoint()
        fwp = cq.Workplane(cq.Plane(center, xaxis, zaxis), origin=center, obj=face)
        
        show_object(face_wp)
        
        show_object(long_edge)
        
        show_object(fwp.wires().toPending().revolve(90,(-1,-5,0),(1,-5,0)))

        return face

    return wp.each(_flange_callback)

cq.Workplane.flange = flange

show_object(result)
face = result.faces("<Y").flange(">Z")


#edge = face


#result.flange()