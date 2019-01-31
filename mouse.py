#!/usr/bin/env python3.7
"""
Falcon's X,Y controls absolute cursor position.

 + Left click
 🌀 Middle click
 ⚡ Right click
 ▶ Exit
"""

import atexit
import time

from pymouse import PyMouse

from falcon import buttons, falcon, xyz

def main(callback=None):
    m = PyMouse()
    def exit_handler():
        for button in range(3):
            m.release(0, 0, button + 1)
    atexit.register(exit_handler)
    width, height = m.screen_size()
    width /= 2
    height /= 2
    old_buttons = 0
    for f in falcon():
        x, y, z = xyz(f.getPosition())
        new_buttons = buttons(f)
        xx = int(width + x * width // 0.03)
        yy = int(height - y * height // 0.03)
        m.move(xx, yy)
        if callback:
            callback(f, xx, yy)
        for button in range(3):
            if new_buttons & 1 << button and not old_buttons & 1 << button:
                m.press(xx, yy, button + 1)
            if not new_buttons & 1 << button and old_buttons & 1 << button:
                m.release(xx, yy, button + 1)
        if new_buttons & 1<<3:
            print("▶ pressed; exiting")
            break
        old_buttons = new_buttons
        time.sleep(1/60)

if __name__ == "__main__":
    main()
