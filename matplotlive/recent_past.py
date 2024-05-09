#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Live plot to which time series data is streamed."""

from typing import Optional, Tuple

from .sketch import Sketch


class RecentPast:
    """Live plot to which time series data is streamed."""

    sketch: Sketch

    def __init__(
        self,
        duration: float,
        ylim: Tuple[float, float],
        ylim_right: Optional[Tuple[float, float]] = None,
        faster: bool = True,
    ):
        """Initialize a new figure.

        Args:
            duration: Duration of the recent-past sliding window, in seconds.
            ylim: Limits for left y-axis.
            ylim_right: If set, create a right y-axis with these limits.
            faster: If set, use blitting.
        """
        xlim = (-abs(duration), 0.0)
        self.sketch = Sketch(xlim, ylim, ylim_right, faster)

    def add_left(self, name: str, *args, **kwargs) -> None:
        """Add a new time series to the left axis.

        Args:
            name: Name of the time series.
            args: Forwarded to ``pyplot.plot``.
            kwargs: Forwarded to ``pyplot.plot``.
        """
        self.sketch.add_line(name, "left", *args, **kwargs)

    def add_right(self, name: str, *args, **kwargs) -> None:
        """Add a new time series to the right axis.

        Args:
            name: Name of the time series.
            args: Forwarded to ``pyplot.plot``.
            kwargs: Forwarded to ``pyplot.plot``.
        """
        self.sketch.add_line(name, "right", *args, **kwargs)

    def send(self, name: str, value: float) -> None:
        """Send a new value for a given time series.

        Args:
            name: Name of the time series.
            value: New value for the series.
        """
        pass
