#!/usr/bin/env python3.7
"""
Render a hard cube you can feel.
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
        force = np.array([0.0, 0.0, 0.0])
        p = np.array(xyz(f.getPosition()))
        if (CUBE[0] < p).all() and (CUBE[1] > p).all():
            closest_edge, dist = min(enumerate(np.append(CUBE[0] - p, CUBE[1] - p)), key=lambda x: abs(x[1]))
            force[closest_edge % 3] = dist
        f.setForces(vec(STIFFNESS * force))

if __name__ == "__main__":
    main()
