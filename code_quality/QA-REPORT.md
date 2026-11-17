# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-11-17 · commit `4390f8376`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 0 | 🟢 |
| files needing `ruff format` | ≤ 0 | 2 | 🔴 |
| mypy errors | ≤ 0 | 0 | 🟢 |
| test coverage (lines, owned code) | ≥ 80.0 | 96.5 % | 🟢 |
| test coverage (branches, owned code) | ≥ 75.0 | 92.9 % | 🟢 |
| max CRAP score | ≤ 6.0 | 9.0 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 8 | 🔴 |
| bandit HIGH issues | ≤ 0 | 0 | 🟢 |
| dead code items | ≤ 0 | 0 | 🟢 |
| pip-audit vulnerabilities | ≤ 0 | 0 | 🟢 |
| god classes | ≤ 0 | 0 | 🟢 |
| files radon cannot parse | ≤ 0 | 0 | 🟢 |
| manual conventions | ≤ 0 | 0 | 🟢 |
| import cycles/architecture | ≤ — | not enabled | ⚪ |

## Scope

The model in this repository is generated: the trees below are rewritten by the daily `auto_update` workflow and are never edited by hand. They are excluded from the lint, type, security, dead-code, complexity and CRAP checks, and from the coverage **gate** — the gate measures the code we own. Their coverage is still measured and reported below, because the model is the product.

- `otlmow_model/OtlmowModel/Classes`
- `otlmow_model/OtlmowModel/Datatypes`
- `otlmow_model/OtlmowModel/Helpers/all_classes.py`

## Tools not available

The metrics of these tools are **not measured**: a missing tool reports 0 findings, which looks like a clean run. Install them before trusting the numbers above.

- `bandit`
- `lint-imports`
- `pip-audit`
- `vulture`

## Coverage split — generated vs hand-written

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 89.0 % of the lines and 89.1 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 56683 | 88.7 % | 44 | 18.2 % |
| hand-written | 2354 | 96.5 % | 820 | 92.9 % |

## Lead refactor target (highest CRAP)

`otlmow_model/OtlmowModel/BaseClasses/CachedProperty.py:34` → `__get__` — CRAP **9.0** — complexity **3** — coverage **12.5 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 22638 | 66 | 3234 | 7 | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` |
| 5166 | 26 | 738 | 7 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 4011 | 21 | 573 | 7 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |
| 4002 | 6 | 667 | 6 | `otlmow_model/OtlmowModel/BaseClasses/AssetSerialisation.py` |
| 2736 | 12 | 342 | 8 | `otlmow_model/OtlmowModel/BaseClasses/TimeField.py` |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-27 | 0.0 | 0.0 | 0 | 1 | 0.0 | 0 | red |
| 2026-10-28 | 96.3 | 0.0 | 0 | 305 | 9.0 | 8 | red |
| 2026-10-28 | 96.5 | 92.9 | 0 | 305 | 9.0 | 8 | red |
| 2026-10-28 | 96.5 | 92.9 | 0 | 292 | 9.0 | 8 | red |
| 2026-10-30 | 0.0 | 0.0 | 0 | 1 | 0.0 | 0 | red |
| 2026-10-30 | 89.0 | 89.1 | 0 | 290 | 0.0 | 0 | red |
| 2026-11-17 | 96.5 | 92.9 | 0 | 0 | 9.0 | 8 | red |
