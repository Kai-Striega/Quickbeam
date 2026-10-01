# Quickbeam

Micro-benchmarking that explains *why* code is slow, not just how long it takes.

Quickbeam measures timing distributions and hardware counters and records the
environment each measurement ran in. A compiled C++20 core does the measuring
and a thin Python layer exposes it. The core can also be used directly from
C++.

::::{grid} 3
:::{grid-item-card} Tutorial
:link: tutorial/index
:link-type: doc
Your first benchmark, step by step.
:::
:::{grid-item-card} How-to guides
:link: how-to/index
:link-type: doc
Recipes for specific tasks.
:::
:::{grid-item-card} Reference
:link: reference/index
:link-type: doc
The Python and C++ APIs.
:::
::::

```{toctree}
:hidden:
:maxdepth: 2

tutorial/index
how-to/index
reference/index
supported-platforms
```
