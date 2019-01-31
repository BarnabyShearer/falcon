#!/usr/bin/env python3.7
"""
Python friendlyness Helpers
"""

import time
import pynifalcon

FIRMWARE = 0x1
KINEMATIC = 0x2
GRIP = 0x4

def falcon(index=0):
    """
    Generator with yeilds each frame of the loop
    """
    falcon = pynifalcon.FalconDeviceBridge()
    if falcon.getCount() is 0:
        raise Exception("No devices attached")
    if not falcon.open(index):
        raise Exception("Cannot open device")
    if not falcon.loadFirmware():
        time.sleep(1)
        if not falcon.loadFirmware():
            time.sleep(1)
            if not falcon.loadFirmware():
                raise Exception("Cannot load firmware")
    while True:
        if falcon.runIOLoop(FIRMWARE | KINEMATIC):
            yield falcon


def raw(f):
    """SWIG incorrectly parses binary as a python string"""
    return f.getRawOutput().encode('unicode_internal')[4:-4:4]


def homing(f):
    """
    Check if we need homing.
    n.b. atm you have to run one of the libnifalcon examples to home
    """
    return ((raw(f)[-2] - 0x41) >> 4) & 7 != 7


def buttons(f):
    """Return the button bitfield"""
    return (raw(f)[-2] - 0x41) & 0x0f


def xyz(v):
    """Unwrap vector"""
    return (v.x, v.y, v.z)


def vec(v):
    """Wrap vector"""
    tmp = pynifalcon.FalconVec3d()
    tmp.x, tmp.y, tmp.z = v
    return tmp
