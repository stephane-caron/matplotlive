#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Updatable plot using matplotlib."""

from typing import Any, Dict, Optional, Sequence, Tuple

import matplotlib
from matplotlib import pyplot as plt

from .exceptions import MatplotliveError


class Sketch:
    """Updatable plot using matplotlib."""

    lines: Dict[str, Any]

    def __init__(
        self,
        xlim: Tuple[float, float],
        ylim: Tuple[float, float],
        ylim_right: Optional[Tuple[float, float]] = None,
        faster: bool = True,
    ):
        """Initialize sketch plot.

        Args:
            xlim: Limits for the x-axis.
            ylim: Limits for left-hand side y-axis.
            ylim_right: If set, create a right y-axis with these limits.
            faster: If set, use blitting.
        """
        if faster:  # blitting doesn't work with all matplotlib backends
            matplotlib.use("TkAgg")
        figure, left_axis = plt.subplots()
        left_axis.set_xlim(*xlim)
        left_axis.set_ylim(*ylim)
        right_axis = None
        if ylim_right is not None:
            right_axis = left_axis.twinx()
            right_axis.set_ylim(*ylim_right)
        plt.show(block=False)
        plt.pause(0.05)
        self.background = None
        self.canvas = figure.canvas
        self.canvas.mpl_connect("draw_event", self.__on_draw)
        self.faster = faster
        self.figure = figure
        self.left_axis = left_axis
        self.lines = {}
        self.right_axis = right_axis

    def redraw(self) -> None:
        """Redraw the entire plot (e.g. after updating axis labels)."""
        plt.show(block=False)

    def reset(self) -> None:
        """Reset the sketch."""
        for line in self.lines.values():
            line.remove()
        self.lines = {}
        self.update()

    def add_line(self, name: str, side: str, *args, **kwargs) -> None:
        """Add a line-plot to the left axis.

        Args:
            name: Name to refer to this line, for updates.
            side: Axis to which the line is attached, "left" or "right".
            args: Forwarded to ``pyplot.plot``.
            kwargs: Forwarded to ``pyplot.plot``.
        """
        axis = self.left_axis if side == "left" else self.right_axis
        if axis is None:
            raise MatplotliveError(f"{side}-hand side axis not initialized")
        kwargs["animated"] = True
        (line,) = axis.plot([], *args, **kwargs)
        self.lines[name] = line

    def legend(self, legend: Sequence[str]) -> None:
        """Add a legend to the plot.

        Args:
            legend: Legend.
        """
        self.left_axis.legend(legend)

    def update_line(self, name: str, xdata, ydata) -> None:
        """Update a previously-added line.

        Args:
            name: Name of the line to update.
            xdata: New x-axis data.
            ydata: New y-axis data.
        """
        self.lines[name].set_data(xdata, ydata)

    def __draw_lines(self) -> None:
        for line in self.lines.values():
            self.figure.draw_artist(line)

    def __on_draw(self, event) -> None:
        if event is not None:
            if event.canvas != self.canvas:
                raise RuntimeError
        self.background = self.canvas.copy_from_bbox(self.figure.bbox)
        self.__draw_lines()

    def update(self) -> None:
        """Update the output figure."""
        if self.background is None:
            self.__on_draw(None)
        elif self.faster:
            self.canvas.restore_region(self.background)
            self.__draw_lines()
            self.canvas.blit(self.figure.bbox)
        else:  # slow mode, if blitting doesn't work
            self.canvas.draw()
        self.canvas.flush_events()
