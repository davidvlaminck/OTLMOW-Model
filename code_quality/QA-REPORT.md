# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-23 · commit `83664c24b`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 737 | 🔴 |
| files needing `ruff format` | ≤ 0 | 77 | 🔴 |
| mypy errors | ≤ 0 | 309 | 🔴 |
| test coverage (lines, owned code) | ≥ 80.0 | 95.8 % | 🟢 |
| test coverage (branches, owned code) | ≥ 75.0 | 91.2 % | 🟢 |
| max CRAP score | ≤ 6.0 | 11.0 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 11 | 🔴 |
| bandit HIGH issues | ≤ 0 | 1 | 🔴 |
| dead code items | ≤ 0 | 0 | 🟢 |
| god classes | ≤ 0 | 0 | 🟢 |
| files radon cannot parse | ≤ 0 | 0 | 🟢 |
| known CVEs in locked dependencies | ≤ 0 | 95 | 🔴 |

## Ratchet regressions

These lint counts went **up** compared to the previous cycle and block the merge:

- W292: 10 -> 12
- F401: 6 -> 7
- PLC0415: 3 -> 6
- TRY300: 4 -> 5
- B010: 2 -> 3
- F841: 2 -> 3
- B904: 1 -> 2
- PLR0911: 0 -> 2
- N813: 0 -> 1
- S324: 0 -> 1

## Scope

The model in this repository is generated: the trees below are rewritten by the daily `auto_update` workflow and are never edited by hand. They are excluded from the lint, type, security, dead-code, complexity and CRAP checks, and from the coverage **gate** — the gate measures the code we own. Their coverage is still measured and reported below, because the model is the product.

- `otlmow_model/OtlmowModel/Classes`
- `otlmow_model/OtlmowModel/Datatypes`
- `otlmow_model/OtlmowModel/Helpers/all_classes.py`

## Coverage split — generated vs hand-written

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 89.0 % of the lines and 87.4 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 56682 | 88.7 % | 44 | 18.2 % |
| hand-written | 2317 | 95.8 % | 816 | 91.2 % |

## Known CVEs in the locked dependencies

`pip-audit --local --format json` audits the installed environment against the OSV database. The count above is the total number of vulnerabilities; bandit scans the source and cannot see whether a pinned dependency is itself vulnerable. The audit runs against the local environment rather than `uv.lock` because pip-audit does not understand uv lock files.

| Package | Version | CVEs |
|---|---|---|
| `bleach` | 6.3.0 | GHSA-g75f-g53v-794x, GHSA-gj48-438w-jh9v, GHSA-8rfp-98v4-mmr6 |
| `lxml` | 6.0.2 | PYSEC-2026-87, PYSEC-2026-87 |
| `mistune` | 3.2.0 | PYSEC-2026-168, PYSEC-2026-2651, PYSEC-2026-2206, PYSEC-2026-168, PYSEC-2026-2207, PYSEC-2026-2652, PYSEC-2026-2217, PYSEC-2026-2214… |
| `nbconvert` | 7.16.6 | PYSEC-2026-1691, PYSEC-2026-2230, PYSEC-2026-2229, PYSEC-2026-1691, PYSEC-2026-2230, PYSEC-2026-2229 |
| `pip` | 25.1.1 | PYSEC-2026-1795, PYSEC-2026-1796, PYSEC-2026-2875, PYSEC-2026-2876, PYSEC-2026-196, PYSEC-2026-1795, PYSEC-2026-1796, PYSEC-2026-196… |
| `pyarrow` | 23.0.0 | PYSEC-2026-113, PYSEC-2026-113 |
| `pygments` | 2.19.2 | PYSEC-2026-2987, PYSEC-2026-2987 |
| `pytest` | 8.4.1 | PYSEC-2026-1845, PYSEC-2026-1845 |
| `soupsieve` | 2.8.3 | PYSEC-2026-3072, PYSEC-2026-3071, PYSEC-2026-3072, PYSEC-2026-3071, PYSEC-2026-4170, PYSEC-2026-4171 |
| `tornado` | 6.5.1 | PYSEC-2026-2287, PYSEC-2026-140, PYSEC-2026-2287, PYSEC-2026-140, PYSEC-2026-3388, PYSEC-2026-3387, PYSEC-2026-3389, PYSEC-2025-266… |
| `uv` | 0.7.19 | PYSEC-2026-2001, PYSEC-2026-2295, PYSEC-2026-2001, PYSEC-2026-2295, PYSEC-2026-4321, GHSA-w476-p2h3-79g9, GHSA-pjjw-68hj-v9mw, GHSA-4gg8-gxpx-9rph |

## Lead refactor target (highest CRAP)

`otlmow_model/OtlmowModel/BaseClasses/DynamicLoader.py:171` → `_import_module` — CRAP **11.0** — complexity **11** — coverage **100.0 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 19182 | 60 | 3197 | 6 | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` |
| 3780 | 2 | 630 | 6 | `otlmow_model/OtlmowModel/BaseClasses/AssetSerialisation.py` |
| 3108 | 19 | 518 | 6 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 2832 | 17 | 472 | 6 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |
| 2453 | 2 | 223 | 11 | `otlmow_model/OtlmowModel/BaseClasses/DynamicLoader.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `Q000` | 177 |
| `I001` | 87 |
| `TRY003` | 70 |
| `B028` | 28 |
| `SIM117` | 26 |
| `PTH100` | 23 |
| `PTH120` | 23 |
| `PTH118` | 22 |
| `ARG001` | 21 |
| `PT031` | 17 |
| `ARG003` | 16 |
| `S311` | 15 |
| `RUF013` | 14 |
| `PLR2004` | 13 |
| `UP006` | 12 |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | CVEs | Result |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2026-10-21 | 92.5 | 84.4 | 762 | 661 | 13.0 | 13 | - | red |
| 2026-10-21 | 95.9 | 91.4 | 741 | 667 | 6.0 | 6 | - | red |
| 2026-10-21 | 95.8 | 91.2 | 723 | 669 | 6.0 | 6 | - | red |
