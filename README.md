# matplotlive

Stream live plots to a [Matplotlib](https://matplotlib.org/) figure.

## Installation

```console
pip install matplotlive
```

## Usage

```py
import math
import matplotlive

plot = matplotlive.LivePlot(
    timestep=0.001,  # seconds
    duration=1.0,    # seconds
    ylim=(-5.0, 5.0),
)

for i in range(10_000):
    plot.send("bar", math.sin(i / 10))
    plot.send("foo", 3 * math.cos(i / 100))
    plot.update()
```

## See also

- [Teleplot](https://github.com/nesnes/teleplot): alternative to plot telemetry data from a running program.
