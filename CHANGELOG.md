# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [1.1.1] - 2024-08-29

### Added

- LivePlot: Add `push` function

### Fixed

- Fix push function missing from previous release

## [1.1.0] - 2024-08-27

### Added

- LivePlot: Add `legend` shorthand function
- LivePlot: Add `reset` function
- Sketch: Add a `reset` function

## [1.0.0] - 2024-08-06

### Added

- Base class for all library exceptions
- LivePlot class for live time series streaming
- Sine waves example using a LivePlot
- Sine waves example using a raw Sketch rather than a LivePlot
- Sketch class for fast line redrawing on an existing Matplotlib canvas
- Unit tests for the Sketch class

[unreleased]: https://github.com/stephane-caron/matplotlive/compare/v1.1.1...HEAD
[1.1.1]: https://github.com/stephane-caron/matplotlive/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/stephane-caron/matplotlive/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/stephane-caron/matplotlive/releases/tag/v1.0.0
