# Security policy

## Supported versions

Only the latest release receives security fixes.

## Reporting a vulnerability

Please report vulnerabilities privately. Do not open a public issue.

- **Preferred:** use GitHub's
  [private vulnerability reporting](https://github.com/Kai-Striega/Quickbeam/security/advisories/new).
- **Alternative:** email <me@kaistriega.com>.

Include the Quickbeam version, the environment snapshot Quickbeam prints, and
steps to reproduce.

## Scope

These are especially relevant to Quickbeam:

- Reading result files, in particular the binary format used to merge
  results across processes. These files should be treated as untrusted input.
- Hardware counter access. Quickbeam never raises its own privileges or
  changes `perf_event_paranoid`. A path where it does is a vulnerability.
- The release pipeline: wheels are published only by the tagged release
  workflow, with PyPI attestations and GitHub build provenance.

Out of scope: Quickbeam runs whatever code you ask it to benchmark, with your
privileges. That code is not sandboxed.
