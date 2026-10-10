# Changelog

## Unreleased

- Ecosystem standardization: SECURITY.md, CONTRIBUTING.md, requirements, CI smoke checks.

## 1.0.0 (2026-09-18)

- Initial stable single-tool release (educational, authorized-use only).

## [3.0.0] - 2026-10-10
### Added
- Soft-404 baseline filtering
- --bypass (401/403 header bypass attempts), --status filter, sensitive-path tags
- Unified TBH v3 CLI: --proxy, --cookie, -H, --timeout, --delay, --json, --version, --no-color
- Baseline / soft-404 logic, exit codes for pipelines (0 clean, 1 finding, 2 error)
- Consistent JSON report schema (tool, version, target, baseline, findings, summary)
### Changed
- Honest versioning and User-Agent with repo link
- Proper exception handling (no bare except)
