#!/usr/bin/env python3.7
"""
Print the Falcon's position and button status.
"""

import math
import time

from falcon import buttons, falcon, homing, xyz

def main():
    for f in falcon():
        print('{0[0]:+.5f} {0[1]:+.5f} {0[2]:+.5f} : {1:04b} : {2}'.format(
            xyz(f.getPosition()),
            buttons(f),
            'not homed' if homing(f) else 'homed'
        ))

if __name__ == "__main__":
    main()
