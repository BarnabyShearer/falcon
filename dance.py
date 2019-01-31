#!/usr/bin/env python3.7
"""
Demo position control.
"""

import math
import time

import numpy as np
from falcon import falcon, vec, xyz
from pid import PID

STIFFNESS = 1000
SPEED = 3.0

def main():
    pids = np.array((PID(), PID(), PID()))
    start = time.time()

    for f in falcon():
        t = (time.time() - start) / SPEED % 1
        target = np.array((
            math.sin(math.pi * t * 2) * .03,
            math.cos(math.pi * t * 2) * .03,
            .125 + (math.sin(math.pi * t * 4) * .03)
        ))
        f.setForces(vec(map(
            lambda x: x[0].update(x[1]) * STIFFNESS,
            zip(
                pids,
                np.array(xyz(f.getPosition())) - target
            )
        )))

if __name__ == "__main__":
    main()
