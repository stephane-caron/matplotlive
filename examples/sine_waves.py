#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Draw sine waves using a live plot."""

import math

from matplotlive import LivePlot

OMEGA = 20.0  # Hz
TIMESTEP = 1e-2  # [s]

plot = LivePlot(
    timestep=TIMESTEP,
    duration=1.0,
    ylim=(-1.5, 1.5),
    ylim_right=(-3.5, 3.5),
)

plot.add_left("sin", "b-")
plot.left_axis.set_ylabel(r"$\sin(\omega t)$", color="b")
plot.left_axis.tick_params(axis="y", labelcolor="b")

plot.add_right("3 cos", "g-")
plot.add_right("1.5 cos", "g:")
plot.right_axis.set_ylabel(r"Cosines", color="g")
plot.right_axis.tick_params(axis="y", labelcolor="g")

plot.legend()
plot.redraw()

for i in range(500):
    t = i * TIMESTEP
    plot.send("sin", math.sin(OMEGA * t))
    plot.send("3 cos", 3 * math.cos(OMEGA * t))
    plot.send("1.5 cos", 1.5 * math.cos(OMEGA * t))
    plot.update()
