# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-30 · commit `487e0248e`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 0 | 🟢 |
| files needing `ruff format` | ≤ 0 | 2 | 🔴 |
| mypy errors | ≤ 0 | 290 | 🔴 |
| test coverage (lines, owned code) | ≥ 80.0 | 89.0 % | 🟢 |
| test coverage (branches, owned code) | ≥ 75.0 | 89.1 % | 🟢 |
| max CRAP score | ≤ 6.0 | 0.0 | 🟢 |
| max cyclomatic complexity | ≤ 6 | 0 | 🟢 |
| bandit HIGH issues | ≤ 0 | 0 | 🟢 |
| dead code items | ≤ 0 | 1217 | 🔴 |
| pip-audit vulnerabilities | ≤ 0 | 0 | 🟢 |
| god classes | ≤ 0 | 26 | 🔴 |
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

- `lint-imports`
- `radon`

## Coverage split — generated vs hand-written

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 89.0 % of the lines and 89.1 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 0 | 0.0 % | 0 | 0.0 % |
| hand-written | 59037 | 89.0 % | 864 | 89.1 % |

## Lead refactor target (highest CRAP)

_No CRAP data available._

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-27 | 0.0 | 0.0 | 0 | 1 | 0.0 | 0 | red |
| 2026-10-28 | 96.3 | 0.0 | 0 | 305 | 9.0 | 8 | red |
| 2026-10-28 | 96.5 | 92.9 | 0 | 305 | 9.0 | 8 | red |
| 2026-10-28 | 96.5 | 92.9 | 0 | 292 | 9.0 | 8 | red |
| 2026-10-30 | 0.0 | 0.0 | 0 | 1 | 0.0 | 0 | red |
| 2026-10-30 | 89.0 | 89.1 | 0 | 290 | 0.0 | 0 | red |
