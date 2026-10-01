# Quickbeam

Micro-benchmarking that explains *why* code is slow, not just how long it takes.

Quickbeam measures full timing distributions alongside hardware counters
(cycles, instructions, cache and branch misses) and records the environment
each measurement ran in, so a result comes with the evidence needed to
interpret it. A compiled C++20 core does the measuring; a thin Python layer
exposes it. The C++ core also works on its own as a benchmarking harness for
C++ projects.

> **Status:** pre-release. v0.1.0 is under active development and the API is
> not yet stable.

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

Quickbeam builds with Meson and installs a `quickbeam` pkg-config file. In a
Meson project it can also be used as a subproject:

```meson
quickbeam_dep = dependency('quickbeam')
```

## Supported platforms

| Platform | Architectures   | Hardware counters |
| -------- | --------------- | ----------------- |
| Linux    | x86_64, aarch64 | Yes, via `perf_event` |
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
