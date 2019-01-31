#!/usr/bin/env python3.7
"""
`mouse.py` and pixel under cursor's color sets Z force.
"""

import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
from gi.repository import GdkPixbuf

import mouse
from falcon import vec

def callback(f, xx, yy):
    f.setForces(vec([
        0,
        0,
        sum(Gdk.pixbuf_get_from_window(
            Gdk.get_default_root_window(),
            xx,
            yy,
            1,
            1
        ).get_pixels()) / 500 + 1
    ]))

if __name__ == "__main__":
    mouse.main(callback)
