"""Micro-benchmarking that explains why code is slow, not just how long it takes."""

from importlib.metadata import version as _version

from quickbeam._core import now_ns

__all__ = ["__version__", "now_ns"]
__version__ = _version("quickbeam")
