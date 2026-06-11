#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Spectral induced polarization (SIP) MethodManager.

Spectral induced polarization (SIP) data handling, modelling and inversion."""

from .fdip import FDIP
FDIPdata = FDIP
SIPdata = FDIP
from .fdipmodelling import (DCIPMModelling,
                           ERTTLmod,
                           ERTMultiPhimod,
                           )

__all__ = ['FDIP', 'FDIPdata', 'SIPdata']
