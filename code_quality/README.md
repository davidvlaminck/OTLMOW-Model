# Code Quality — measure → characterise → refactor → verify → ratchet

The operating manual for AI agents (and humans) that improve a Python repository
without breaking it.

Everything in this folder is self-contained:

| Path | What it is |
|---|---|
| `README.md` | This document — the process |
| `PY-ANTI-PATTERNS.md` | Banned constructs, each mapped to the ruff rule that detects it |
| `QA-REPORT.md` | **Generated** dashboard — never edit by hand |
| `scripts/qa_report.py` | Runs every gate and writes `QA-REPORT.md` + `reports/qa.json` |
| `scripts/crap_scores.py` | CRAP ranking and change hot spots |
| `coverage.cfg` | Coverage configuration for the quality gate only |
| `ci/quality.yml` | GitHub Actions workflow to copy into `.github/workflows/` |
| `reports/` | Machine-readable artefacts (generated) |

---

## 1. Philosophy

1. **Measure** objectively: lint, types, tests, coverage, complexity, security, dead code.
2. **Characterise** the behaviour before touching it — a refactor without a pinned
   behaviour is a rewrite with extra steps.
3. **Publish** a dashboard of current numbers against thresholds.
4. **Refactor** the worst offender first: highest CRAP, broken by change hot spot.
5. **Verify**: same behaviour, green tests, ratchet not regressed.
6. **Ratchet**: the gate may only get tighter. Never trade a metric for another.

The one-line summary: **metrics tell you where to look, characterisation tells you
whether you broke something.** Neither alone is a quality process.

---

## 2. The loop

```
┌────────────────┐
│ 1. Measure     │────┐
│ lint/types/    │    │
│ tests/complex  │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 2. Report      │    │
│ QA-REPORT.md   │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 3. Characterise│    │  ← pin behaviour BEFORE editing
│ golden tests   │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 4. Refactor    │    │
│ highest CRAP   │    │
│ hot spot first │    │
└───────┬────────┘    │
        ▼             │
┌────────────────┐    │
│ 5. Verify      │────┘  ← behaviour identical, tests green,
│ behaviour+tests│         ratchet not regressed
└───────┬────────┘
        ▼
    ratchet down
```

**Loop rule.** One target per cycle, one commit per behaviour change. Stop when the
cycle takes longer than the target is worth — write down why in the report and pick
the next one.

---

## 3. Tool mapping

| Stage | Tool | Catches | Does **not** catch |
|---|---|---|---|
| Lint / anti-patterns | `ruff` | style, bugs, imports, banned constructs, dead branches | design problems |
| Format | `ruff format` | formatting drift | — |
| Static types | `mypy` (staged, see §6) | wrong types, broken contracts | runtime behaviour |
| Tests | `pytest` + `pytest-cov` | regressions | whether the assertions mean anything |
| Test strength | `mutmut` | tests that assert nothing | — |
| Complexity | `radon` | unreadable functions | whether the function is needed |
| CRAP score | `radon` + `coverage` | risky code | — |
| Hot spots | `radon` + `git log` | code that keeps breaking | — |
| Security | `bandit` | injection, unsafe deserialisation | dependency CVEs → `pip-audit` |
| Dead code | `vulture` | unreachable code | public API that is used externally |
| Dependencies | `pip-audit` | known CVEs | — |
| Duplication | `jscpd` | copy-paste | — |
| Import cycles | `lint-imports` | architectural drift | — |
| Docstrings | `pydoclint` | docstring/signature mismatch | — |

Install the quality tools **into the project virtualenv** so they see the project
dependencies:

```bash
uv pip install ruff==0.17.0 "mypy<2" radon bandit vulture pip-audit
uv pip install mutmut jscpd        # optional, see sections 8 and 3
```

`radon` is optional — `scripts/crap_scores.py` falls back to `uvx radon` when it is
not installed. `pip-audit` is not optional: it is the only tool that can see
whether a pinned dependency carries a known CVE, and bandit cannot.

---

## 4. Configuration

The blocks below are already applied in `pyproject.toml` for this repository. For a
new repository, copy them and adjust the paths.

### 4.1 ruff

```toml
[tool.ruff]
line-length = 120
target-version = "py39"
src = ["otlmow_model", "UnitTests", "model_update"]
# Vendored third-party code is not ours to lint.
extend-exclude = [
    "UnitTests/TestModel",
    "otlmow_model/OtlmowModel/Classes",
    "otlmow_model/OtlmowModel/Datatypes",
    "otlmow_model/OtlmowModel/Helpers/all_classes.py",
]

[tool.ruff.lint]
select = [
    "E", "F", "I", "B", "C4", "UP", "PYI", "PT", "RUF", "S", "BLE", "TRY", "FLY",
    "A", "C", "PL", "Q", "RET", "N", "W", "T20", "G", "LOG", "PIE", "SIM", "PERF",
    "ARG", "TID", "PTH",
]
ignore = ["E501"]

[tool.ruff.lint.flake8-quotes]
inline-quotes = "single"
docstring-quotes = "double"

[tool.ruff.lint.per-file-ignores]
"otlmow_model/OtlmowModel/**/*.py" = ["N802", "N803", "N815", "N806", "TID252"]
"UnitTests/**" = ["S101", "N802", "N803", "N815", "PLR2004", "PT006", "PT011"]
"model_update/**" = ["T201", "S603", "S607"]
"code_quality/scripts/*.py" = ["T201", "S603"]

[tool.ruff.format]
docstring-code-format = true
quote-style = "single"
```

Traps, all hit and verified in this repository:

- **`"P"` is not a ruff selector.** `select = [... "P" ...]` makes ruff abort with
  `Unknown rule selector 'P'`. The pylint rules are selected with `"PL"`. (`"PG"` is
  also invalid — those pygrep rules were removed from ruff.)
- **`T20` and `G` must be selected explicitly.** `PY-ANTI-PATTERNS.md` bans `print()`
  and f-strings in logging calls; without `"T20"` / `"G"` in `select` those bans never
  fire.
- **Quote style is two settings.** `[tool.ruff.format] quote-style` drives the
  formatter; `[tool.ruff.lint.flake8-quotes] inline-quotes` drives the `Q000` linter.
  Set both to the style the code already uses, otherwise every string in the
  repository becomes a diff. This repository already uses single quotes (2 984 of
  3 196 strings).
- **`TID252` is disabled for the package, on purpose.** The package uses relative
  imports (`from ..Exceptions.X import X`) because
  `UnitTests/TestModel/OtlmowModel` is a *copy* of the package that the tests
  import under another package name. An absolute import would silently import the
  real package instead of the copy, and the tests would test the wrong code. The
  ban is switched off with a per-file ignore, not with a `# noqa`.
- **The generated model is excluded.** `Classes/`, `Datatypes/` and
  `Helpers/all_classes.py` are written by `OTLClassCreator` and overwritten by the
  daily `auto_update` workflow. A lint finding in them cannot be fixed: the next
  automatic commit overwrites the file.

### 4.2 pytest

Do **not** put `--cov` into `addopts` in a repository whose CI already computes
coverage in a separate workflow: it changes the published coverage badge and can
break the existing test matrix. Invoke coverage explicitly in the quality job:

```bash
python -m pytest --cov=otlmow_model --cov-report=json:code_quality/reports/coverage.json -q
```

`testpaths` may still be set to the real test directory (`UnitTests` here) so that a
bare `pytest` does not collect the whole repository.

### 4.3 coverage

The quality gate uses its own configuration file so it cannot interfere with the
badge produced by `.github/workflows/coverage.yml`:

```ini
# code_quality/coverage.cfg
[run]
source = otlmow_model
branch = true
omit =
    UnitTests/TestModel/*
    */__pycache__/*
    */site-packages/*

[report]
exclude_also =
    if TYPE_CHECKING:
    raise NotImplementedError
    @abstractmethod
    if __name__ == .__main__.:
```

Use it with `COVERAGE_RCFILE=code_quality/coverage.cfg` (the QA script does this
automatically) or `--cov-config=code_quality/coverage.cfg`.

**The coverage gate measures the hand-written code.** The report is split into the
generated model and the code we own, and the threshold is applied to the second
group. The whole package of this repository covers 88 % of its lines, but 55 839
of its 57 657 statements belong to the generated model: the headline number is
dominated by code that nobody refactors by hand, and it hides the gap in the code
a refactor actually touches (73.5 %).

### 4.4 mypy in a namespace package

The package has **no `__init__.py`**: it is a PEP 420 namespace package. Without
the two settings below mypy cannot resolve the relative imports of the package
and reports `Relative import climbs too many namespaces` for every one of them:

```toml
[tool.mypy]
mypy_path = "."
explicit_package_bases = true
namespace_packages = true
```

The vendored copy of the model (`UnitTests/TestModel`) and the generated trees
are followed as `Any` instead of being type checked:

```toml
[[tool.mypy.overrides]]
module = [
    "otlmow_model.OtlmowModel.Classes.*",
    "otlmow_model.OtlmowModel.Datatypes.*",
    "otlmow_model.OtlmowModel.Helpers.all_classes",
    "UnitTests.TestModel.*",
]
follow_imports = "skip"
ignore_errors = true
```

---

## 5. Gates that actually gate

The single most common failure in a quality document is a gate that cannot fail.
Every command below was executed against this repository; the exit codes are real.

| Command | What it enforces | Exit code on violation |
|---|---|---|
| `ruff check <src> <tests> <tooling> <scripts>` | every selected rule | 1 |
| `ruff format --check <src> <tests> <tooling> <scripts>` | formatting is applied | 1 |
| `mypy <src> <tests> <tooling> <scripts>` | type errors | 1 |
| `pytest --cov=otlmow_model` + the `coverage` row of the QA report | coverage floor | 1 |
| `radon cc -j <src>` + the `max complexity` row of the QA report | complexity ceiling | 1 |
| `bandit -q -r <src>` | security findings | 1 |
| `vulture <src> --min-confidence 80` | dead code | 1 |
| `qa_report.py --fail-on <gates>` | the named gates **and the ratchet** | 1 |

The quality tooling in `code_quality/scripts/` is linted and type-checked by the
same gate: a gate that does not check itself is not a gate.

> **`radon cc -n C` is not a gate.** `-n` only filters what is printed; radon exits 0
> even for a grade-`F` function.

> **radon 6 removed `--fail-under`.** `radon cc --fail-under 15 <src>` exits 2 with
> `unrecognized arguments: --fail-under`, whatever the code looks like — a gate that
> fails for the wrong reason. The complexity ceiling is the `max complexity` row of
> `QA-REPORT.md`: `qa_report.py` exits 1 when it is breached, and `ci/quality.yml`
> checks the same ceiling on the json output of radon.

> **the `ruff format` counter has to follow the ruff version.** ruff 0.17 prints
> `unformatted: File would be reformatted` per file, older versions printed
> `Would reformat: <path>`. A counter that only knows the old output reports 0
> files and the gate can never fail.

> **a crash is not a pass.** `ruff format --check` panics on a file with a byte
> order mark (`panicked at crates/ruff_annotate_snippets/.../source_map.rs`) and
> prints no file list at all: the counter would report 0 files and the gate could
> never fail. `qa_report.py` detects the panic and reports the gate as failed.

> **a file that cannot be parsed is a hole in the gate.** radon reports
> `invalid non-printable character U+FEFF` for the same files and skips them: they
> are invisible to the complexity ceiling and to the CRAP ranking. The
> `files radon cannot parse` row of the report counts them.

> **a missing tool is not a pass.** `_tool()` resolves the tools through `PATH`; a
> tool that is not installed reports 0 findings, which looks like a clean run. The
> report lists the tools that were not available, and a gate whose tool is missing
> fails.

> **a stale cache is not a measurement.** mypy's incremental cache re-checks only
> the files that changed; after a partial change it can report 1 error instead of
> 680. `qa_report.py` runs mypy with `--no-incremental`: the full check takes a
> couple of seconds and it is the only number that can be trusted.

---

## 6. Type checking — staged adoption, ending at `strict`

`strict = true` on a codebase without annotations produces thousands of errors and
is never adopted. Adopt it in three stages; each stage is a mergeable, green commit.

| Stage | Configuration | Errors in this repo | Exit criteria |
|---|---|---|---|
| 1 | bodies checked, signatures optional | **680** | zero errors |
| 2 | `disallow_untyped_defs` per module | not measured yet | package fully annotated |
| 3 | `strict = true` | not measured yet | strict enabled permanently |

Stage 1 (current state):

```toml
[tool.mypy]
python_version = "3.9"
mypy_path = "."
explicit_package_bases = true
namespace_packages = true
warn_unused_ignores = true
check_untyped_defs = true
disallow_any_generics = true
no_implicit_optional = true
strict_equality = true
warn_return_any = true

[[tool.mypy.overrides]]
module = ["otlmow_model.*"]
disallow_untyped_defs = false
```

Stage 2 — flip one module at a time, never the whole package at once:

```toml
[[tool.mypy.overrides]]
module = ["otlmow_model.OtlmowModel.Helpers.RelationValidator"]
disallow_untyped_defs = true
```

Stage 3 — the endgame. Once stage 2 is green, replace the whole block with:

```toml
[tool.mypy]
python_version = "3.9"
strict = true
```

**Do not skip straight to stage 3**: the intermediate stages keep every commit
mergeable.

The 680 errors of stage 1 are not spread evenly: 466 of them are in
`UnitTests/GeneralTests` (`OTLObject_test.py` alone has 202) and only 199 are in
the library itself. Start with the library — `RelationCreator.py` (65),
`OTLObject.py` (61) and `RelationValidator.py` (15) — and treat the tests as a
separate, later target: a test file is not a public API and a type error in a
test does not break a consumer.

> **mypy must stay below version 2.** mypy 2.x refuses to target Python 3.9
> (`Python 3.9 is not supported (must be 3.10 or higher)`) and exits with an error,
> so a package that supports 3.9 has to pin `mypy<2`. On Python 3.9 uv resolves
> `mypy<2` to 1.19.1 automatically.

---

## 7. Behaviour preservation — the gate metrics cannot replace

A refactor can halve complexity, keep coverage at 91 %, and change every cell of a
generated Excel file. Metrics do not notice. The only defence is to pin the current
behaviour **before** editing.

### 7.1 Characterisation test

Write a test that captures the *current* output of the target function and fails if
that output changes unintentionally:

```python
def test_create_relation_is_unchanged():
    """Golden file: the created relation must stay exactly the same."""
    relation = create_relation(
        relation_type=HeeftBetrokkene,
        source_uuid='0f7e6b4c-1b2a-4c3d-8e9f-0a1b2c3d4e5f',
        source_typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht',
        target_uuid='1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d',
        target_typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kade',
    )
    assert relation.to_dict() == GOLDEN_RELATION
```

Build the snapshot from *content*, not from bytes: an Excel file embeds
timestamps, a UUID is generated per run, and the model picks a random branch of a
union type.

For a CSV output compare the text; for XML compare the parsed tree; for a model
object compare `to_dict()`.

**A model object with random content cannot be compared byte by byte.** In this
repository the dummy values come from `random` inside the model, and the generated
objects carry a random value for every free field. The snapshot must therefore
normalise:

- random values become a marker that keeps their type (`<text>`, `<number>`,
  `<date>`, `<bool>`), so a value that changes type is still detected;
- the identifiers that are derived from a random source become a fixed marker;
- the order of a set-like collection is sorted before it is compared.

`UnitTests/GeneralTests/OTLObject_dict_test.py` already pins the dictionary
representation of an object; it is the natural place to extend the golden data
for the relation helpers.

### 7.2 The rule

> No refactor of a function starts before a characterisation test exists for it.

If the function cannot be characterised (side effects, network, database), write the
characterisation test for the seam above it instead.

### 7.3 Verification step

Before/after comparison is the actual gate:

```bash
git stash                  # or: work on a branch and keep the old revision
python -m pytest UnitTests -k "Relation"
git stash pop
python -m pytest UnitTests -k "Relation"
```

Both runs must pass. If the golden test fails after the refactor, either the
refactor changed behaviour (bug) or the golden file was updated to match the new
behaviour (review that diff with the same care as the code change).

---

## 8. Test strength — coverage is not proof

Coverage says a line ran. It does not say an assertion checked it. A test suite can
sit at 91 % coverage and assert nothing meaningful. Mutation testing measures the
thing that actually matters: **would the test fail if the code were wrong?**

```toml
# pyproject.toml
[tool.mutmut]
source_paths = ["otlmow_model"]
tests_dir = ["UnitTests"]        # a list in pyproject.toml, a string in setup.cfg
```

```bash
uv run mutmut run
uv run mutmut results
```

- `source_paths` is mandatory; without it mutmut cannot find the code to mutate.
- The package must be importable under its real name (mutmut's trampoline rejects
  `src.module` style package names).
- Interpret the score as *surviving mutants*, not as a percentage to optimise. A
  surviving mutant is either a missing test or a genuinely equivalent mutation —
  review them, then write the test or add `# noqa` with a reason.

Adopt mutation testing per module, starting with the module you are about to
refactor. A module with no surviving mutants can be refactored with far less fear.

---

## 9. CRAP score and change hot spots

### 9.1 Formula

```
CRAP = complexity² × (1 − coverage/100)³ + complexity
```

- `complexity` = cyclomatic complexity of the function (`radon cc -j -s`)
- `coverage` = percentage of executable lines of that function covered by tests

### 9.2 Interpretation — and its limit

| Coverage | Effect |
|---|---|
| 100 % | CRAP = complexity |
| 0 % | CRAP = complexity² + complexity |

**At high coverage CRAP degenerates into raw complexity.** In the hand-written code
of this repository the coverage is 73.5 %, so the CRAP score still mixes both
factors — but only just: the two functions with the highest CRAP are the two
with the lowest coverage *and* the highest complexity. Three consequences:

- Adding tests will not move the metric for well-covered code. Target complexity.
- The absolute threshold (≤ 6 here) is only meaningful for weakly covered code. Read the
  CRAP column *together with* the complexity and coverage columns, never alone.
- A function can be "improved" by splitting it into ten small ones. That is metric
  gaming, not a refactor: require the behaviour to stay identical and the tests to
  stay green, and review the resulting structure on its merits.

### 9.3 Bands

| CRAP | Meaning | Action |
|---|---|---|
| ≤ 5 | clean | leave alone |
| 5–10 | acceptable | monitor |
| 10–30 | risky | refactor soon |
| 30–60 | dangerous | refactor now |
| > 60 | critical | block merge |

### 9.4 Computing it

`scripts/crap_scores.py` does it and is the reference implementation:

```bash
python -m pytest --cov=otlmow_model --cov-report=json:code_quality/reports/coverage.json -q
python code_quality/scripts/crap_scores.py --source otlmow_model --top 25
```

It maps radon's blocks to covered line ranges (radon's JSON has a different shape
for one file than for many), skips class-level blocks, skips the generated trees
(`--exclude`) and reports the ranking:

```
| CRAP | Complexity | Coverage | Function | Location |
|---:|---:|---:|---|---|
| 53.5 | 25 | 64.3 % | `is_valid_relation_using_relation_uri` | `otlmow_model/OtlmowModel/Helpers/RelationValidator.py:31` |
```

A file that radon cannot parse is **skipped**, not counted as clean: the report
lists the files it could not read, because a file that is invisible to the
complexity gate is a hole in the gate.

### 9.5 Change hot spots — complexity alone picks the wrong target

The real risk of a function is complexity **times how often it changes**. A
complex function nobody touches is less urgent than a medium one that breaks every
month. The script combines git churn with complexity:

```
| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 11603 | 17 | 283 | 41 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
```

**The window matters.** The default is three years, not one: the commits of the
last twelve months in this repository are the automatic model updates, which only
touch the generated trees. A twelve-month window reports a churn of 1 commit for
every hand-written file and hides the real hot spots.

Selection rule for the lead target:

1. Rank by CRAP.
2. Rank by hot-spot score.
3. Take the function that appears high in **both**. A file that is hot but simple
   usually needs a different fix (a design change), not a local refactor.

---

## 10. AI-specific code smells

These are the failure modes that code written by a language model produces
repeatedly. Each has a detection rule, so they can be found mechanically rather
than by reading everything.

| Smell | Why it is a problem | Detection |
|---|---|---|
| **Speculative parameters** — `**kwargs` forwarded to a call that ignores them | hides typos, widens the API surface | `grep -n "\*\*kwargs" <src>`; ruff `ARG001`/`ARG002` |
| **Defensive swallowing** — `except AttributeError: pass` | hides real errors | ruff `S110`, `BLE001`, `TRY300` |
| **Duplicated sync/async twins** | two implementations, one behaviour | `jscpd --min-tokens 50 <src>` |
| **Docstring that restates the code** | noise that hides useful docs | `pydoclint`; `interrogate --fail-under 100` |
| **Silent fallback / default** — returns `[]` instead of raising | callers cannot distinguish "empty" from "broken" | review every `return None` / `return []` in a diff |
| **Renaming without behaviour change** | diff noise, hides the real change | require the diff to contain a behavioural assertion |
| **Speculative generality** — abstraction for one caller | indirection without reuse | `vulture` + "is there a second caller?" |
| **Accurate-looking but unverified API use** | hallucinated library call | see §12 |
| **Copy-pasted test fixtures** | tests assert the fixture, not the code | `jscpd` over the test tree |
| **Tautological assertions** — `assert result is not None` | proves nothing | mutation testing (§8) |

Extra rules to keep in mind when *writing* AI-assisted code:

- Prefer the smallest change that solves the problem. Do not "improve" surrounding
  code in the same edit.
- Do not add a layer of abstraction with exactly one implementation.
- Never invent a parameter, a return value or an exception that no caller uses.
- When unsure about a library API, look it up (§12) — do not guess and do not
  silence the type checker to make the guess compile.

---

## 11. Agent guardrails and commit discipline

An agent without guardrails will rewrite the repository. These limits keep the work
reviewable:

1. **One target per cycle.** The lead target from the report, nothing else.
2. **One behaviour change per commit.** Commits must be bisectable: each one is
   green on its own.
3. **Never reformat unrelated files.** If `ruff format` must run, it is its own
   commit, first, before any refactor.
4. **Never change a public API** of a published package without explicit approval.
   The camelCase names flagged by `N802`/`N803` are this package's published API —
   they are excluded in the ruff config on purpose.
5. **Never weaken a gate** to make something pass: no `# noqa` without a reason
   comment, no deleted test, no lowered threshold, no `except: pass`.
6. **Never touch vendored code** (`UnitTests/TestModel`).
7. **Do not commit generated noise** — coverage HTML, `.db` files, `.xlsx` outputs.
8. **Stop when the diff grows.** If a "small" refactor touches more than ~3 files or
   ~200 lines, it is not a refactor; split it or ask.
9. **Report honestly.** If a metric cannot be improved without changing behaviour,
   say so in the report instead of gaming the number.

### 11.1 Definition of done for a cycle

- [ ] Characterisation/golden test exists for the target and passes.
- [ ] The refactor is committed on its own, tests green.
- [ ] The golden test still passes unchanged.
- [ ] `ruff`, `mypy`, `pytest`, `bandit` are green (or the ratchet did not regress).
- [ ] `QA-REPORT.md` regenerated; the lead target moved to the next offender.
- [ ] The report states what changed and what was deliberately left alone.

---

## 12. Anti-hallucination: verify every third-party API

This repository depends on `otlmow-converter` and `otlmow-modelbuilder`, which are
not part of the standard library and are not in the training data of most models.
An agent that guesses an API produces code that looks right and fails at runtime.

**Rule: never write a call to a third-party API that has not been verified in the
installed package.**

```bash
uv run python -c "import inspect; from otlmow_converter.OtlmowConverter import OtlmowConverter; print(inspect.signature(OtlmowConverter.from_objects_to_file))"
uv run python -c "import otlmow_converter; print(otlmow_converter.__version__)"
```

Also allowed: reading the installed source
(`python -c "import x; print(x.__file__)"`) or the package's own docs/tests in
`.venv/`. Pin behaviour to the versions in `uv.lock`.

If an API cannot be verified, the correct output is a question, not an assumption.

---

## 13. Concurrency, determinism and performance checklist

Code that uses threads, async or retries breaks in ways no metric catches. Before
refactoring such code, verify:

- **Determinism** — does the output order depend on dict/set iteration or on thread
  completion order? Pin it with a sorted comparison or an explicit sort.
- **Shared state** — is a mutable default, a class attribute or a module-level
  cache mutated from a worker? (ruff `RUF012`, `B006`.)
- **Exception policy** — is an exception swallowed in a worker so the main path
  believes it succeeded?
- **Retry loops** — is there a `while True` without a bound? A retry without a
  maximum is an infinite loop waiting for a bad day.
- **Resource cleanup** — are executors, sessions and file handles closed on the
  error path?
- **Complexity** — did the refactor turn an O(n) loop into an O(n²) one? Check the
  number of database or file reads inside a loop.

---

## 14. Ratchet and diff-scoped gates

A repository with a history of violations cannot reach "zero issues" in one pass,
and an agent asked to do so will either churn the whole codebase or give up. Use a
**ratchet** instead: the budget may only shrink.

`scripts/qa_report.py` implements this. It stores the per-rule lint counts of the
previous cycle in `reports/qa-history.json` and fails when any rule count went up:

```
ratchet regressions:
  I001: 29 -> 34
```

Rules for the agent:

- Fixing a rule that is not part of the current target is allowed only if it does
  not touch unrelated code — otherwise it belongs to a separate commit.
- A rule count may never increase, including "fixes" that introduce a new rule.
- Thresholds may only be tightened, never loosened.
- The history table in `QA-REPORT.md` is the audit trail of the ratchet.

Diff-scoped checks (for a pull request, not for the whole repository):

```bash
CHANGED=$(git diff --name-only origin/master...HEAD -- '*.py')
ruff check $CHANGED
mypy $CHANGED
```

---

## 15. The QA report is generated

```bash
python code_quality/scripts/qa_report.py
```

writes `code_quality/QA-REPORT.md` and `code_quality/reports/qa.json`, and appends a
row to `reports/qa-history.json`.

- The report is **never edited by hand**. Change a threshold in the script instead.
- Regenerating it produces a small diff (only the rows that moved), so it stays
  reviewable.
- `reports/` holds generated artefacts: keep `qa.json` if you want the history in
  git, and ignore the rest. In this repository `reports/.gitignore` excludes
  `coverage.json` (7 MB) and `crap.json` (350 KB): they are rewritten by every
  run and would make every commit a multi-megabyte diff.
- `--skip-tests` reuses the existing coverage report, `--no-history` keeps the
  ratchet history untouched (for a run on the CI) and `--fail-on <gates>` limits
  the gates that block the run — see §16.

The report contains: the threshold table, the enforced gates, the lead refactor
target, the hot spots, the per-rule lint breakdown and the cycle history.

---

## 16. CI enforcement

Copy `ci/quality.yml` to `.github/workflows/quality.yml`. In this repository the
gate is **not installed yet** — plan item 1 of §18.7 — so `ci/quality.yml` is the
template of that file, and the two have to be kept in sync once it is copied.

**Roll it out in two stages**, otherwise the first run is red and the workflow gets
disabled on day two:

1. **Advisory** — the gates with a known budget report but do not block
   (`continue-on-error: true`): lint, format check, type check. They become
   blocking when their budget is zero, one rule at a time: add the gate to the
   `--fail-on` list below.
2. **Enforcing** — the gates that are green today block the merge, and so does the
   ratchet (lint counts may not increase). The absolute zero-issue gate comes
   last, once the budget is actually zero.

The individual `ruff`/`mypy`/`bandit`/`vulture` steps only make the findings
visible in the log; the thresholds that decide whether a merge is blocked live in
`DEFAULT_THRESHOLDS` of `qa_report.py`, so the workflow and the report can never
disagree.

Which gates block is decided in one place, in the script:

```yaml
- name: Quality gates
  run: |
    uv run python code_quality/scripts/qa_report.py \
      --source otlmow_model \
      --tooling model_update \
      --exclude otlmow_model/OtlmowModel/Classes,otlmow_model/OtlmowModel/Datatypes,otlmow_model/OtlmowModel/Helpers/all_classes.py \
      --skip-tests \
      --no-history \
      --fail-on bandit,dead-code
```

- `--fail-on <gates>` — the comma separated gates that must pass; without it,
  *every* gate must pass. The thresholds stay in `DEFAULT_THRESHOLDS` of the
  script, so the workflow and the report can never disagree.
- `--skip-tests` — reuse the coverage report of the test step instead of running
  the suite twice.
- `--no-history` — a run on the CI must not append a row to the ratchet history;
  the history is the audit trail of the real cycles.
- `--exclude` — the generated trees. They are not ours to fix, so they are not
  part of the security, dead-code, complexity and CRAP checks. The ruff and mypy
  configuration excludes them as well (`pyproject.toml`).

The ratchet is enforced by every run, with or without `--fail-on`.

Notes:

- Use `uv pip install -r pyproject.toml --extra test` for the project dependencies,
  then add the quality tools explicitly: `uv pip install ruff==0.17.0 "mypy<2"
  radon bandit vulture`.
- `uv sync` **removes** tools that are not in the lock file (including a locally
  installed ruff), so do not use `uv sync` and then `uv run ruff`.
- `uv run --python 3.9` **recreates** the project virtualenv with that interpreter.
  Use a separate virtualenv when you need a second interpreter.
- Pin the ruff version (`ruff==0.17.0`) so a new release cannot break the gate, and
  keep `mypy<2` while the package supports Python 3.9.
- Run the gate on the lowest supported Python version as well; type and lint
  results differ per version.

---

## 17. Anti-patterns

See `PY-ANTI-PATTERNS.md` for the banned constructs and the exact ruff rule that
detects each one. Every rule listed there is enabled in `pyproject.toml`.

---

## 18. Appendix — measured baseline (OTLMOW-Model, 2026-10-21)

Generated by `code_quality/scripts/qa_report.py`; the live dashboard is
`code_quality/QA-REPORT.md`.

### 18.1 The numbers

| Metric | Threshold | Current | Status |
| |---|---|---|
| ruff issues | 0 | **737** | 🔴 |
| files needing `ruff format` | 0 | **77** | 🔴 |
| mypy errors (stage 1) | 0 | **309** | 🔴 |
| test coverage (lines, owned code) | ≥ 80 % | **95.8 %** | 🟢 |
| test coverage (branches, owned code) | ≥ 75 % | **91.2 %** | 🟢 |
| max CRAP | ≤ 6 | **11.0** | 🔴 |
| max complexity | ≤ 6 | **11** | 🔴 |
| bandit HIGH | 0 | **1** | 🔴 |
| dead code | 0 | 0 | 🟢 |
| god classes | 0 | 0 | 🟢 |
| files radon cannot parse | 0 | 0 | 🟢 |
| known CVEs in dependencies | 0 | **95** | 🔴 |

This is the first cycle of this repository: there is no previous baseline, so
every number is a debt, not a regression. The ratchet starts here.

The two gates that are green today are `dead-code` and `god-classes` — those are
the ones that may block the merge (`--fail-on bandit,dead-code`). `pip-audit`
is now measured for the first time: it finds 95 known CVEs in 11 packages of the
local environment (bleach, lxml, mistune, nbconvert, pip, pyarrow, pygments,
pytest, soupsieve, tornado, uv). It is reported, not yet blocking — see §18.7.

### 18.2 What is in scope

The repository is not a normal library: **2 527 of its 2 584 source files are
generated**. `Classes/` and `Datatypes/` are written by `OTLClassCreator` and
overwritten by the daily `auto_update` workflow, and
`Helpers/all_classes.py` is regenerated with them. They are excluded from every
check: a finding in them cannot be fixed, because the next automatic commit
overwrites the file.

| Scope | Files | Lines | What we do with it |
|---|---:|---:|---|
| Generated | 2 527 | 140 061 | never edited by hand; covered by the tests, measured, reported |
| Hand-written (package) | 55 | 3 277 | the code the quality gate applies to |
| Hand-written (`model_update`) | 2 | 173 | the automatic model update, linted and type checked |
| Tests | 41 | 5 453 | linted and type checked, not part of the coverage gate |

The hand-written part of the package is `BaseClasses/` (27 files), `Helpers/`
(8), `Exceptions/` (15), `GeometrieTypes/` (5) and `warnings/` (1).

### 18.3 The four findings that matter

**1. A byte order mark breaks two of the gates.** Nineteen files of the
hand-written code and of the tests start with a UTF-8 BOM:

- `ruff format` **panics** on four of them (`panicked at
  crates/ruff_annotate_snippets/.../source_map.rs`). The format gate cannot
  even run — it produces no file list at all.
- `radon` refuses to parse **13** of them (`invalid non-printable character
  U+FEFF`). They are invisible to the complexity ceiling and to the CRAP
  ranking. `BaseClasses/OTLObject.py` — the most churned hand-written file of
  the repository, 2 100 changed lines — is one of them, so the hot-spot table
  cannot see it.

The BOM is invisible in an editor and harmless at runtime, which is why it
survived. It is a pure encoding change: stripping it cannot change a single
behaviour, and it unblocks the format gate, the complexity gate and the CRAP
ranking at once.

**2. The 13 invisible files hide the real hot spot.** The complexity ceiling
is not breached by 6.8×, it is breached by 8.5× — and the worst function is
not in the relation helpers. This is what the report measures once the BOM is
gone (measured on a temporary change, then reverted):

| Metric | With the BOM | Without the BOM |
|---|---:|---:|
| files needing `ruff format` | crashed | **78** |
| files radon cannot parse | 13 | 0 |
| max CRAP | 53.5 | **2554.5** |
| max complexity | 41 | **51** |
| god classes | 0 | **2** |

The lead target changes with it:

| CRAP | Complexity | Coverage | Function | Location |
|---:|---:|---:|---|---|
| 2554.5 | 51 | **1.3 %** | `_recursive_create_rdf_dict_from_asset` | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py:615` |
| 930.7 | 31 | **2.2 %** | `set_value_by_dictitem` | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py:813` |
| 465.9 | 38 | 33.3 % | `_recursive_create_dict_from_asset` | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py:516` |
| 166.6 | 13 | 3.1 % | `_make_string_version_from_dict` | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py:760` |
| 63.6 | 15 | 40.0 % | `clear_value` | `otlmow_model/OtlmowModel/BaseClasses/OTLObject.py:101` |
| 53.5 | 25 | 64.3 % | `is_valid_relation_using_relation_uri` | `otlmow_model/OtlmowModel/Helpers/RelationValidator.py:31` |
| 46.4 | 41 | 85.2 % | `create_relation` | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py:15` |

Four of the seven worst functions are in one file — `OTLObject.py`, 1 047 lines,
which holds the two god classes `OTLAttribuut` and `OTLObject`. Three of them
are **almost untested**: `_recursive_create_rdf_dict_from_asset` runs on 1.3 %
of its lines, `set_value_by_dictitem` on 2.2 %. The recursive dict/RDF
serialisation of an object is the least protected code of the package, and it
is the code every consumer of `otlmow_model` calls first.

**3. The coverage of the code we own is 73.5 %, not 88 %.** The whole package
covers 88.2 % of its lines — but 55 839 of the 57 657 statements belong to the
generated model. The hand-written code is 1 818 statements at **73.5 %** and 862
branches at **54.2 %**: 481 statements and 395 branches are never executed. The
headline number was hiding the gap; the report now splits the two and the gate
uses the owned code.

**4. The complexity ceiling is breached by 6.8×** — 8.5× once the BOM is gone.
The gate allows a complexity of 6. The worst function has 41 today, 51 after
the BOM is stripped.

### 18.4 CRAP ranking

The ranking below is the one the report produces **today**. It is incomplete:
the 13 files that radon cannot parse are not in it. The ranking after the BOM
is stripped is in §18.3 — it is a different ranking, with a different leader.

| CRAP | Complexity | Coverage | Function | Location |
|---:|---:|---:|---|---|
| 53.5 | 25 | 64.3 % | `is_valid_relation_using_relation_uri` | `otlmow_model/OtlmowModel/Helpers/RelationValidator.py:31` |
| 46.4 | 41 | 85.2 % | `create_relation` | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py:15` |
| 35.5 | 17 | 60.0 % | `validate_wkt` | `otlmow_model/OtlmowModel/BaseClasses/WKTValidator.py:35` |
| 18.3 | 18 | 90.5 % | `convert_to_correct_type` | `otlmow_model/OtlmowModel/BaseClasses/DateTimeField.py:30` |
| 17.1 | 17 | 92.7 % | `convert_to_correct_type` | `otlmow_model/OtlmowModel/BaseClasses/TimeField.py:28` |
| 14.7 | 4 | 12.5 % | `value_default` | `otlmow_model/OtlmowModel/BaseClasses/DateTimeField.py:92` |
| 13.2 | 13 | 89.5 % | `validate_coords_list` | `otlmow_model/OtlmowModel/BaseClasses/WKTValidator.py:79` |
| 13.0 | 13 | 100.0 % | `convert_to_correct_type` | `otlmow_model/OtlmowModel/BaseClasses/DateField.py:22` |
| 12.2 | 12 | 89.5 % | `_get_all_concrete_relations` | `otlmow_model/OtlmowModel/BaseClasses/RelationInteractor.py:24` |
| 12.0 | 12 | 100.0 % | `convert_to_correct_type` | `otlmow_model/OtlmowModel/BaseClasses/IntegerField.py:22` |

Two functions are above the "dangerous" band of 30. Both are in the relation
helpers, and both have the same shape: the handling of `source` and of `target`
is written out twice, in four different ways, and the deprecation check is
duplicated verbatim. That is a duplication problem, not a logic problem — which
is good news, because duplication is the one refactor a test suite can verify
without a golden file.

A third family deserves a mention: `convert_to_correct_type` exists in six
fields (`DateTimeField` 18, `TimeField` 17, `DateField` 13, `IntegerField` 12,
`BooleanField` 11, `FloatOrDecimalField`) and every one of them is above the
ceiling. The same shape is written six times.

### 18.5 Hot spots

| Score | Commits | Lines changed | Max complexity | File |
|---:|---:|---:|---:|---|
| 11603 | 17 | 283 | 41 | `otlmow_model/OtlmowModel/Helpers/RelationCreator.py` |
| 5525 | 11 | 221 | 25 | `otlmow_model/OtlmowModel/Helpers/RelationValidator.py` |
| 3708 | 12 | 206 | 18 | `otlmow_model/OtlmowModel/BaseClasses/DateTimeField.py` |
| 3430 | 16 | 343 | 10 | `otlmow_model/OtlmowModel/Helpers/OTLObjectHelper.py` |
| 3366 | 9 | 198 | 17 | `otlmow_model/OtlmowModel/BaseClasses/TimeField.py` |

`OTLObject.py` (2 100 changed lines, the most churned file of the package) does
not appear: radon cannot parse it, because of the BOM. It will appear as soon
as the BOM is gone — and it is the file with 7 of the 16 `C901` findings, the
two god classes and the four worst functions.

### 18.6 The lint debt, grouped by what it costs

855 findings. They are not 855 decisions — they are six kinds of work.

Mechanical, one commit each, no behaviour change:

| Rule | Count | What it is |
|---|---:|---|
| `Q000` | 193 | double quotes where the repository uses single quotes |
| `I001` | 84 | import order |
| `UP006` | 27 | `typing.List` / `Dict` / `Type` instead of the builtin generics |
| `SIM117` | 26 | a `with` nested in a `with` |
| `PTH100`/`PTH120`/`PTH118` | 68 | `os.path` instead of `pathlib` (mostly in the tests) |
| `RET505`/`RET506`/`RET503` | 18 | a redundant `else` after `return` |
| `W292`/`W293` | 11 | no newline at the end of the file, whitespace on a blank line |
| `C417` | 8 | an unnecessary dict comprehension |

Design decisions, one per commit, each with a test:

| Rule | Count | What it is |
|---|---:|---|
| `TRY003` | 83 | an exception raised with a long message instead of a dedicated type — 27 of them in `OTLObject.py` alone |
| `B028` | 39 | `warnings.warn` without `stacklevel=2`: the warning points at the library instead of at the caller |
| `S311` | 15 | `random` without a seed: the generated values are not reproducible |
| `RUF013` | 20 | an implicit `Optional` (`x: Path = None`) — the annotation lies |
| `F403`/`F401` | 12 | the wildcard-import facade `Helpers/all_functions.py` and two unused imports |
| `LOG015` | 6 | `logging.warning(...)` on the root logger |
| `E722` | 3 | a bare `except:` — 2 of them in `model_update/automatic_update.py` |
| `T201` | 3 | `print()` in library code |
| `RUF012` | 2 | a mutable class attribute |
| `G004` | 1 | an f-string in a logging call |
| `BLE001` | 1 | `except Exception` around a whole block |

Complexity, handled by the refactors of the plan below: `C901` (16),
`PLR0912` (11), `PLR0911` (7), `PLR0913`/`PLR0917` (8 + 8), `PLR0915` (6).

Test-only: `ARG001` (20, an unused argument in a fixture), `PLR2004` (15, a
magic value), `PT031` (17, a prefix in a pytest.raises).

### 18.7 The ordered plan

One target per cycle, one behaviour change per commit (§11).

0. **Strip the byte order mark** (19 files, one line each). No behaviour
   change — the test suite gives exactly the same result before and after
   (360 passed, 1 skipped) — and it unblocks three gates: the format gate, the
   complexity gate and the CRAP ranking. *Do this first: every other number in
   this report is provisional until the 13 invisible files are visible.* After
   it, the real baseline is the one of §18.3: max CRAP 2554.5, max complexity
   51, 78 files to format, 2 god classes.
1. **Re-measure and install the CI gate.** Copy `code_quality/ci/quality.yml` to
   `.github/workflows/quality.yml`. The two gates that are green today
   (`bandit`, `dead-code`) block the merge; the rest are reported. The ratchet
   starts at the numbers of §18.1 — but the ratchet baseline must be the one
   *after* the BOM is stripped, otherwise the first cycle already looks like a
   regression.
2. **Close the coverage gap of the owned code** (73.5 % → 80 %, 54.2 % →
   75 %). The 395 uncovered branches are where the errors are. Start with the
   four functions of `OTLObject.py` that are almost untested
   (`_recursive_create_rdf_dict_from_asset` 1.3 %, `set_value_by_dictitem`
   2.2 %, `_make_string_version_from_dict` 3.1 %): they are the lead target
   *and* the least covered.
3. **Refactor `OTLObject.py`.** It is the biggest hand-written file (1 047
   lines), it holds the two god classes, the four worst functions and 7 of the
   16 `C901` findings. Split it before touching anything else: the
   serialisation (`_recursive_create_dict_from_asset`,
   `_recursive_create_rdf_dict_from_asset`, `_make_string_version_from_dict`,
   `set_value_by_dictitem`) is one concern, the attribute model (`OTLAttribuut`)
   another.
4. **Refactor `create_relation`** (complexity 41 → ≤ 6) and
   **`is_valid_relation_using_relation_uri`** (25 → ≤ 6). Both duplicate the
   source/target handling. A characterisation test comes first (§7).
5. **One shared `convert_to_correct_type`** for the six field types, with the
   per-type logic behind a small strategy. Six copies of the same shape, each
   above the complexity ceiling.
6. **mypy stage 1 (680) → stage 2 → stage 3 `strict`**, module by module. The
   library first (199 errors), the tests later (466 errors).
7. **`ruff format` over the owned code and the real tests** — as its own
   commit, after the BOM is gone. 78 files are waiting for it.
8. **The remaining lint findings**, per rule, as separate commits: the
    mechanical ones first (one commit each), the design ones last, each with a
    test.
9. **`pip-audit`** is now measured (95 CVEs in 11 packages of the local
    environment). It is reported, not blocking. It becomes blocking when the
    environment is clean — which means upgrading the toolchain pins, not the
    library itself, since most of the 11 packages are test/CI tooling.

### 18.8 What this cycle deliberately leaves alone

- **The generated model.** `Classes/`, `Datatypes/` and `all_classes.py` are
  not linted, not type checked and not refactored. Changing the generator
  (`otlmow_modelbuilder`, a different package) is a separate project.
- **The 8-argument public functions** (`PLR0913`/`PLR0917` in
  `create_relation`, `is_valid_relation_using_relation_uri` and `OTLObject.py`):
  changing the published signature needs explicit approval (§11.4). The
  argument lists stay; the *bodies* are what the refactor touches.
- **`Helpers/all_functions.py`**, the wildcard-import facade: it is a published
  convenience import, and `F403` is the price. Replacing it with explicit
  re-exports is a public-API decision.
- **`Helpers/AssetCreator.py`** is an empty file in the published package. It is
  dead weight, but deleting it is an API decision, not a refactor.
- **The `print()` calls of `model_update`** (`T201`): printing is the interface
  of that script.
- **The lint, format and type budgets of 855, crashed and 680**: the CI
  reports them but does not block on them yet (§16). Each becomes blocking
  when its budget reaches zero.

---


## 19. Using this bundle in another repository

The bundle is designed to be copied. This section is the checklist for doing that.

### Copy as-is, no edits

| File | Why it is portable |
|---|---|
| `code_quality/scripts/crap_scores.py` | every path is derived from `__file__`; the package, the coverage report, the excluded trees and the churn window are CLI arguments. Falls back to `uvx radon` when radon is not installed. |
| `code_quality/scripts/qa_report.py` | same; the project name in the report title is read from `pyproject.toml`. The thresholds in `DEFAULT_THRESHOLDS` are the ones of the repository it was written for — every one of them has a CLI flag (`--max-crap`, `--max-complexity`, `--coverage-min`, `--coverage-branch-min`), or you edit the constant. |
| `code_quality/PY-ANTI-PATTERNS.md` | documentation only, no repository specifics. |

### Copy and edit these values

| File | What to change |
|---|---|
| `code_quality/coverage.cfg` | `source = <package>` and the `omit` list (drop the vendored-model entry if there is none). |
| `code_quality/ci/quality.yml` | the four path arguments (`otlmow_model`, `UnitTests`, `model_update`), the Python version, the tool pins (`ruff==…`, `mypy<2`), the `--exclude` list and the gates that block the merge in the `--fail-on` step. |
| `code_quality/README.md` | §4.1/§4.4/§6 config blocks; delete §18 (the measured baseline) and §20 (the test analysis of this repository) and write your own. |
| `pyproject.toml` | `[tool.ruff*]`, `[tool.mypy]`: the `src`, `extend-exclude` and `per-file-ignores` paths. |
| `DEFAULT_EXCLUDES` in both scripts | the generated trees of the repository. A repository without generated code sets it to an empty list. |

### Do not copy

`code_quality/QA-REPORT.md` and `code_quality/reports/` — they are generated.
Running the script recreates them.

### Verify after copying

```bash
python -m pytest --cov=<package> --cov-report=json:code_quality/reports/coverage.json -q
python code_quality/scripts/crap_scores.py --source <package> --exclude <generated trees>
python code_quality/scripts/qa_report.py --source <package> --tests <tests> --tooling <tooling>
```

The first two commands must print a CRAP table; the third must print the ten
metrics and write `QA-REPORT.md`. If `radon` is missing, the CRAP table comes back
empty — install it (`uv pip install radon`) or let the script use `uvx radon`. The
report lists the tools that were not available: a missing tool is reported as a
failed gate, never as a clean run.

---

## 20. Test sufficiency analysis (this repository, 2026-10-21)

A gate can only be switched on when the tests can actually *detect* a defect.
This section records what the test suite can and cannot detect today. It is the
evidence behind the order of work in §18.7.

### 20.1 What the suite covers today

| Metric | Value |
|---|---:|
| tests | 361 (+ 173 subtests) |
| line coverage, whole package | 88.2 % |
| line coverage, hand-written code | **73.5 %** |
| branch coverage, hand-written code | **54.2 %** |
| uncovered statements, hand-written code | 481 |
| uncovered branches, hand-written code | 395 |

The suite runs in 11 seconds and is green (360 passed, 1 skipped). The skipped
test is `OTLObjectHelper_test.py:251`: it fails when it runs together with the
other tests because `dynamic_create_asset_from_ns_and_name` mutates `sys.path`.
**A test that only passes when it runs alone is a test that will not protect a
refactor**: it must be fixed before the relation helpers are touched.

### 20.2 What the suite cannot detect

| Gap | Evidence | Consequence |
|---|---|---|
| **The suite measures the generated model.** 55 839 of the 57 657 measured statements belong to the generated tree, which is exercised indirectly by the instantiation tests. | The headline coverage of 88.2 % says almost nothing about the 1 818 statements of the code we own. | A refactor of `RelationCreator` or `OTLObject` could halve the coverage of the library and the package number would not move. |
| **The branch coverage of the owned code is 54.2 %.** | 395 branches are never executed, in a package whose whole logic is branching (source *or* target, instance *or* typeURI, legacy *or* not, agent *or* asset). | The half of the code that decides *which* branch to take is the half that is not tested. |
| **The serialisation of an object is almost untested.** | `_recursive_create_rdf_dict_from_asset` runs on 1.3 % of its lines, `set_value_by_dictitem` on 2.2 %, `_make_string_version_from_dict` on 3.1 %. They are the three worst functions of the package (complexity 51, 31 and 13). | The code that turns a model object into a dict, into RDF and back is the code every consumer calls first, and it is the code the suite knows the least about. |
| **The assertions are partly tautological.** 121 of the 944 assertions are `assert x is not None` and 59 are `assert x is None`. | `assert result is not None` proves that something was returned, not that it is correct. | A refactor that returns the wrong object still passes. |
| **One test only passes when it runs alone.** | `UnitTests/GeneralTests/OTLObjectHelper_test.py:251` is skipped: it fails when it runs together with the other tests because `dynamic_create_asset_from_ns_and_name` mutates `sys.path`. | A test that cannot run in the suite cannot protect a refactor. It has to be fixed before `OTLObjectHelper` is touched. |
| **The random values are not reproducible.** | `S311` fires 15 times: the model fills the free fields with `random` without a seed. | Two runs of the same input produce different objects. A golden test has to normalise the random values first — and the fact that the *library* is not reproducible is itself a finding. |

### 20.3 What has to be added before the first refactor

| Test | What it pins |
|---|---|
| A golden test of the dict serialisation | `to_dict()` of an object with every attribute type, including the nested and the list attributes |
| A golden test of the RDF serialisation | the RDF of the same object, cell by cell |
| A golden test of `from_dict` | that a dict produced by `to_dict` round-trips to the same object |
| A golden test of `create_relation` | the exact relation object for a source/target pair, in all four combinations (instance or typeURI, legacy or not) |
| A golden test of `is_valid_relation_using_relation_uri` | the boolean result and the deprecation warning for every branch of the function |
| A test of the `convert_to_correct_type` family | the conversion and the error message of every field type, including the boundary values |
| A fix for the skipped test | `dynamic_create_asset_from_ns_and_name` must not depend on the order of the test run |
| A seeded generator | `random` with a fixed seed, or an injectable value, so a golden test is stable |

### 20.4 The numbers now

| Metric | Value |
|---|---:|
| tests | 361 (+ 173 subtests) |
| line coverage, hand-written code | 73.5 % |
| branch coverage, hand-written code | 54.2 % |
| worst function, line coverage | 1.3 % (`_recursive_create_rdf_dict_from_asset`) |

Branch coverage is measured (`branch = true` in `code_quality/coverage.cfg`) and
gated separately from the line coverage — on the hand-written code, not on the
package.

