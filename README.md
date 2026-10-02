# Quickbeam

Micro-benchmarking that explains *why* code is slow, not just how long it takes.

Quickbeam measures full timing distributions alongside hardware counters
(cycles, instructions, cache and branch misses) and records the environment
each measurement ran in, so a result comes with the evidence needed to
interpret it. A compiled C++20 core does the measuring; a thin Python layer
exposes it. The C++ core also works on its own as a benchmarking harness for
C++ projects.

> **Status:** early development. The published 0.1.0 is a proof of concept
> that validates the build and release pipeline; it does not include the
> measurement core. The first usable release is planned as 0.2.0.

## Install

```console
pip install quickbeam
```

Wheels are published for Linux (x86_64, aarch64) and macOS (arm64, x86_64) on
CPython 3.13 and later, including free-threaded builds. There are no runtime
dependencies.

## Usage

*Example coming with the first public API.*

### From C++

*Coming with the measurement core.* Quickbeam builds with Meson, and the core
is planned to be usable on its own from C++ projects.

## Supported platforms

| Platform | Architectures   | Hardware counters |
| -------- | --------------- | ----------------- |
| Linux    | x86_64, aarch64 | Planned, via `perf_event` |
| macOS    | arm64, x86_64   | Planned           |
| Windows  | Not supported   | Not supported     |

Minimum compiler, standard library and macOS versions are listed in the
[supported platforms](https://quickbeam.readthedocs.io/en/latest/supported-platforms.html)
page.

## Documentation

<https://quickbeam.readthedocs.io>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). To report a security issue, see
[SECURITY.md](SECURITY.md).

## License

BSD-3-Clause. See [LICENSE](LICENSE).
