import cadquery as cq

result = cq.Workplane("XY" ).box(3, 3, 0.5).edges("|Z").fillet(0.125)

result.val().exportStep("output/box.step")
cq.exporters.export(result, 'output/box.stl')