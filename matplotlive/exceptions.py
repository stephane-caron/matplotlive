#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""
Exceptions from matplotlive.

We catch all solver exceptions and re-throw them in a library-owned exception
to avoid abstraction leakage. See this `design decision
<https://github.com/getparthenon/parthenon/wiki/Design-Decision:-Throw-Custom-Exceptions>`__
for more details on the rationale behind this choice.
"""


class MatplotliveError(Exception):
    """Base class for matplotlive exceptions."""
