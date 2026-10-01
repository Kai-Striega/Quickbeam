# Contributing to Quickbeam

Contributions are welcome. By contributing, you agree that your contribution
is licensed under the project's [BSD-3-Clause license](LICENSE). There is no
contributor agreement.

## Building from source

The recommended setup is [pixi](https://pixi.sh). It installs the compilers,
Meson, Python, Catch2, nanobind and every other tool from conda-forge, at the
versions locked in `pixi.lock`, so you get the same environment as CI.

### With pixi

```console
pixi run test-cpp      # configure, build and run the C++ tests (builddir-<env>/)
pixi run test-asan     # the same under ASan + UBSan (builddir-asan/)
pixi run test-py       # editable install, then pytest
pixi run docs          # Sphinx, warnings as errors
pixi run lint          # all pre-commit hooks
pixi run tidy          # clang-tidy
```

Other Python versions are separate environments:
`pixi run -e py313 test-py`, likewise `py315` and the free-threaded `py314t`.
To build with your system compiler instead of conda-forge's, use the `system`
environment: `CXX=clang++ pixi run -e system test-cpp`. `pixi task list` shows
everything. Tasks and environments are defined under `[tool.pixi]` in
`pyproject.toml`.

The C++ tasks and the editable install build with `--werror`, so any warning
(the project uses `warning_level=3`, which includes `-Wpedantic`) fails the build.

conda-forge's C++ standard library is newer than most system ones, so passing
locally does not guarantee the wheel builds pass. CI checks both.

### Without pixi

You need a C++20 compiler (see
[supported platforms](docs/supported-platforms.md)), Python 3.13 or later and
Git. meson-python editable installs rebuild the extension on import, and they
need the build dependencies installed in the environment:

```console
python -m venv .venv
source .venv/bin/activate
pip install --group dev
pip install --no-build-isolation --editable .
pytest
```

On free-threaded Python 3.14 (`python3.14t`), add
`-Csetup-args=-Dpython.allow_limited_api=false` to the install command,
because the stable ABI is not available there.

For the C++ core only (the tests need Catch2 3 where pkg-config can find it,
for example `apt install catch2` or `brew install catch2`):

```console
meson setup builddir -Dtests=enabled
meson compile -C builddir
meson test -C builddir
```

Use `builddir`, not `build`: meson-python's editable installs use `build/`.

Useful options (see `meson.options`):

- `-Dhardware_counters=disabled` builds without the counter backend.
- `-Db_sanitize=address,undefined -Db_lundef=false` builds with sanitisers.

## Code rules

- The core (`src/core`, `include/quickbeam`) is compiled with exceptions
  disabled. Report failures through error codes. Never abort in the hot
  path.
- Only symbols marked `QUICKBEAM_API` are exported.
- The core has no runtime dependencies beyond the C++ standard library.
- Run `pixi run -e lint pre-commit install` (or `pre-commit install`) once.
  The hooks format C++ with clang-format and Python with Ruff, and type-check
  with mypy.

## Proposing changes

1. For anything larger than a bug fix, open an issue first.
2. Add tests: Catch2 in `tests/cpp`, pytest in `tests/python`. Changes to
   measurement logic should also be checked against the `validation/` workloads.
3. Add an entry under `[Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

## Releasing

1. Set the version in `meson.build` and `CITATION.cff`.
2. Rehearse: run the Release workflow by hand (Actions → Release → Run
   workflow). It checks the versions match, builds every wheel and the sdist,
   and publishes them to TestPyPI. Check the result in a clean environment:
   `pip install -i https://test.pypi.org/simple/ quickbeam`.
3. Date the changelog entry and set `date-released` in `CITATION.cff`.
4. Tag `vX.Y.Z` on `main` (`git tag -s`) and push the tag. The release
   workflow repeats the checks and builds, then publishes to PyPI with
   attestations once the `pypi` deployment is approved.
