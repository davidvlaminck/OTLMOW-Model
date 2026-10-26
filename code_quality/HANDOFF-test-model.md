# Handoff — the test datamodel must not carry a copy of the runtime

> A separate, self-contained task. It does **not** continue the refactoring
> cycles in `code_quality/REFACTOR_LOG.md`; it can be done before, after or
> in parallel with them.
>
> Copy the contents of this file into a new session, or simply say:
> *"Read `code_quality/HANDOFF-test-model.md` in the OTLMOW-Model repo and implement it."*

---

## 0. Hard rules for this task

- **NEVER run `git commit`, `git push`, `git add -A`, or anything that creates a commit.** The user controls the commits. After every iteration, tell the user *exactly* which files to stage and *what message* to use, and stop.
- Working dir: `/home/david/PycharmProjects/OTLMOW-Model`, branch `master`.
- The tests are the safety net: **the suite must stay green**. If a test fails after the change, triage it — do not weaken the assertion.
- The model builder and the daily `auto_update` workflow are **out of scope** (see §9). Everything in this handoff is doable in this repository alone.

---

## 1. The problem in one paragraph

`UnitTests/TestModel/OtlmowModel` is a *copy* of the package: it holds a curated
datamodel (23 class/datatype files) **and** a copy of the whole hand-written
runtime. That copy has drifted, it is loaded under **three different module
names** in a single test session, and it produces **four distinct
`OTLAttribuut` classes** — of which only one is the code that ships. The
consequence is that the unit tests do not always test the repository's
runtime, and no test notices.

The agreed fix: **delete the copy of the runtime from the test tree and bind
the test datamodel to the repository's runtime**, so that there is exactly one
implementation, and add a guard that fails the build if a copy ever comes back.

---

## 2. The vocabulary — two groups, plus the test datamodel

The project already draws this line in `code_quality/HANDOFF.md` §1 and in the
coverage split of `code_quality/QA-REPORT.md` ("generated vs hand-written").
Give it names and use them everywhere:

| group | name | content | owner | rules |
|---|---|---|---|---|
| **A** | **the datamodel** (generated) | `otlmow_model/OtlmowModel/Classes/` (1403), `Datatypes/` (1154), `Helpers/all_classes.py`, `generated_info.json` | the model builder | rewritten daily by `.github/workflows/auto_update.yml`; never hand-edited; excluded from lint/mypy/bandit/vulture/complexity/CRAP and from the coverage gate |
| **B** | **the runtime** (hand-written) | `otlmow_model/OtlmowModel/BaseClasses/` (30), `Exceptions/` (15), `Helpers/` (7 of 8), `GeometrieTypes/` (5), `warnings/` (1) | us | the quality gate applies; the refactoring cycles target this; **this is the behaviour that ships** |
| **C** | **the test datamodel** | `UnitTests/TestModel/OtlmowModel/` | hand-curated | **datamodel only** (group A subset + fixtures) — it must not contain a copy of group B |

Group A = what the OTL database describes. Group B = the machinery that
interprets it (attributes, fields, serialisation, validation, relations).
The controlled set applies to **A**; **B is always the live code from this
repository** — a copy of B is by definition not the code under development.

---

## 3. What was measured (all verified in this repository)

### 3.1 The copy has drifted

`diff -rq otlmow_model/OtlmowModel UnitTests/TestModel/OtlmowModel`:

| directory | files | differ |
|---|---:|---:|
| `BaseClasses/` | 27 | **13** |
| `Exceptions/` | 15 | 3 |
| `Helpers/` | 8 | 3 (incl. the generated `all_classes.py`) |
| `GeometrieTypes/`, `warnings/` | 6 | 0 |

11 of the 13 `BaseClasses` differences are only the **UTF-8 BOM** (removed from
the package in `70f3b1560`, never removed from the copy). The rest are real:

| file in the copy | state |
|---|---|
| `BaseClasses/OTLObject.py` | still the **pre-cycle-1 monolith** (1047 lines, both classes) — the split into `OTLAttribuut.py` / `AssetSerialisation.py` / `DynamicLoader.py` never reached it |
| `Helpers/RelationCreator.py` | still the **pre-cycle-3** version |
| `Helpers/RelationValidator.py` | still the **pre-cycle-2** version |
| `BaseClasses/{DateTimeField,TimeField,WKTValidator,KeuzelijstField,FloatOrDecimalField,StringField,LiteralField,MetaInfo}.py` | pre-cycle versions |

13 test files import group B from that copy (§6, step 3).

### 3.2 Four `OTLAttribuut` classes in one test session

```
static  attribute class : UnitTests.TestModel.OtlmowModel.BaseClasses.OTLObject
dynamic attribute class : OtlmowModel.BaseClasses.OTLObject
SAME class object ?     : False
same source file ?      : True
isinstance(static, dynamic_class) ? False
```

| # | module name | file | how it got there |
|---|---|---|---|
| 1 | `otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut` | repository | normal import — the one that ships |
| 2 | `UnitTests.TestModel.OtlmowModel.BaseClasses.OTLObject` | the copy | static import of the test datamodel |
| 3 | `OtlmowModel.BaseClasses.OTLObject` | the copy | the dynamic importer, test model |
| 4 | `OtlmowModel.BaseClasses.OTLObject` | **repository** | the dynamic importer, real model — *same name as #3, different file* |

#3 and #4 share one module name, so whichever is imported first wins and the
other is unreachable. That is the `Voedt` collision in §8.

### 3.3 The dynamic importer creates a third namespace

`otlmow_model/OtlmowModel/BaseClasses/DynamicLoader.py:169-180`:

```python
module_path = f'OtlmowModel.Classes.{namespace_path}{class_name}'   # TOP-LEVEL name
if str(model_directory) not in sys.path:
    sys.path.insert(1, str(model_directory))
return importlib.import_module(module_path)
```

It does not use a package path — it puts the model directory on `sys.path` and
imports the **top-level** name `OtlmowModel`. So the test datamodel is bound
under a *third* name, and the relative imports inside those files resolve to
`OtlmowModel.BaseClasses.*`.

| who loads the test datamodel | namespace | `...BaseClasses.OTLObject` resolves to |
|---|---|---|
| static import | `UnitTests.TestModel.OtlmowModel.*` | the copy |
| **dynamic importer** | **`OtlmowModel.*`** (top level, via `sys.path`) | the copy |
| the repository | `otlmow_model.OtlmowModel.*` | — |

### 3.4 The dynamic importer cannot tell the two models apart

```
1) real Voedt      -> otlmow_model/OtlmowModel/Classes/Onderdeel/Voedt.py
2) testmodel Voedt -> otlmow_model/OtlmowModel/Classes/Onderdeel/Voedt.py
   same class object as the real one ? True
```

Requesting `Voedt` with `model_directory=UnitTests/TestModel` returned the
**real** package's `Voedt`: the module path string is identical in both cases,
and the cache key `(namespace, class_name)` in `_create_type_from_class_dict_entry`
(`DynamicLoader.py:160-166`) **ignores `model_directory`**. `model_directory`
steers the *class-dictionary* lookup only, never the *module* that is imported.

`Instantiation_test.py:90` compares `another_test_class.typeURI ==
AnotherTestClass.typeURI` — a **string** comparison, not a class comparison —
so it passes whether or not the two classes are the same object. It does not
verify what it looks like it verifies.

---

## 4. How the fix works (the mechanism, in plain words)

**Every import — whatever its syntax — ends up as the same question: "give me
the module with this dotted name."** For a relative import, Python first
*computes* the absolute dotted name, then asks that question.

`UnitTests/TestModel/OtlmowModel/Classes/Onderdeel/AllCasesTestClass.py` starts with:

```python
from ...BaseClasses.OTLObject import OTLAttribuut
```

| written | resolves to |
|---|---|
| `.` | `UnitTests.TestModel.OtlmowModel.Classes.Onderdeel` |
| `..` | `UnitTests.TestModel.OtlmowModel.Classes` |
| `...` | `UnitTests.TestModel.OtlmowModel` |

so the relative name becomes the absolute name
`UnitTests.TestModel.OtlmowModel.BaseClasses.OTLObject`.

**Python then looks that exact string up in `sys.modules` — the cache of
"dotted name → module object" — and only asks the filesystem if it is absent.**

So: *if the real module is already registered under that name, the relative
import lands on the real code, and the copy on disk is never opened.*

Verified in a miniature:

```
WITHOUT aliasing:   leaf.Thing.origin = copy   (from .../demo/unit/model/base.py)
WITH aliasing:      leaf.Thing.origin = real   (from .../realpkg/base.py)
                    same object as realpkg.base.Thing ? True
```

and against this repository:

```
the module the relative import resolved to:
    .../otlmow_model/OtlmowModel/BaseClasses/OTLObject.py
attribute instance created by the test datamodel:
    otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut.OTLAttribuut
is it the repository OTLAttribuut ? True
```

The **same** trick has to be applied to the second namespace
(`OtlmowModel.*`, created by the dynamic importer) — otherwise the dynamic
path still reaches the copy:

```
static  attribute class : otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut.OTLAttribuut
dynamic attribute class : otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut.OTLAttribuut
both are the repository OTLAttribuut ? True
the dynamic class still comes from the test datamodel ?
    .../UnitTests/TestModel/OtlmowModel/Classes/Onderdeel/AllCasesTestClass.py
```

Note the last line: the *datamodel* still comes from the test tree — the
controlled set stays controlled. Only the runtime is redirected.

---

## 5. The solution

1. A `UnitTests/conftest.py` that registers the repository's runtime under the
   two namespaces the test tree uses.
2. Delete the 55 copied runtime files from `UnitTests/TestModel/OtlmowModel/`.
3. Re-point the 13 test files that import group B from the copy.
4. Add a guard test that fails the build if a copy comes back, and that proves
   the runtime under test is the repository's.

**No change to the model builder. No change to the CI workflow. No copy step.**

---

## 6. Implementation plan

### Step 0 — baseline

```bash
.venv/bin/python -m pytest -q          # record the number: 492 passed, 1 skipped, 1 failed
```

> There is one **pre-existing** failure, unrelated to this task:
> `UnitTests/GeneralTests/OTLObject_test.py::test_get_all_concrete_relations_real_class`
> (the real model has one more concrete relation than the test expects). Do not
> "fix" it in this task; note it in the commit message.

### Step 1 — `UnitTests/conftest.py` (new file)

```python
"""Bind the test datamodel to the runtime of this repository.

UnitTests/TestModel/OtlmowModel contains the *datamodel* only (group A).
Its generated classes import the runtime (group B) with relative imports
("from ...BaseClasses.OTLObject import OTLAttribuut"). Under a second
package name those relative imports would resolve to a *copy* of the
runtime, and the copy drifts (it already had drifted in 13 files).

Registering the repository's modules under the names the test tree uses
makes the import machinery pick them up: Python looks a module up in
sys.modules before it looks at the filesystem. The tests then always
execute the code in otlmow_model/OtlmowModel.
"""
import importlib
import pkgutil
import sys

# The two namespaces under which the test datamodel is loaded:
#  - the static one, when a test imports it directly;
#  - OtlmowModel, the top-level name the dynamic importer creates by putting
#    the model directory on sys.path (see BaseClasses/DynamicLoader.py).
NAMESPACES = ('UnitTests.TestModel.OtlmowModel', 'OtlmowModel')

RUNTIME_PACKAGES = ('BaseClasses', 'Exceptions', 'GeometrieTypes', 'warnings')

# Helpers is mixed: all_classes.py belongs to the datamodel (it lists the
# test datamodel's own classes and must keep resolving to the test tree);
# the other modules are runtime.
RUNTIME_MODULES_IN_HELPERS = (
    'OTLObjectHelper',
    'RelationCreator',
    'RelationValidator',
    'GenericHelper',
    'generated_lists',
    'all_functions',
    'AssetCreator',
)


def _alias_runtime(namespace: str) -> None:
    for package_name in RUNTIME_PACKAGES:
        package = importlib.import_module(f'otlmow_model.OtlmowModel.{package_name}')
        sys.modules[f'{namespace}.{package_name}'] = package
        for info in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f'otlmow_model.OtlmowModel.{package_name}.{info.name}')
            sys.modules[f'{namespace}.{package_name}.{info.name}'] = module
    for module_name in RUNTIME_MODULES_IN_HELPERS:
        module = importlib.import_module(f'otlmow_model.OtlmowModel.Helpers.{module_name}')
        sys.modules[f'{namespace}.Helpers.{module_name}'] = module


for _namespace in NAMESPACES:
    _alias_runtime(_namespace)
```

`conftest.py` is imported by pytest **before** any test module, so the
aliasing is in place before the first `import UnitTests.TestModel...` and before
the first dynamic import. That is the only ordering requirement.

### Step 2 — delete the copy of group B from the test tree (55 files)

```bash
git rm -r UnitTests/TestModel/OtlmowModel/BaseClasses \
          UnitTests/TestModel/OtlmowModel/Exceptions \
          UnitTests/TestModel/OtlmowModel/GeometrieTypes \
          UnitTests/TestModel/OtlmowModel/warnings
git rm UnitTests/TestModel/OtlmowModel/Helpers/all_functions.py \
       UnitTests/TestModel/OtlmowModel/Helpers/AssetCreator.py \
       UnitTests/TestModel/OtlmowModel/Helpers/generated_lists.py \
       UnitTests/TestModel/OtlmowModel/Helpers/GenericHelper.py \
       UnitTests/TestModel/OtlmowModel/Helpers/OTLObjectHelper.py \
       UnitTests/TestModel/OtlmowModel/Helpers/RelationCreator.py \
       UnitTests/TestModel/OtlmowModel/Helpers/RelationValidator.py
```

**What must remain in `UnitTests/TestModel/OtlmowModel/`:**

| keep | why |
|---|---|
| `Classes/` (12 files) | the controlled set of classes |
| `Datatypes/` (11 files) | the controlled set of datatypes |
| `Helpers/all_classes.py` | group A: the import-list of the test datamodel's own classes — used by `Instantiation_import_all_test.py` |
| `generated_info.json` | the controlled class/relation dictionary, addressed by `model_directory` |

Do **not** delete `__pycache__` directories by hand — git does not track them.

> The 23 remaining files still import group B with relative imports. They keep
> working: the aliasing from step 1 makes those relative imports land on the
> repository's modules. Do not edit them.

### Step 3 — re-point the 13 test files

Replace `UnitTests.TestModel.OtlmowModel.<group>` with `otlmow_model.OtlmowModel.<group>`:

| file | lines | import |
|---|---|---|
| `UnitTests/GeneralTests/Deprecated_test.py` | 9, 10 | `Exceptions.AttributeDeprecationWarning`, `Exceptions.ClassDeprecationWarning` |
| `UnitTests/GeneralTests/MetaInfo_test.py` | 10, 11 | `BaseClasses.MetaInfo`, `Exceptions.ClassDeprecationWarning` |
| `UnitTests/GeneralTests/OTLObject_dict_test.py` | 12, 13 | `BaseClasses.OTLObject`, `Exceptions.NonStandardAttributeWarning` |
| `UnitTests/GeneralTests/OTLObjectHelper_test.py` | 13 | `Helpers.OTLObjectHelper` |
| `UnitTests/GeneralTests/OTLObject_test.py` | 15, 17, 18 | `BaseClasses.OTLObject`, `Exceptions.CanNotClearAttributeError`, `Exceptions.NonStandardAttributeWarning` |
| `UnitTests/OTLAttribuutTests/DateFieldAttribute_test.py` | 9 | `warnings.IncorrectTypeWarning` |
| `UnitTests/OTLAttribuutTests/FloatOrDecimalAttribute_test.py` | 4, 5 | `Exceptions.CouldNotConvertToCorrectTypeError`, `warnings.IncorrectTypeWarning` |
| `UnitTests/OTLAttribuutTests/KeuzelijstField_test.py` | 8, 9 | `Exceptions.InvalidOptionError`, `Exceptions.RemovedOptionError` |
| `UnitTests/OTLAttribuutTests/KwantWrdField_test.py` | 4, 5 | `Exceptions.CouldNotConvertToCorrectTypeError`, `warnings.IncorrectTypeWarning` |
| `UnitTests/OTLAttribuutTests/OTLAttribuutDummy_test.py` | 11-18 | `BaseClasses.{Boolean,Date,DateTime,FloatOrDecimal,Integer,String,Time}Field`, `BaseClasses.OTLObject` |
| `UnitTests/OTLAttribuutTests/StringAttribute_test.py` | 4 | `Exceptions.CouldNotConvertToCorrectTypeError` |
| `UnitTests/OTLAttribuutTests/UnionTypeAttribute_test.py` | 4, 5 | `Exceptions.CouldNotConvertToCorrectTypeError`, `Exceptions.UnionTypeError` |

**Keep as is:** `UnitTests/GeneralTests/Instantiation_import_all_test.py:5`
(`from UnitTests.TestModel.OtlmowModel.Helpers.all_classes import *`) — that is
group A and must keep resolving to the test tree.

After the change, verify nothing is left:

```bash
grep -rn "UnitTests.TestModel.OtlmowModel.\(BaseClasses\|Exceptions\|GeometrieTypes\|warnings\|Helpers\.\(OTLObjectHelper\|RelationCreator\|RelationValidator\|GenericHelper\|generated_lists\|all_functions\|AssetCreator\)\)" UnitTests
# must print nothing
```

### Step 4 — the guard (new file)

`UnitTests/GeneralTests/TestModel_isolation_test.py`:

```python
"""The test datamodel must contain the datamodel only.

The runtime (BaseClasses, Exceptions, GeometrieTypes, warnings, Helpers) has
exactly one implementation: the one in otlmow_model/OtlmowModel. A copy under
UnitTests/TestModel is a second implementation that can drift - and it had
already drifted (13 files differed, and the copied OTLObject.py was still the
pre-refactor monolith). The tests would then exercise code that does not ship.

The two tests below are the guarantee: the first forbids the copy from
coming back, the second proves that the code the tests execute is the
repository's runtime - through the static import path and through the
dynamic importer, which loads the test datamodel under a third namespace.
"""
import sys
from pathlib import Path

from otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import dynamic_create_instance_from_uri

TEST_MODEL_ROOT = Path(__file__).parent.parent / 'TestModel' / 'OtlmowModel'
RUNTIME_DIRECTORIES = ('BaseClasses', 'Exceptions', 'GeometrieTypes', 'warnings')
ALL_CASES_TEST_CLASS_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'


def _first_attribute(instance):
    return next(v for v in vars(instance).values() if getattr(v, 'is_otl_attribute', False))


def test_test_model_contains_no_copy_of_the_runtime():
    offenders = [
        str(path.relative_to(TEST_MODEL_ROOT))
        for directory in RUNTIME_DIRECTORIES
        for path in (TEST_MODEL_ROOT / directory).rglob('*.py')
    ]
    assert not offenders, (
        f'The runtime must not be copied into the test datamodel: {offenders}. '
        f'Import it from otlmow_model.OtlmowModel instead.'
    )


def test_statically_imported_test_datamodel_executes_the_repository_runtime():
    from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass

    assert isinstance(_first_attribute(AllCasesTestClass()), OTLAttribuut)


def test_dynamically_imported_test_datamodel_executes_the_repository_runtime():
    instance = dynamic_create_instance_from_uri(
        ALL_CASES_TEST_CLASS_URI, model_directory=Path(__file__).parent.parent / 'TestModel')
    assert isinstance(_first_attribute(instance), OTLAttribuut)


def test_the_re_exported_attribuut_is_the_same_object():
    """The generated model imports OTLAttribuut from BaseClasses.OTLObject."""
    from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut as re_exported
    assert re_exported is OTLAttribuut
```

### Step 5 — verify

```bash
.venv/bin/python -m pytest -q
```

Expected: the same result as the baseline, **plus** the 4 new guard tests
passing. If a test fails:

- a failure in a test that imported the copy is **expected to be possible**:
  the copy was stale, so a behaviour difference may show up. Triage it: if the
  new behaviour is correct, update the test; if it is a regression, fix the
  runtime. Do not re-introduce the copy.

### Step 6 — documentation

- `code_quality/HANDOFF.md` §1: update the sentence that describes
  `UnitTests/TestModel/OtlmowModel` as "a vendored copy of the package" — it
  is a vendored copy of the **datamodel** only.
- `code_quality/README.md`: mention the test datamodel next to the
  generated/hand-written split.
- `code_quality/REFACTOR_LOG.md`: add a cycle entry for this change.

---

## 7. What the change buys

| before | after |
|---|---|
| 4 `OTLAttribuut` classes in one session | 1 |
| 13 test files import a stale copy | 0 |
| 55 files that can drift silently | 0 |
| 79 `.py` files in the test tree | 24 |
| the runtime under test is sometimes not the runtime that ships | always the runtime that ships |

---

## 8. The `Voedt` collision — files that use the class from both runtimes

`Voedt` exists in **both** models, with **identical file content** but as two
distinct class objects:

| file | role |
|---|---|
| `otlmow_model/OtlmowModel/Classes/Onderdeel/Voedt.py` | group A, the real model |
| `UnitTests/TestModel/OtlmowModel/Classes/Onderdeel/Voedt.py` | group A, the test datamodel (identical content) |

Used by the tests (all from the **test datamodel** — no test imports the real
`Voedt`):

| file | lines | use |
|---|---|---|
| `UnitTests/GeneralTests/OTLObject_test.py` | 14 (import), 1632, 1772, 1776 | `relatie = Voedt()`; relation-URI strings |
| `UnitTests/GeneralTests/Deprecated_test.py` | 13 (import), 31, 39 | `v = Voedt()` (deprecation) |
| `UnitTests/GeneralTests/RelationCreator_test.py` | 9 (import), 44, 54, 175, 179 | `relation_type=Voedt` |
| `UnitTests/GeneralTests/OTLObjectHelper_test.py` | 12 (import), 248 | `is_directional_relation(Voedt(), ...)` |
| `UnitTests/GeneralTests/RelationValidator_test.py` | 8 (import), 55, 57, 61-63, 73-75, 83-85, 92, 101, 177, 185 | `relation_type=Voedt`, `Voedt.typeURI` |
| `UnitTests/TestModel/OtlmowModel/Classes/Onderdeel/AllCasesTestClass.py` | 32 | `add_valid_relation(relation='...#Voedt', ...)` |
| `UnitTests/TestModel/OtlmowModel/Classes/Onderdeel/AnotherTestClass.py` | 19 | `add_valid_relation(relation='...#Voedt', ...)` |
| `UnitTests/TestModel/OtlmowModel/Helpers/all_classes.py` | 5 | `from ..Classes.Onderdeel.Voedt import Voedt` |

**The risk that the aliasing does not remove** (it is a `DynamicLoader` issue,
§9): the dynamic importer resolves a class *name* to whichever module was
imported first, because the module path `OtlmowModel.Classes.<ns>.<Class>` is
identical for both models and the `_imported_modules` cache key ignores
`model_directory`. Demonstrated:

```
1) real Voedt      -> otlmow_model/OtlmowModel/Classes/Onderdeel/Voedt.py
2) testmodel Voedt -> otlmow_model/OtlmowModel/Classes/Onderdeel/Voedt.py
   same class object as the real one ? True
```

The **same** collision exists for every class name that is in both models.
Full list (16 of the 23 test-datamodel files have a twin in the real package):

| test datamodel file | twin in the real package |
|---|---|
| `Classes/ImplementatieElement/AIMDBStatus.py` | yes |
| `Classes/ImplementatieElement/AIMObject.py` | yes |
| `Classes/ImplementatieElement/AIMToestand.py` | yes |
| `Classes/ImplementatieElement/AIMVersie.py` | yes |
| `Classes/ImplementatieElement/DirectioneleRelatie.py` | yes |
| `Classes/ImplementatieElement/NietDirectioneleRelatie.py` | yes |
| `Classes/ImplementatieElement/RelatieObject.py` | yes |
| `Classes/Onderdeel/Bevestiging.py` | yes |
| `Classes/Onderdeel/Voedt.py` | yes |
| `Datatypes/DtcAssetVersie.py` | yes |
| `Datatypes/DtcIdentificator.py` | yes |
| `Datatypes/KlAIMToestand.py` | yes |
| `Datatypes/KwantWrdInMaand.py` | yes |
| `Datatypes/KwantWrdInVolt.py` | yes |
| `Classes/Onderdeel/AllCasesTestClass.py` | **no** — test fixture |
| `Classes/Onderdeel/AnotherTestClass.py` | **no** — test fixture |
| `Classes/Onderdeel/DeprecatedTestClass.py` | **no** — test fixture |
| `Datatypes/DtcTestComplexType.py` | **no** — test fixture |
| `Datatypes/DtcTestComplexType2.py` | **no** — test fixture |
| `Datatypes/DteTestEenvoudigType.py` | **no** — test fixture |
| `Datatypes/DtuTestUnionType.py` | **no** — test fixture |
| `Datatypes/KwantWrdTest.py` | **no** — test fixture |
| `Datatypes/KlTestKeuzelijst.py` | **no** — test fixture |

The 9 fixtures are the reason the test datamodel exists at all: they cover
field types that the real model does not exercise in one place.

---

## 9. Out of scope — file these as separate issues

1. **The model builder emits relative imports for the test datamodel.**
   The proper end state is that the builder writes
   `from otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut import OTLAttribuut`
   (absolute) for the test-datamodel output, and relative for the shipped
   package (`TID252` stays disabled — see `code_quality/HANDOFF.md` §4). Then
   the `conftest.py` aliasing becomes unnecessary and can be dropped. The
   templates live in the external `OTLMOW-ModelBuilder` repository; the
   generated files are rewritten daily, so this cannot be fixed in
   `otlmow_model/**`.
2. **`DynamicLoader` cannot distinguish the two models** (§3.4): the module
   path has no model-specific prefix and `_imported_modules` ignores
   `model_directory`. A fix would bind the model directory under a unique
   top-level name instead of the generic `OtlmowModel`, and include the model
   directory in the cache key. That changes public behaviour
   (`dynamic_create_instance_from_uri`) and needs its own characterisation
   tests. It also stops the importer from leaving a top-level `OtlmowModel`
   name in the user's `sys.path`.
3. **The re-export in `BaseClasses/OTLObject.py`** is load-bearing for the
   140 generated files (`from ..BaseClasses.OTLObject import OTLAttribuut`).
   Keep it; it is public API for external consumers. The guard test in step 4
   protects it.
4. **`OTLObject.py` imports `AssetSerialisation` and `DynamicLoader` eagerly**,
   so importing a generated datatype drags in the serialisation engine
   (28 modules / 64.8 ms instead of 13 / 41.3 ms). A lazy `__getattr__`
   (PEP 562) would fix that. Independent of this task.

---

## 10. Risk register

| risk | likelihood | mitigation |
|---|---|---|
| A test fails because the copy was stale and the runtime changed | medium | triage: the runtime is the truth; the copy was not. Add a characterisation test for the behaviour and update the expectation. |
| The aliasing breaks an import that nobody anticipated | low | the aliasing only *adds* names to `sys.modules`; anything that imported the copy still resolves (to the repository's module). Run the full suite. |
| A new group-B module is added to the runtime and is not aliased | low | `RUNTIME_PACKAGES` is enumerated by `pkgutil.iter_modules`, so new modules are picked up automatically. Only `Helpers` is listed by name, because it is mixed. |
| The dynamic importer resolves a test-datamodel class to the real model | **known** | §9.2. The aliasing removes the runtime half of the problem; the class half remains. `Instantiation_test.py:84-104` is the place where it shows. |
| Windows CI behaves differently | low | `sys.modules` manipulation is platform-independent. The matrix (3.9 - 3.14, 3 OSes) covers it. |

---

## 11. Commit plan

The user commits; stage and propose messages only.

| # | files | message |
|---|---|---|
| 1 | `UnitTests/conftest.py`, `UnitTests/TestModel/OtlmowModel/**` (deletions), the 12 re-pointed test files | `test: run the unit tests against the repository runtime instead of a copy` |
| 2 | `UnitTests/GeneralTests/TestModel_isolation_test.py` | `test: guard against a copy of the runtime in the test datamodel` |
| 3 | `code_quality/HANDOFF.md`, `code_quality/README.md`, `code_quality/REFACTOR_LOG.md` | `docs: name the datamodel and the runtime, document the test datamodel` |

If the suite shows a behaviour difference between the copy and the runtime,
that is a **finding**: land it as its own commit with a characterisation test
that pins the runtime's behaviour, and mention it in the message.
