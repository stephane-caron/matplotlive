#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import time

import numpy as np

from matplotlive import Sketch

t_min = 0.0
t_max = 10.0
nb_knots = 12
trange = np.linspace(t_min, t_max, nb_knots)

sketch = Sketch(
    xlim=(t_min, t_max),
    ylim=(-1.5, 1.5),
    ylim_right=(-3.5, 3.5),
)

sketch.add_line("sine", "left", "b-")
sketch.left_axis.set_ylabel("sin(t)", color="b")
sketch.left_axis.tick_params(axis="y", labelcolor="b")

sketch.add_line("cosine", "right", "g-")
sketch.right_axis.set_ylabel("3 cos(t)", color="g")
sketch.right_axis.tick_params(axis="y", labelcolor="g")

sketch.redraw()  # update axis labels

dt = 1e-2
for i in range(100):
    t = i * dt
    sketch.update_line("sine", trange, np.sin(trange + t))
    sketch.update_line("cosine", trange, 3 * np.cos(trange + t))
    sketch.update()
    time.sleep(dt)
