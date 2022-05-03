from rackad.lib import RackSize
import rackad.panels as panel
import rackad.mount as mount
import cadquery as cq
from rackad.builder import output, build
from rackad.sheet import *

parts = [
    panel.FLAT_1U19,
    panel.FLAT_2U19,
    panel.FLAT_1U10,
    panel.FLAT_2U10,
    panel.FORMED_1U10,
    mount.Switch8(),
]


if 'show_object' in locals():
    for key, value in build(parts).items():
        show_object(value, name=key.number)
else:
    output(parts)