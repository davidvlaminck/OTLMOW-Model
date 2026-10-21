# QA Report — otlmow_model

> GENERATED FILE — produced by `code_quality/scripts/qa_report.py`.
> Do not edit by hand; edit the thresholds in the script instead.

Generated: 2026-10-21 · commit `338e4f38c`

## Thresholds (gate)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | ≤ 0 | 855 | 🔴 |
| files needing `ruff format` | ≤ 0 | crashed | 🔴 |
| mypy errors | ≤ 0 | 680 | 🔴 |
| test coverage (lines, owned code) | ≥ 80.0 | 73.5 % | 🔴 |
| test coverage (branches, owned code) | ≥ 75.0 | 54.2 % | 🔴 |
| max CRAP score | ≤ 6.0 | 53.5 | 🔴 |
| max cyclomatic complexity | ≤ 6 | 41 | 🔴 |
| bandit HIGH issues | ≤ 0 | 0 | 🟢 |
| dead code items | ≤ 0 | 0 | 🟢 |
| god classes | ≤ 0 | 0 | 🟢 |
| files radon cannot parse | ≤ 0 | 13 | 🔴 |

## Scope

The model in this repository is generated: the trees below are rewritten by the daily `auto_update` workflow and are never edited by hand. They are excluded from the lint, type, security, dead-code, complexity and CRAP checks, and from the coverage **gate** — the gate measures the code we own. Their coverage is still measured and reported below, because the model is the product.

- `otlmow_model/OtlmowModel/Classes`
- `otlmow_model/OtlmowModel/Datatypes`
- `otlmow_model/OtlmowModel/Helpers/all_classes.py`

## Coverage split — generated vs hand-written

The gate above measures the **hand-written** code: that is the code a refactor touches. The whole package — generated model included — covers 88.2 % of the lines and 52.4 % of the branches. The generated model lifts the headline number and would hide the gap in the code we own.

| Code | Statements | Line % | Branches | Branch % |
|---|---:|---:|---:|---:|
| generated (excluded) | 55839 | 88.7 % | 44 | 18.2 % |
| hand-written | 1818 | 73.5 % | 862 | 54.2 % |

## Files the tools cannot read

These files are invisible to the complexity gate and to the CRAP ranking. A file that cannot be parsed is a hole in the gate, not a clean file.

| File | Error |
|---|---|
| `otlmow_model/OtlmowModel/BaseClasses/ComplexField.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/FloatOrDecimalField.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/KeuzelijstField.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/LiteralField.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/MetaInfo.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/OTLField.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/StringField.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/UnionTypeField.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/BaseClasses/UnionWaarden.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/Exceptions/CouldNotConvertToCorrectTypeError.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/Exceptions/RemovedOptionError.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |
| `otlmow_model/OtlmowModel/Exceptions/UnionTypeError.py` | invalid non-printable character U+FEFF (<unknown>, line 1) |

## Lead refactor target (highest CRAP)

`otlmow_model/OtlmowModel/Helpers/RelationValidator.py:31` → `is_valid_relation_using_relation_uri` — CRAP **53.5** — complexity **25** — coverage **64.3 %**

Verify with `code_quality/README.md` §7 before touching it: the behaviour must be pinned by a golden-file test first.

## Change hot spots (churn x complexity)

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 11603 | 17 | 283 | 41 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 5525 | 11 | 221 | 25 | `otlmow_model/OtlmowModel/Helpers/RelationValidator.py` |
| 3708 | 12 | 206 | 18 | `otlmow_model/OtlmowModel/BaseClasses/DateTimeField.py` |
| 3430 | 16 | 343 | 10 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |
| 3366 | 9 | 198 | 17 | `otlmow_model/OtlmowModel/BaseClasses/TimeField.py` |

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
| 2026-10-21 | 73.5 | 54.2 | 855 | 680 | 53.5 | 41 | red |
