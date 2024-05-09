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

    def setUp(self):
        self.live_plot = LivePlot(
            xlim=(0.0, 12.0),
            ylim=(-1.0, 1.0),
            ylim_right=(-10.0, 10.0),
            faster=False,
        )

    def test_left_axis(self):
        plot = LivePlot(
            xlim=(0.0, 12.0),
            ylim=(-1.0, 1.0),
            faster=False,
        )
        self.assertIsNotNone(plot.left_axis)
        self.assertIsNone(plot.right_axis)

    def test_right_axis(self):
        plot = LivePlot(
            xlim=(0.0, 12.0),
            ylim=(-1.0, 1.0),
            ylim_right=(-10.0, 10.0),
            faster=False,
        )
        self.assertIsNotNone(plot.left_axis)
        self.assertIsNotNone(plot.right_axis)
