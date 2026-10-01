// Proof-of-concept binding: a monotonic clock read. It exercises the nanobind
// build (stable ABI, free-threaded wheels) before the measurement core exists.
#include <nanobind/nanobind.h>

#include <chrono>
#include <cstdint>

namespace quickbeam {

std::int64_t now_ns() noexcept {
    const auto since_epoch = std::chrono::steady_clock::now().time_since_epoch();
    return std::chrono::duration_cast<std::chrono::nanoseconds>(since_epoch).count();
}

} // namespace quickbeam

NB_MODULE(_core, m) {
    m.doc() = "Quickbeam's compiled extension (proof of concept).";
    m.def("now_ns", &quickbeam::now_ns,
          "Current std::chrono::steady_clock reading in nanoseconds.\n\n"
          "Monotonic with an arbitrary epoch: only differences are meaningful.");
}
