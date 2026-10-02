# Supported platforms

## Operating systems and architectures

| OS      | Architectures   | Wheels | Hardware counters      |
| ------- | --------------- | ------ | ---------------------- |
| Linux   | x86_64, aarch64 | manylinux, musllinux | Planned, via `perf_event` |
| macOS   | arm64, x86_64   | Yes    | Planned. TODO(macos-counters) |
| Windows | –               | No     | –                      |

Windows is out of scope.

On Linux, counter access depends on `/proc/sys/kernel/perf_event_paranoid` and
on container or VM settings. Once counters are implemented, Quickbeam will
check this at runtime and report it in the environment snapshot. Unavailable
counters will produce a warning, not an error.

## Python

CPython 3.13 and later, following [SPEC 0](https://scientific-python.org/specs/spec-0000/).

- Standard builds: one stable-ABI (`abi3`) wheel per platform covers 3.13 and
  later.
- Free-threaded builds: separate wheels for 3.14t and 3.15t. TODO(abi3t): move
  3.15t to the `abi3t` stable ABI once nanobind supports it.

## Compilers and standard libraries

The minimums are the oldest versions that support every C++20 feature
Quickbeam uses, and are tested in CI from the first core code onwards. The
core does not exist yet; the features it is expected to use are concepts,
`std::span`, `<bit>`, `<chrono>` and floating-point `std::to_chars`.

| Toolchain         | Minimum version          |
| ----------------- | ------------------------ |
| GCC / libstdc++   | TODO(min-toolchain)      |
| Clang / libc++    | TODO(min-toolchain)      |
| Apple Clang       | TODO(min-toolchain)      |
| macOS deployment target | TODO(min-macos)    |

The main risk is floating-point `std::to_chars`, which serialisation depends
on. It is often the feature that sets the minimum standard library and macOS
version.

## Build tools (from source)

- Meson 1.5 or later and meson-python 0.18 or later
- Ninja
