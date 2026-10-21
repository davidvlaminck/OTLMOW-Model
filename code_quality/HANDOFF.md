# OTLMOW-Model — code quality: handoff for the next session

Copy the contents of this file into a new session, or simply say:
*"Read `code_quality/HANDOFF.md` in the OTLMOW-Model repo and continue from there."*

---

## 0. Hard rules for this task

- **NEVER run `git commit`, `git push`, `git add -A`, or anything that creates a commit.** The user controls the commits. After every iteration, tell the user *exactly* which files to stage and *what message* to use, and stop.
- Working dir: `/home/davidlinux/PycharmProjects/OTLMOW-Model`, branch `master`, HEAD `338e4f38c`.
- One target per cycle, one behaviour change per commit (see `code_quality/README.md` §11).
- A refactor of a function needs a characterisation test **before** the refactor (§7).

## 1. The repository

- Published package: `otlmow_model` (distribution), importable as `otlmow_model.OtlmowModel`.
- It is a **PEP 420 namespace package: no `__init__.py` anywhere**. That breaks mypy's relative-import resolution unless `explicit_package_bases = true` + `mypy_path` are set (done).
- **2 527 of the 2 584 source files are generated** (`OTLClassCreator`, rewritten by the daily `auto_update` workflow): `otlmow_model/OtlmowModel/Classes/**`, `otlmow_model/OtlmowModel/Datatypes/**`, `otlmow_model/OtlmowModel/Helpers/all_classes.py`. Never edit them by hand — the next automatic commit overwrites any fix. They are excluded from lint, mypy, bandit, vulture, complexity, CRAP, and from the coverage *gate*.
- Hand-written code: `BaseClasses/` (27 files), `Helpers/` (8), `Exceptions/` (15), `GeometrieTypes/` (5), `warnings/` (1), plus `model_update/` (2) and `UnitTests/` (41).
- `UnitTests/TestModel/OtlmowModel` is a **vendored copy** of the package, imported by the tests under a second name. This is why the package uses relative imports — see §4.

## 2. Environment

```bash
cd /home/davidlinux/PycharmProjects/OTLMOW-Model
.venv/bin/python --version          # 3.9
```

Quality tools are installed **in the venv** (not in the lock file):

```bash
.venv/bin/python -m pip install "ruff==0.17.0" "mypy<2" radon bandit vulture
```

> `uv sync` **removes** them (it prunes anything not in `uv.lock`). Use `uv pip install` instead.
> The scripts find the tools through `PATH`, so run them with `PATH="$PWD/.venv/bin:$PATH"`.

## 3. What is already in place (done in the previous session)

`code_quality/` is a bundle copied from the OTLMOW-Template repository and adapted to this one:

| File | State |
|---|---|
| `code_quality/README.md` | operating manual; **§18 = the measured baseline + findings + ordered plan**, **§20 = test sufficiency analysis**. Both are written for *this* repo. |
| `code_quality/PY-ANTI-PATTERNS.md` | the banned constructs, with the ruff rule for each. |
| `code_quality/scripts/qa_report.py` | the gate driver. Extended with `--exclude` (generated trees), `--tooling` (model_update), a coverage split, a `radon-parse` gate, crash/tool-absence detection. |
| `code_quality/scripts/crap_scores.py` | CRAP ranking + change hot spots. Extended with `--exclude`. |
| `code_quality/coverage.cfg` | `source = otlmow_model`, `branch = true`. |
| `code_quality/ci/quality.yml` | CI template, adapted. **Not installed yet** — no `.github/workflows/quality.yml` exists. |
| `code_quality/QA-REPORT.md` | **generated** dashboard. Do not edit by hand. |
| `code_quality/reports/qa.json`, `qa-history.json` | generated, tracked. `coverage.json` (7 MB) and `crap.json` are gitignored via `code_quality/reports/.gitignore`. |

`pyproject.toml` gained `[tool.pytest.ini_options]`, `[tool.ruff*]`, `[tool.mypy]`.

### Commands

```bash
# tests
.venv/bin/python -m pytest -q                                   # 360 passed, 1 skipped, 173 subtests
.venv/bin/python -m pytest --nbmake Readme.ipynb -q              # the CI also runs this

# coverage + report (the two commands that matter)
COVERAGE_RCFILE=code_quality/coverage.cfg .venv/bin/python -m pytest \
  --cov=otlmow_model --cov-report=json:code_quality/reports/coverage.json -q
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python code_quality/scripts/qa_report.py --skip-tests

# the gate must fail today (exit code 1) — that is correct, not a bug
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python code_quality/scripts/qa_report.py --skip-tests; echo "exit: $?"

# CRAP / hot spots
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python code_quality/scripts/crap_scores.py --source otlmow_model --top 25
```

The scripts also accept `--exclude <comma separated paths>` and `--churn-since`. Default excludes:
`otlmow_model/OtlmowModel/Classes,otlmow_model/OtlmowModel/Datatypes,otlmow_model/OtlmowModel/Helpers/all_classes.py`.

## 4. Gotchas that will bite you

- **The package must keep relative imports.** `TID252` is disabled for the package with a per-file ignore. `UnitTests/TestModel/OtlmowModel` is a *copy* of the package that the tests import under a different name — absolute imports would silently import the real package and the tests would test the wrong code. Do not "fix" TID252.
- **The published API is camelCase** (`typeURI`, `kardinaliteit_min`). `N802`/`N803`/`N815`/`N806` are ignored for the package. Do not rename anything public.
- **The test suite dirties the git index.** `UnitTests/ModelUpdater/ModelUpdater_test.py` creates `UnitTests/TestModel/OtlmowModel/Datatypes/KlNew.py`, `git add`s it, then deletes it in teardown. The file ends up staged-but-deleted (`AD` in `git status`). After running the tests, clean it with:
  ```bash
  git rm --cached -f UnitTests/TestModel/OtlmowModel/Datatypes/KlNew.py
  rm -f UnitTests/TestModel/OtlmowModel/Datatypes/KlNew.py
  ```
  It is currently staged again (`AD`) — clean it before the first commit.
- `qa_report.py` runs mypy with `--no-incremental` on purpose: mypy's incremental cache reported **1 error instead of 680** after a partial change. Do not remove that flag.
- The `ruff format` counter detects the ruff panic and reports the gate as failed. A crash is never a pass.
- `code_quality/reports/qa-history.json` is the ratchet history: **one row per run**. Reset it with `echo '[]' > code_quality/reports/qa-history.json` only when you deliberately want a new baseline. The ratchet fails the run when a lint count goes **up** — that is intentional.

## 5. The baseline (2026-10-21, first cycle of this repo)

| Metric | Threshold | Current | Status |
|---|---|---|---|
| ruff issues | 0 | 855 | 🔴 |
| files needing `ruff format` | 0 | **crashed** | 🔴 |
| mypy errors (stage 1) | 0 | 680 | 🔴 |
| coverage lines (owned code) | ≥ 80 % | 73.5 % | 🔴 |
| coverage branches (owned code) | ≥ 75 % | 54.2 % | 🔴 |
| max CRAP | ≤ 6 | 53.5 | 🔴 |
| max complexity | ≤ 6 | 41 | 🔴 |
| bandit HIGH | 0 | 0 | 🟢 |
| dead code | 0 | 0 | 🟢 |
| god classes | 0 | 0 | 🟢 |
| files radon cannot parse | 0 | 13 | 🔴 |

Green today: only `bandit` and `dead-code` → those are the two that may block the merge (`--fail-on bandit,dead-code`).

## 6. The four findings

1. **A UTF-8 BOM in 19 files breaks two gates.** `ruff format` *panics* on 4 of them (the format gate cannot run at all); `radon` cannot parse 13 of them, so they are invisible to the complexity gate and the CRAP ranking — including `OTLObject.py`, the most churned hand-written file.
2. **Those 13 invisible files hide the real hot spot.** Measured on a temporary change (then reverted): max CRAP 53.5 → **2554.5**, max complexity 41 → **51**, format debt → **78 files**, god classes 0 → **2**. New leader: `_recursive_create_rdf_dict_from_asset` (`OTLObject.py:615`, complexity 51, **1.3 % coverage**), then `set_value_by_dictitem` (31, 2.2 %), `_recursive_create_dict_from_asset` (38, 33.3 %), `_make_string_version_from_dict` (13, 3.1 %) — four of the seven worst functions are in one file, `OTLObject.py` (1 047 lines, holds the god classes `OTLAttribuut` and `OTLObject`).
3. **Coverage of the code we own is 73.5 % / 54.2 %, not 88 %.** 55 839 of the 57 657 statements are the generated model. 481 statements and 395 branches of the owned code are never executed.
4. **855 lint findings, 680 mypy errors** — grouped by cost in `code_quality/README.md` §18.6.

## 7. The plan (README §18.7) and what to commit after each iteration

Each iteration = one commit. Never commit; **stage the files and give the user the commit message.**

| # | Target | Files to stage | Suggested message |
|---|---|---|---|
| 0 | **Strip the BOM** (next task) | the 19 files below | `chore: remove the byte order mark from the source files` |
| 1 | Install the CI gate | `.github/workflows/quality.yml` (new) | `ci: add the quality gate workflow` |
| 2 | Close the coverage gap of the owned code | new/extended tests | `test: cover the object serialisation of OTLObject` |
| 3 | Refactor `OTLObject.py` | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` (+ new modules) | `refactor: split the serialisation out of OTLObject` |
| 4 | Refactor the two relation helpers | `Helpers/RelationCreator.py`, `Helpers/RelationValidator.py` | `refactor: extract the duplicated source/target handling` |
| 5 | One shared `convert_to_correct_type` | the six field modules | `refactor: share the type conversion between the fields` |
| 6 | mypy stage 1 → 2 → 3 | per module, per stage | `chore: annotate <module>` |
| 7 | `ruff format` | 78 files, **its own commit** | `style: apply ruff format` |
| 8 | The rest of the lint findings | per rule | `style: <rule>` / `refactor: <rule>` |

### Iteration 0 — the BOM fix (the next task)

19 files, one line each (the first line only). The list:

```
otlmow_model/OtlmowModel/BaseClasses/ComplexField.py
otlmow_model/OtlmowModel/BaseClasses/FloatOrDecimalField.py
otlmow_model/OtlmowModel/BaseClasses/KeuzelijstField.py
otlmow_model/OtlmowModel/BaseClasses/LiteralField.py
otlmow_model/OtlmowModel/BaseClasses/MetaInfo.py
otlmow_model/OtlmowModel/BaseClasses/OTLField.py
otlmow_model/OtlmowModel/BaseClasses/OTLObject.py
otlmow_model/OtlmowModel/BaseClasses/StringField.py
otlmow_model/OtlmowModel/BaseClasses/UnionTypeField.py
otlmow_model/OtlmowModel/BaseClasses/UnionWaarden.py
otlmow_model/OtlmowModel/Exceptions/CouldNotConvertToCorrectTypeError.py
otlmow_model/OtlmowModel/Exceptions/RemovedOptionError.py
otlmow_model/OtlmowModel/Exceptions/UnionTypeError.py
UnitTests/GeneralTests/Deprecated_test.py
UnitTests/GeneralTests/MetaInfo_test.py
UnitTests/GeneralTests/OTLObject_dict_test.py
UnitTests/GeneralTests/OTLObject_test.py
UnitTests/ModelUpdater/ModelUpdater_test.py
UnitTests/OTLFieldTests/WKTValidator_test.py
```

Method: read the bytes, drop the leading `b'\xef\xbb\xbf'`, write the rest back. Do not touch anything else in the file.

Verification (all three must hold):

1. `.venv/bin/python -m pytest -q` → **360 passed, 1 skipped, 173 subtests** (identical to today).
2. `.venv/bin/ruff format --check otlmow_model UnitTests model_update code_quality/scripts` → no panic, **78 files would be reformatted** (that is the pre-existing formatting debt, not a regression — it becomes iteration 7).
3. The report now shows `ruff_format_files: 78`, `unparsable_files: 0`, `max_crap: 2554.5`, `max_complexity: 51`, `god_classes: 2`.

Note: `ruff_issues` stays 855 and `mypy_errors` stays 680 — the BOM is invisible to both.

**Important:** after the BOM fix the ratchet baseline of `code_quality/reports/qa-history.json` is stale (it was recorded with the BOM). Decide deliberately: either regenerate the baseline with `echo '[]' > code_quality/reports/qa-history.json` before the next run, or accept that the next run shows a ratchet change. The report says: *the ratchet baseline must be the one after the BOM is stripped, otherwise the first cycle already looks like a regression.*

### After iteration 0, update these two places (same commit or a follow-up doc commit)

- `code_quality/README.md` §18.1 / §18.3 — the "with the BOM" column becomes the current state.
- `code_quality/QA-REPORT.md` — regenerate, never edit by hand.

## 8. Current git state

```
AD UnitTests/TestModel/OtlmowModel/Datatypes/KlNew.py   <- test artefact, clean it (§4)
AM code_quality/PY-ANTI-PATTERNS.md
AM code_quality/QA-REPORT.md
AM code_quality/README.md
AM code_quality/ci/quality.yml
AM code_quality/coverage.cfg
A  code_quality/reports/.gitignore
AM code_quality/reports/qa-history.json
AM code_quality/reports/qa.json
AM code_quality/scripts/crap_scores.py
AM code_quality/scripts/qa_report.py
 M pyproject.toml
```

The `code_quality/` bundle is **staged but not committed** (the user added the folder that way). `pyproject.toml` is modified but unstaged.
