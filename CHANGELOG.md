# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- script `mffdiff.py` to compare two MFF files

## [0.6.3] - 2021-05-17
### Added
- dependency Deprecated

### Changed
- deprecate property `Reader.flavor` in favor of `Reader.mff_flavor`

## [0.6.2] - 2021-02-05
### Fixed
- Remove `pip` import in `setup.py` to allow `pypi` packaging

## [0.6.1] - 2021-02-03
### Fixed
In `Reader.get_physical_samples_from_epoch()`:

- wrong output when passing `dt=0.0`; now returns empty array
- error when passing `t0 = 0, 0 < dt < 1 / sr`

## [0.6.0] - 2021-01-14
### Added
- `FileInfo` properties `acquisitionVersion`, `ampType`

### Changed
- deprecate `FileInfo` property `version` for `mffVersion`

## [0.5.9] - 2020-11-25
### Fixed
- Include license and requirements in sdist.

### Changed
- Replace circleci build with GitHub Actions lint and test workflow.

## [0.5.8] - 2020-11-17
### Added
- Ability to add multiple binary files to `mffpy.Writer` object.

### Fixed
- Disallow writing EGI-incompatible binary files.
- Allow writing binary files with 0 offset between epochs.

## [0.5.7] - 2020-11-02
### Added
- XML schemata definitions (see ".XML Files" section of README.md).
- Writing of categories.xml files.

### Changed
- Parse key elements in categories.xml files with `mffpy.xml_files.Categories` class.
- Incorporate `cached_property` dependency into `mffpy` library.

[Unreleased]: https://github.com/bel-public/mffpy/compare/v0.6.3...HEAD
[0.6.3]: https://github.com/bel-public/mffpy/compare/v0.6.2...v0.6.3
[0.6.2]: https://github.com/bel-public/mffpy/compare/v0.6.1...v0.6.2
[0.6.1]: https://github.com/bel-public/mffpy/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/bel-public/mffpy/compare/v0.5.9...v0.6.0
[0.5.9]: https://github.com/bel-public/mffpy/compare/v0.5.8...v0.5.9
[0.5.8]: https://github.com/bel-public/mffpy/compare/v0.5.7...v0.5.8
[0.5.7]: https://github.com/bel-public/mffpy/releases/tag/v0.5.7
