# Changelog

This package uses [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)

## Unreleased
### Removed
- The dangerous function called `contains_subset` with recursive mode.
  The implementation is was to general and error prone.
  Until a stable function can be provided, it should be a part of the API. 

## [2.0.3] - 2019-10-21
### Fixed
- Expected type of `Assert.body_contains_subset`

## [2.0.2] - 2019-06-26
### Fixed
- Docstrings in `Assert` missing complete failure message

## [2.0.1] - 2019-06-25
### Fixed
- `Assert.contains_subset` failed for lists with multiple values

## [2.0.0] - 2019-06-24
### Fixed
- Docstring examples

### Removed
- `also` from Assert class

## [1.4.0] - 2019-06-19

## [1.3.0] - 2019-06-12
- More `has_status` methods for HTTP status codes

## [1.2.0] - 2019-06-11
### Added
- `body_length`

## [1.1.0] - 2019-06-11
### Added
- `has_length_greater*`
- `has_length_less*`
- methods `
subset` for asserting sub-sets

### Fixed
- Docstring from `has_length*` methods

## [1.0.0] - 2019-06-04
## [0.0.5] - 2019-05-28
## [0.0.4] - 2019-05-27
## [0.0.3] - 2019-05-27
## [0.0.2] - 2019-05-27
## [0.0.1] - 2019-05-26
