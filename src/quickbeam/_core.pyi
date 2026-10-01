# Stubs for the compiled quickbeam._core module. Keep in sync with _core.cpp,
# or regenerate with `python -m nanobind.stubgen -m quickbeam._core`.

def now_ns() -> int:
    """Current std::chrono::steady_clock reading in nanoseconds.

    Monotonic with an arbitrary epoch: only differences are meaningful.
    """
