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
        self.assertIsNotNone(plot.left_axis)

    def test_uninitialized_right(self):
        plot = self.make_test_plot()
        self.assertIsNone(plot.right_axis)
        with self.assertRaises(MatplotliveError):
            plot.add_right("bar")

    def test_add_right(self):
        plot = self.make_test_plot(ylim_right=(0.0, 10.0))
        plot.add_right("bar")
        self.assertEqual(len(plot.series), 1)
        self.assertIsNotNone(plot.right_axis)

    def test_add_twice(self):
        plot = self.make_test_plot()
        plot.add_left("foo")
        with self.assertRaises(MatplotliveError):
            plot.add_left("foo")

    def test_send(self):
        plot = self.make_test_plot()
        plot.send("foo", 1.0)
        self.assertTrue("foo" in plot.series)
        plot.send("foo", 2.0)
        plot.send("foo", 3.0)
        self.assertAlmostEqual(plot.series["foo"][-1], 3.0)

    def test_push(self):
        plot = self.make_test_plot()
        plot.push("foo", 1.0)
        self.assertFalse("foo" in plot.series)
        plot.add_left("foo")
        self.assertTrue("foo" in plot.series)
        plot.push("foo", 2.0)
        plot.push("foo", 3.0)
        self.assertAlmostEqual(plot.series["foo"][-1], 3.0)

    def test_update(self):
        plot = self.make_test_plot()
        plot.add_left("foo")
        plot.add_left("bar")
        plot.send("foo", 1.0)
        plot.send("foo", 2.0)
        plot.send("bar", 3.0)
        plot.update()
        self.assertAlmostEqual(plot.series["foo"][-1], 2.0)
        self.assertAlmostEqual(plot.series["bar"][-1], 3.0)
