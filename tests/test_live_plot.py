#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Unit tests for the LivePlot class."""

import unittest

from matplotlive import LivePlot, MatplotliveError


class TestLivePlot(unittest.TestCase):
    """Test live plots."""

    def make_test_plot(self, *args, **kwargs):
        return LivePlot(
            timestep=0.01,
            duration=0.5,
            ylim=(-1.0, 1.0),
            faster=False,
            *args,
            **kwargs
        )

    def test_init(self):
        plot = self.make_test_plot()
        self.assertIsNotNone(plot.trange)
        self.assertEqual(len(plot.series), 0)

    def test_add(self):
        plot = self.make_test_plot()
        self.assertEqual(len(plot.series), 0)
        plot.add_left("foo")
        self.assertEqual(len(plot.series), 1)

    def test_uninitialized_right(self):
        plot = self.make_test_plot()
        with self.assertRaises(MatplotliveError):
            plot.add_right("bar")

    def test_add_right(self):
        plot = self.make_test_plot(ylim_right=(0.0, 10.0))
        plot.add_right("bar")
        self.assertEqual(len(plot.series), 1)
