# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-21 · commit `2ef6e090a`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 855 | 🔴 |
| files needing `ruff format` | ≤ 0 | 79 | 🔴 |
| mypy errors | ≤ 0 | 680 | 🔴 |
| test coverage (lines, owned code) | ≥ 80.0 | 80.3 % | 🟢 |
| test coverage (branches, owned code) | ≥ 75.0 | 65.2 % | 🔴 |
| max CRAP score | ≤ 6.0 | 881.7 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 51 | 🔴 |
| bandit HIGH issues | ≤ 0 | 0 | 🟢 |
| dead code items | ≤ 0 | 0 | 🟢 |
| god classes | ≤ 0 | 2 | 🔴 |
| files radon cannot parse | ≤ 0 | 0 | 🟢 |

## Scope

The model in this repository is generated: the trees below are rewritten by the daily `auto_update` workflow and are never edited by hand. They are excluded from the lint, type, security, dead-code, complexity and CRAP checks, and from the coverage **gate** — the gate measures the code we own. Their coverage is still measured and reported below, because the model is the product.

- `otlmow_model/OtlmowModel/Classes`
- `otlmow_model/OtlmowModel/Datatypes`
- `otlmow_model/OtlmowModel/Helpers/all_classes.py`

## Coverage split — generated vs hand-written

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 88.5 % of the lines and 62.9 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 56621 | 88.7 % | 44 | 18.2 % |
| hand-written | 1818 | 80.3 % | 862 | 65.2 % |

## Lead refactor target (highest CRAP)

`otlmow_model/OtlmowModel/BaseClasses/OTLObject.py:615` → `_recursive_create_rdf_dict_from_asset` — CRAP **881.7** — complexity **51** — coverage **31.6 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 107202 | 57 | 2102 | 51 | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` |
| 11603 | 17 | 283 | 41 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 5525 | 11 | 221 | 25 | `otlmow_model/OtlmowModel/Helpers/RelationValidator.py` |
| 3708 | 12 | 206 | 18 | `otlmow_model/OtlmowModel/BaseClasses/DateTimeField.py` |
| 3430 | 16 | 343 | 10 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `Q000` | 193 |
| `I001` | 84 |
| `TRY003` | 83 |
| `B028` | 39 |
| `UP006` | 27 |
| `SIM117` | 26 |
| `PTH100` | 23 |
| `PTH120` | 23 |
| `PTH118` | 22 |
| `ARG001` | 20 |
| `RUF013` | 20 |
| `PT031` | 17 |
| `C901` | 16 |
| `PLR2004` | 15 |
| `S311` | 15 |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-21 | 73.5 | 54.2 | 855 | 680 | 2554.5 | 51 | red |
| 2026-10-21 | 80.3 | 65.2 | 858 | 682 | 881.7 | 51 | red |
| 2026-10-21 | 80.3 | 65.2 | 855 | 680 | 881.7 | 51 | red |
