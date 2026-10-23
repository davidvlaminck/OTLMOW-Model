# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-21 · commit `0597d8b26`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 723 | 🔴 |
| files needing `ruff format` | ≤ 0 | 78 | 🔴 |
| mypy errors | ≤ 0 | 669 | 🔴 |
| test coverage (lines, owned code) | ≥ 80.0 | 95.8 % | 🟢 |
| test coverage (branches, owned code) | ≥ 75.0 | 91.2 % | 🟢 |
| max CRAP score | ≤ 6.0 | 6.0 | 🟢 |
| max cyclomatic complexity | ≤ 6 | 6 | 🟢 |
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

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 89.0 % of the lines and 87.4 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 56682 | 88.7 % | 44 | 18.2 % |
| hand-written | 2313 | 95.8 % | 816 | 91.2 % |

## Lead refactor target (highest CRAP)

`otlmow_model/OtlmowModel/BaseClasses/AssetSerialisation.py:327` → `clean_dict` — CRAP **6.0** — complexity **6** — coverage **100.0 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 18822 | 58 | 3137 | 6 | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` |
| 3294 | 1 | 549 | 6 | `otlmow_model/OtlmowModel/BaseClasses/AssetSerialisation.py` |
| 2862 | 18 | 477 | 6 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 2058 | 16 | 343 | 6 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |
| 1884 | 12 | 314 | 6 | `otlmow_model/OtlmowModel/Helpers/RelationValidator.py` |

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

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-21 | 92.5 | 84.4 | 762 | 661 | 13.0 | 13 | red |
| 2026-10-21 | 95.9 | 91.4 | 741 | 667 | 6.0 | 6 | red |
| 2026-10-21 | 95.8 | 91.2 | 723 | 669 | 6.0 | 6 | red |
