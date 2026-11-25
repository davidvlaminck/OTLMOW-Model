# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-11-24 · commit `45f775622`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 529 | 🔴 |
| files needing `ruff format` | ≤ 0 | 1 | 🔴 |
| mypy errors | ≤ 0 | 3 | 🔴 |
| test coverage (lines, owned code) | ≥ 80.0 | 96.8 % | 🟢 |
| test coverage (branches, owned code) | ≥ 75.0 | 93.0 % | 🟢 |
| max CRAP score | ≤ 6.0 | 7.0 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 7 | 🔴 |
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

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 89.2 % of the lines and 89.2 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 57467 | 88.9 % | 44 | 18.2 % |
| hand-written | 2395 | 96.8 % | 830 | 93.0 % |

## Lead refactor target (highest CRAP)

`otlmow_model/OtlmowModel/BaseClasses/OTLObject.py:303` → `_extract_rdf_type_uri` — CRAP **7.0** — complexity **7** — coverage **90.9 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 17255 | 60 | 2465 | 7 | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` |
| 4032 | 7 | 672 | 6 | `otlmow_model/OtlmowModel/BaseClasses/AssetSerialisation.py` |
| 3654 | 22 | 522 | 7 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 3129 | 17 | 447 | 7 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |
| 2435 | 6 | 487 | 5 | `otlmow_model/OtlmowModel/BaseClasses/OTLAttribuut.py` |

## ruff findings per rule

| Rule | Count |
|---|---:|
| `I001` | 87 |
| `TRY003` | 70 |
| `B028` | 28 |
| `SIM117` | 26 |
| `ARG001` | 23 |
| `PTH100` | 23 |
| `PTH120` | 23 |
| `PTH118` | 22 |
| `PT031` | 17 |
| `ARG003` | 16 |
| `S311` | 15 |
| `PLR2004` | 14 |
| `UP006` | 10 |
| `F401` | 9 |
| `PLR0913` | 9 |

## History

| Date | Coverage % | Branch % | Ruff | MyPy | Max CRAP | Max complexity | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-10-30 | 0.0 | 0.0 | 0 | 1 | 0.0 | 0 | red |
| 2026-10-30 | 89.0 | 89.1 | 0 | 290 | 0.0 | 0 | red |
| 2026-11-17 | 96.5 | 92.9 | 0 | 0 | 9.0 | 8 | red |
| 2026-11-18 | 96.5 | 92.9 | 0 | 0 | 9.0 | 7 | red |
| 2026-11-18 | 96.8 | 93.0 | 0 | 0 | 7.0 | 7 | red |
| 2026-11-18 | 96.8 | 93.0 | 0 | 0 | 7.0 | 7 | red |
| 2026-11-18 | 96.8 | 93.0 | 535 | 0 | 7.0 | 7 | red |
| 2026-11-23 | 96.8 | 93.0 | 529 | 3 | 7.0 | 7 | red |
| 2026-11-24 | 96.8 | 93.0 | 529 | 3 | 7.0 | 7 | red |
| 2026-11-24 | 96.8 | 93.0 | 529 | 3 | 7.0 | 7 | red |
