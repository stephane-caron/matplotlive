#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Stream live plots to a matplotlib figure."""

from .exceptions import MatplotliveError
from .live_plot import LivePlot
from .sketch import Sketch

__version__ = "1.0.0"

__all__ = [
    "MatplotliveError",
    "LivePlot",
    "Sketch",
]
