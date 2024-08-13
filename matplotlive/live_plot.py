#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Live plot to which time series data is streamed."""

from typing import Dict, Optional, Tuple

import matplotlib
import numpy as np
from numpy.typing import NDArray

from .exceptions import MatplotliveError
from .sketch import Sketch


class LivePlot:
    """Live plot to which time series data is streamed."""

    sketch: Sketch
    trange: NDArray[np.float64]

    def __init__(
        self,
        timestep: float,
        duration: float,
        ylim: Tuple[float, float],
        ylim_right: Optional[Tuple[float, float]] = None,
        faster: bool = True,
    ):
        """Initialize a new figure.

        Args:
            duration: Duration of the recent-past sliding window, in seconds.
            timestep: Time step between two successive values, in seconds.
            ylim: Limits for left y-axis.
            ylim_right: If set, create a right y-axis with these limits.
            faster: If set, use blitting.
        """
        xlim = (-abs(duration), 0.0)
        trange = np.flip(-np.arange(0.0, duration, timestep))
        sketch = Sketch(xlim, ylim, ylim_right, faster)
        sketch.left_axis.set_xlabel("Time (seconds)")
        self.__legend = {"left": [], "right": []}
        self.__max_updates: int = 0
        self.__nb_updates: Dict[str, int] = {}
        self.__shape = (len(trange),)
        self.series: Dict[str, NDArray[np.float64]] = {}
        self.sketch = sketch
        self.trange = trange

    @property
    def left_axis(self) -> matplotlib.axes.Subplot:
        """Left axis of the plot."""
        return self.sketch.left_axis

    @property
    def right_axis(self) -> Optional[matplotlib.axes.Subplot]:
        """Right axis of the plot."""
        return self.sketch.right_axis

    def legend(self) -> None:
        """Place a legend on the left or right axes that are used."""
        if self.__legend["left"]:
            self.left_axis.legend(self.__legend["left"], loc="upper left")
        if self.__legend["right"]:
            self.right_axis.legend(self.__legend["right"], loc="upper right")

    def redraw(self):
        """Redraw the entire plot (e.g. after updating axis labels)."""
        self.sketch.redraw()

    def reset(self):
        """Clear the plot."""
        self.__max_updates = 0
        self.series = {}
        self.sketch.reset()

    def __add(self, name: str, side: str, *args, **kwargs) -> None:
        self.sketch.add_line(name, side, *args, **kwargs)
        if name in self.series:
            raise MatplotliveError(f"a series named '{name}' already exists")
        self.series[name] = np.full(self.__shape, np.nan)
        self.__nb_updates[name] = 0
        self.__legend[side].append(name)

    def add_left(self, name: str, *args, **kwargs) -> None:
        """Add a new time series to the left axis.

        Args:
            name: Name of the time series.
            args: Positional arguments forwarded to ``pyplot.plot``.
            kwargs: Keyword arguments forwarded to ``pyplot.plot``.
        """
        self.__add(name, "left", *args, **kwargs)

    def add_right(self, name: str, *args, **kwargs) -> None:
        """Add a new time series to the right axis.

        Args:
            name: Name of the time series.
            args: Positional arguments forwarded to ``pyplot.plot``.
            kwargs: Keyword arguments forwarded to ``pyplot.plot``.
        """
        self.__add(name, "right", *args, **kwargs)

    def send(self, name: str, value: float) -> None:
        """Send a new value for a given time series.

        Args:
            name: Name of the time series.
            value: New value for the series.
            args: If adding, positional arguments for ``pyplot.plot``.
            kwargs: If adding, keyword arguments for ``pyplot.plot``.
        """
        if name not in self.series:
            return
        # Deleting and appending is slightly faster than rolling an array of
        # size 20 (mean ± std. dev. of 7 runs, 100,000 loops each):
        #
        #     %timeit np.append(np.delete(a, 0), 11111)
        #     5.69 µs ± 18.5 ns per loop
        #
        #     %timeit np.roll(a, 1)
        #     6.49 µs ± 17.4 ns per loop
        #
        new_series = np.append(np.delete(self.series[name], 0), value)
        self.sketch.update_line(name, self.trange, new_series)
        self.series[name] = new_series
        self.__nb_updates[name] += 1
        self.__max_updates = max(self.__max_updates, self.__nb_updates[name])

    def update(self) -> None:
        """Update plot with latest time-series values.

        Calling this function will catch up all time series with the most
        recent one.
        """
        for name in self.series:
            while self.__nb_updates[name] < self.__max_updates:
                self.send(name, self.series[name][-1])
        self.sketch.update()
