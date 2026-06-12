#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Frequency-domain induced-polarization (FDIP) Data Manager.

FDIP field data handling, modelling and inversion."""

from .fdip import FDIP
from .fdipmodelling import (DCIPMModelling,
                           ERTTLmod,
                           ERTMultiPhimod,
                           )
