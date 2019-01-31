#!/usr/bin/env python3.7
"""
Render a cube which feels sticky.
"""

import numpy as np
from falcon import falcon, vec, xyz

STIFFNESS = 1000
CUBE = np.array([
    [-.030, -.030, .095],
    [.030, .030, .155]
])

def main():
    entry = None
    for f in falcon():
        p = np.array(xyz(f.getPosition()))
        if (CUBE[0] < p).all() and (CUBE[1] > p).all():
            f.setForces(vec(STIFFNESS * (entry - p)))
        else:
            entry = p
            f.setForces(vec([0, 0, 0]))

if __name__ == "__main__":
    main()
