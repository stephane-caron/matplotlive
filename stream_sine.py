#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import time

import numpy as np

from matplotlive import LivePlot

t_min = 0.0
t_max = 10.0
nb_knots = 12
trange = np.linspace(t_min, t_max, nb_knots)

live_plot = LivePlot(
    xlim=(t_min, t_max),
    ylim=(-1.5, 1.5),
    ylim_rhs=(-3.5, 3.5),
)

live_plot.add_left_axis_line("sine", "b-")
live_plot.left_axis.set_ylabel("sin(t)", color="b")
live_plot.left_axis.tick_params(axis="y", labelcolor="b")

live_plot.add_right_axis_line("cosine", "g-")
live_plot.right_axis.set_ylabel("3 cos(t)", color="g")
live_plot.right_axis.tick_params(axis="y", labelcolor="g")

dt = 1e-2
for i in range(100):
    t = i * dt
    live_plot.update_line("sine", trange, np.sin(trange + t))
    live_plot.update_line("cosine", trange, 3 * np.cos(trange + t))
    live_plot.update()
    time.sleep(dt)
