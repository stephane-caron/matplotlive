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

    def setUp(self):
        self.plot = LivePlot(
            timestep=0.01,
            duration=0.5,
            ylim=(-1.0, 1.0),
        )

    def test_init(self):
        self.assertIsNotNone(self.plot.trange)
        self.assertEqual(len(self.plot.series), 0)

    def test_add(self):
        self.assertEqual(len(self.plot.series), 0)
        self.plot.add_left("foo")
        self.assertEqual(len(self.plot.series), 1)

    def test_uninitialized_right(self):
        with self.assertRaises(MatplotliveError):
            self.plot.add_right("bar")
