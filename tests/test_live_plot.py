#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Unit tests for the overall app."""

import unittest

from matplotlive import LivePlot


class TestLivePlot(unittest.IsolatedAsyncioTestCase):
    """Tests the base LivePlot class."""

    def test_init(self):
        live_plot = LivePlot(
            xlim=(0.0, 12.0),
            ylim=(-0.5, 1.0),
            ylim_rhs=(-1.0, 1.0),
            faster=False,
        )
        live_plot.add_line("lhs", "b-")
        live_plot.axis.set_ylabel("LHS axis label", color="b")
        live_plot.axis.tick_params(axis="y", labelcolor="b")
        live_plot.add_rhs_line("rhs", "g-")
        self.assertIsNotNone(live_plot.rhs_axis)
        live_plot.rhs_axis.set_ylabel("RHS axis label", color="g")
        live_plot.rhs_axis.tick_params(axis="y", labelcolor="g")
        live_plot.add_line("lhs_cur", "bo", lw=2)
        live_plot.add_line("lhs_goal", "b--", lw=1)
        live_plot.add_rhs_line("rhs_goal", "g--", lw=1)
        live_plot.add_rhs_line("rhs_cur", "go", lw=2)
