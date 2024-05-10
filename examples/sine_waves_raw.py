#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Draw sine waves using a raw Sketch rather than a RecentPast plot."""

import numpy as np

from matplotlive import Sketch

OMEGA = 20.0  # Hz
TIMESTEP = 1e-2  # s
NB_STEPS = 100

trange = np.linspace(0.0, NB_STEPS * TIMESTEP, NB_STEPS)
sketch = Sketch(
    xlim=(trange[0], trange[-1]),
    ylim=(-1.5, 1.5),
    ylim_right=(-3.5, 3.5),
)

sketch.add_line("sine", "left", "b-")
sketch.left_axis.set_ylabel(r"$\sin(\omega t)$", color="b")
sketch.left_axis.tick_params(axis="y", labelcolor="b")

sketch.add_line("cosine", "right", "g-")
sketch.right_axis.set_ylabel(r"$3 \cos(\omega t)$", color="g")
sketch.right_axis.tick_params(axis="y", labelcolor="g")

sketch.redraw()  # update axis labels

for i in range(500):
    t = i * TIMESTEP
    sketch.update_line("sine", trange, np.sin(OMEGA * (trange + t)))
    sketch.update_line("cosine", trange, 3 * np.cos(OMEGA * (trange + t)))
    sketch.update()
