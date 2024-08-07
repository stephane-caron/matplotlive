# matplotlive

[![Build](https://img.shields.io/github/actions/workflow/status/stephane-caron/matplotlive/ci.yml?branch=main)](https://github.com/stephane-caron/matplotlive/actions)
[![Coverage](https://coveralls.io/repos/github/stephane-caron/matplotlive/badge.svg?branch=main)](https://coveralls.io/github/stephane-caron/matplotlive?branch=main)
[![Conda version](https://img.shields.io/conda/vn/conda-forge/matplotlive.svg)](https://anaconda.org/conda-forge/matplotlive)
[![PyPI version](https://img.shields.io/pypi/v/matplotlive)](https://pypi.org/project/matplotlive/)

Stream live plots to a [Matplotlib](https://matplotlib.org/) figure.

## Example

```py
import math
import matplotlive

plot = matplotlive.LivePlot(
    timestep=0.01,  # seconds
    duration=1.0,   # seconds
    ylim=(-5.0, 5.0),
)

for i in range(10_000):
    plot.send("bar", math.sin(0.3 * i))
    plot.send("foo", 3 * math.cos(0.2 * i))
    plot.update()
```

## Installation

### From conda-forge

```console
conda install -c conda-forge matplotlive
```

### From PyPI

```console
pip install matplotlive
```

## See also

- [Teleplot](https://github.com/nesnes/teleplot): alternative to plot telemetry data from a running program.
