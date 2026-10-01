import quickbeam


def test_now_ns_returns_int() -> None:
    assert isinstance(quickbeam.now_ns(), int)


def test_now_ns_is_monotonic() -> None:
    readings = [quickbeam.now_ns() for _ in range(10_000)]
    assert readings == sorted(readings)
