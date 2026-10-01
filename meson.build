project(
  'quickbeam',
  'cpp',
  # The single source of truth for the version. pyproject.toml reads it via
  # meson-python; CITATION.cff is checked against it by the release workflow.
  version: '0.1.0',
  license: 'BSD-3-Clause',
  license_files: 'LICENSE',
  meson_version: '>=1.5.0',
  default_options: [
    'cpp_std=c++20',
    'warning_level=3',
    'buildtype=release',
    'b_ndebug=if-release',
  ],
)

cpp = meson.get_compiler('cpp')

# TODO(min-toolchain): derive the minimum GCC, Clang, Apple Clang, libstdc++
# and libc++ versions from the C++20 features the project uses, and enforce
# them here with cpp.version().version_compare(...).

# Hardware counter backend: chosen at configure time, so the build answers
# "can it compile". Whether counters are permitted is a runtime question.
hardware_counters = get_option('hardware_counters')
counters_backend = 'none'
if host_machine.system() == 'linux'
  if cpp.has_header('linux/perf_event.h', required: hardware_counters)
    counters_backend = 'linux'
  endif
elif host_machine.system() == 'darwin'
  # TODO(macos-counters): choose the macOS counter interface and add its
  # configure-time header or framework check here.
  if hardware_counters.allowed()
    counters_backend = 'macos'
  endif
else
  hardware_counters.require(
    false,
    error_message: 'hardware counters are only supported on Linux and macOS',
  )
endif

# Python bindings are disabled by default so the C++ harness builds without
# Python; pyproject.toml enables them for meson-python builds.
py = import('python').find_installation(pure: false, required: get_option('python'))

use_limited_api = false
if py.found()
  # nanobind comes from its Python package: PyPI through [build-system].requires
  # for wheel and sdist builds, conda-forge in the pixi environments. Its library
  # is built here following nanobind's own CMake build ("linked" mode).
  nanobind_root = run_command(
    py,
    '-c',
    'import nanobind, pathlib; print(pathlib.Path(nanobind.__file__).parent)',
    check: true,
  ).stdout().strip()
  # Passed as flags, not include_directories(): in pixi environments the package
  # lives under .pixi/ inside the source tree, which Meson rejects as an
  # absolute include path.
  nanobind_inc_args = [
    '-isystem', nanobind_root / 'include',
    '-isystem', nanobind_root / 'ext' / 'robin_map' / 'include',
  ]

  # Free-threaded CPython has no stable ABI before 3.15 (meson-python also
  # requires -Dpython.allow_limited_api=false there).
  free_threaded = py.get_variable('Py_GIL_DISABLED', 0) == 1
  use_limited_api = get_option('python.allow_limited_api') and not free_threaded

  nanobind_public_args = nanobind_inc_args
  if free_threaded
    nanobind_public_args += '-DNB_FREE_THREADED'
  endif
  nanobind_lib_args = nanobind_public_args + ['-DNB_BUILD', '-fno-strict-aliasing']
  if use_limited_api
    nanobind_lib_args += '-DPy_LIMITED_API=0x030D0000'  # matches limited_api below
  endif
  if not get_option('debug')
    nanobind_lib_args += '-DNB_COMPACT_ASSERTIONS'
  endif
  nanobind_link_args = []
  if host_machine.system() == 'linux'
    nanobind_lib_args += ['-ffunction-sections', '-fdata-sections']
    nanobind_link_args += '-Wl,--gc-sections'
  elif host_machine.system() == 'darwin'
    nanobind_link_args += '-Wl,@' + (nanobind_root / 'cmake' / 'darwin-ld-cpython.sym')
  endif

  nanobind_lib = static_library(
    'nanobind',
    nanobind_root / 'src' / 'nb_combined.cpp',
    dependencies: py.dependency(),
    cpp_args: nanobind_lib_args,
    gnu_symbol_visibility: 'hidden',
    pic: true,
    override_options: ['warning_level=0'],
  )
  nanobind_dep = declare_dependency(
    link_with: nanobind_lib,
    compile_args: nanobind_public_args,
    link_args: nanobind_link_args,
  )

  # The binding layer is compiled with exceptions enabled (nanobind needs them);
  # the core, when it lands, is compiled without.
  py.extension_module(
    '_core',
    'src/quickbeam/_core.cpp',
    dependencies: nanobind_dep,
    limited_api: use_limited_api ? '3.13' : '',
    install: true,
    install_tag: 'python-runtime',
    subdir: 'quickbeam',
  )
  py.install_sources(
    'src/quickbeam/__init__.py',
    'src/quickbeam/_core.pyi',
    'src/quickbeam/py.typed',
    subdir: 'quickbeam',
  )
endif

# The core library and the C++ tests are added here when their sources land.

summary(
  {
    'Hardware counters': counters_backend,
    'Python bindings': py.found(),
    'Stable ABI': use_limited_api,
  },
  section: 'Quickbeam',
)
