#!/usr/bin/env python3.7
"""
Software PWM control of the RGB LEDs
"""

import math
import numpy as np

from falcon import falcon

FRAMES = 25
SPEED = np.array([0.001, 0.002, 0.003])
def main():
    frame_no = 0
    color = np.array([0.0, 0.0, 0.0])
    for f in falcon():
        f.setLEDStatus(
            int(np.packbits(
                np.append(
                    [0,0,0,0],
                    frame_no < np.array(tuple(map(lambda x: math.sin(x) * 25, color)))
                )
            ))
        )
        frame_no += 1
        frame_no %= FRAMES
        color += SPEED
        color %= math.pi * 2

if __name__ == "__main__":
    main()
