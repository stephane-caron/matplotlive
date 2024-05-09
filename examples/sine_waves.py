#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Draw sine waves using a RecentPast plot."""

import time

import numpy as np
from loop_rate_limiters import RateLimiter

from matplotlive import RecentPast

omega = 20.0  # Hz
dt = 1e-2  # [s]
plot = RecentPast(
    timestep=dt,
    duration=1.0,
    ylim=(-1.5, 1.5),
    ylim_right=(-3.5, 3.5),
)

plot.add_left("sin", "b-")
plot.left_axis.set_ylabel(r"$\sin(\omega t)$", color="b")
plot.left_axis.tick_params(axis="y", labelcolor="b")

plot.add_right("3cos", "g-")
plot.right_axis.set_ylabel(r"$3 \cos(\omega t)$", color="g")
plot.right_axis.tick_params(axis="y", labelcolor="g")
plot.redraw()

rate = RateLimiter(frequency=1.0 / dt)
for i in range(1000):
    t = i * dt
    plot.send("sin", np.sin(omega * t))
    plot.send("3cos", 3 * np.cos(omega * t))
    plot.update()
    rate.sleep()
