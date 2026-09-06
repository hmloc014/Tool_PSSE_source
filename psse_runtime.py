# -*- coding: utf-8 -*-
"""Small compatibility helpers for the legacy PSS/E 33 runtime."""

import ctypes


def safe_psseinit(psspy, bus_count):
    """Initialize PSS/E after clearing pending Windows floating-point flags."""
    try:
        # lxml.etree can leave a sticky flag that crashes PSS/E 33's libmmd.
        ctypes.cdll.msvcrt._clearfp()
    except Exception:
        # Non-Windows/source-analysis environments do not expose msvcrt.
        pass
    return psspy.psseinit(bus_count)
