#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import time

import numpy as np
from loop_rate_limiters import RateLimiter

from matplotlive import RecentPast

t_min = 0.0
t_max = 10.0
nb_knots = 12
trange = np.linspace(t_min, t_max, nb_knots)

dt = 1e-2  # [s]
plot = RecentPast(
    10.0,
    dt,
    ylim=(-1.5, 1.5),
    ylim_right=(-3.5, 3.5),
)

plot.add_left("sin", "b-")
plot.left_axis.set_ylabel("sin(t)", color="b")
plot.left_axis.tick_params(axis="y", labelcolor="b")

plot.add_right("3cos", "g-")
plot.right_axis.set_ylabel("3 cos(t)", color="g")
plot.right_axis.tick_params(axis="y", labelcolor="g")
plot.redraw()

rate = RateLimiter(frequency=1.0 / dt)
for i in range(1000):
    t = i * dt
    plot.send("sin", np.sin(t))
    plot.send("3cos", 3 * np.cos(t))
    plot.update()
    rate.sleep()
