# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-21 · commit `ec682f07d`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 762 | 🔴 |
| files needing `ruff format` | ≤ 0 | 77 | 🔴 |
| mypy errors | ≤ 0 | 661 | 🔴 |
| test coverage (lines, owned code) | ≥ 80.0 | 92.5 % | 🟢 |
| test coverage (branches, owned code) | ≥ 75.0 | 84.4 % | 🟢 |
| max CRAP score | ≤ 6.0 | 13.0 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 13 | 🔴 |
| bandit HIGH issues | ≤ 0 | 0 | 🟢 |
| dead code items | ≤ 0 | 0 | 🟢 |
| god classes | ≤ 0 | 0 | 🟢 |
| files radon cannot parse | ≤ 0 | 0 | 🟢 |

## Scope

The model in this repository is generated: the trees below are rewritten by the daily `auto_update` workflow and are never edited by hand. They are excluded from the lint, type, security, dead-code, complexity and CRAP checks, and from the coverage **gate** — the gate measures the code we own. Their coverage is still measured and reported below, because the model is the product.

- `otlmow_model/OtlmowModel/Classes`
- `otlmow_model/OtlmowModel/Datatypes`
- `otlmow_model/OtlmowModel/Helpers/all_classes.py`

## Coverage split — generated vs hand-written

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 88.8 % of the lines and 80.8 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 56621 | 88.7 % | 44 | 18.2 % |
| hand-written | 1965 | 92.5 % | 762 | 84.4 % |

## Lead refactor target (highest CRAP)

`otlmow_model/OtlmowModel/BaseClasses/DateField.py:22` → `convert_to_correct_type` — CRAP **13.0** — complexity **13** — coverage **100.0 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 14714 | 57 | 2102 | 7 | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` |
| 3430 | 16 | 343 | 10 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |
| 2864 | 9 | 179 | 16 | `otlmow_model/OtlmowModel/BaseClasses/MetaInfo.py` |
| 2830 | 17 | 283 | 10 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 2275 | 11 | 175 | 13 | `otlmow_model/OtlmowModel/BaseClasses/DateField.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `Q000` | 177 |
| `I001` | 87 |
| `TRY003` | 75 |
| `B028` | 33 |
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

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-21 | 92.5 | 84.4 | 762 | 661 | 13.0 | 13 | red |
