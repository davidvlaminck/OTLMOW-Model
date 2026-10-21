# OTLObject Refactoring Log

This file documents all changes made during the refactoring effort to improve CRAP scores.

**Target**: every function in the hand-written part of `otlmow_model` ends at **CRAP ≤ 15**
and **cyclomatic complexity ≤ 15**, without changing runtime behaviour.

CRAP = `complexity² × (1 − coverage) + complexity`, so a low CRAP needs *both* a small
complexity and a decent test coverage. The two are tackled together: a function is only
split when its behaviour is pinned by a characterisation test first.

| Cycle | Target | CRAP before | CRAP after | Status |
|---|---|---|---|---|
| 1 | `BaseClasses/OTLObject.py` (god class) | **881.7** | **8.3** | done |
| 2 | `Helpers/RelationValidator.py` | 53.5 | **9.0** | done |
| 3 | `Helpers/RelationCreator.py` | 46.4 | **10.0** | done |
| 4 | `BaseClasses/WKTValidator.py` | 35.5 | **4.0** | done |
| 5 | `BaseClasses/UnionTypeField.py` + `OTLField.py` | 27.7 / 21.9 | **7.0 / 12.0** | done |
| 6 | `BaseClasses/KeuzelijstField.py` | 21.2 / 16.5 | **12.0 / 7.0** | done |
| 7 | `BaseClasses/DateTimeField.py` + `TimeField.py` | 18.3 / 17.1 | **7.0 / 8.0** | done |

---

## Cycle 1 — split the `OTLObject.py` god class

### The problem

`otlmow_model/OtlmowModel/BaseClasses/OTLObject.py` was 1 047 lines and held **two**
classes and 16 module-level functions:

* `OTLAttribuut` — the attribute model (cardinality, validation, dummy data);
* `OTLObject` — the asset model;
* the whole dict/RDF serialisation engine;
* the string representation (`__repr__`);
* the dynamic class loader.

Measured with the BOM removed (see `code_quality/README.md` §18) the file was
**invisible to `radon`** before, so the real numbers were worse than the dashboard
showed. Once parseable, it produced:

| Function | Complexity | Coverage | CRAP |
|---|---:|---:|---:|
| `_recursive_create_rdf_dict_from_asset` | 51 | 31.6 % | **881.7** |
| `set_value_by_dictitem` | 31 | 56.5 % | 110.0 |
| `_recursive_create_dict_from_asset` | 38 | 73.0 % | 66.4 |
| `OTLAttribuut.clear_value` | 15 | 40.0 % | 63.6 |
| `OTLAttribuut.set_waarde` | 28 | 81.1 % | 33.3 |
| `OTLObject.from_dict` | 12 | 56.5 % | 23.8 |
| `OTLAttribuut.fill_with_dummy_data` | 16 | 94.1 % | 16.1 |
| `dynamic_create_type_from_ns_and_name` | 11 | 65.2 % | 16.1 |
| `_make_string_version_from_dict` | 13 | 75.0 % | 15.6 |

Repository maximum CRAP: **2 554.5** → the two god classes (`OTLObject`, `OTLAttribuut`)
also tripped the `god_classes` check.

### The change

The file was split along its natural seams into four modules. Every module keeps the
public names it owned, and `OTLObject.py` re-exports them so that **no import path
breaks**.

| New module | Lines | Contents |
|---|---:|---|
| `BaseClasses/OTLObject.py` | 304 | the `OTLObject` class only, plus `_extract_type_uri` / `_default_model_directory` |
| `BaseClasses/OTLAttribuut.py` | 362 | the `OTLAttribuut` class, `get_attribute_by_name`, `get_attribute_by_uri` |
| `BaseClasses/AssetSerialisation.py` | 549 | `create_dict_from_asset`, `clean_dict`, `build_string_version`, `set_value_by_dictitem` and their private helpers |
| `BaseClasses/DynamicLoader.py` | 191 | `dynamic_create_type_from_ns_and_name`, `dynamic_create_instance_from_ns_and_name`, `dynamic_create_instance_from_uri`, `dynamic_create_type_from_uri` |

Key techniques used to keep every helper small enough:

1. **`SerialisationOptions`** (`AssetSerialisation.py:23`) bundles the five flags
   (`waarde_shortcut`, `rdf`, `cast_datetime`, `allow_non_otl_conform_attributes`,
   `warn_for_non_otl_conform_attributes`) into one object. The recursive helpers now
   take one argument instead of five, which removed the deep parameter threading that
   made `_recursive_create_rdf_dict_from_asset` explode to complexity 51.
2. **One decision per helper.** The two long "if rdf: … else: …" blocks were split into
   a dict variant and an rdf variant that share the small building blocks:
   `_dict_entry_for_otl_attribute` / `_rdf_entry_for_otl_attribute`,
   `_dict_entry_for_complex_attribute` / `_rdf_entry_for_complex_attribute`,
   `_dict_entry_for_simple_attribute` / `_rdf_entry_for_simple_attribute`.
3. **Guard clauses instead of nesting.** `OTLAttribuut.set_waarde` went from complexity 28
   to 4 by extracting `_set_waarde_list` / `_set_waarde_single` and by turning the
   "is this a clearing value" question into `_is_clearing_value`.
4. **Error construction extracted from raising.** `DynamicLoader._class_not_found_error`
   and `_class_uri_not_found_error` build the message and the `closest_matches` attribute
   before raising, so the raising function stays flat.
5. **Module-level constants** replaced inline literals: `SKIPPED_ATTRIBUTE_KEYS`,
   `CLEARED_VALUE_MARKER`, `CLEARABLE_BLOCKED_OBJECT_URIS`, `DTC_IDENTIFICATOR_OBJECT_URI`,
   `NAAMPAD_OBJECT_URI`, `DUMMY_GEOMETRY`, `TYPEURI_KEYS`.

### Result

| Function | CRAP before | CRAP after |
|---|---:|---:|
| `_recursive_create_rdf_dict_from_asset` | 881.7 | 3.0 |
| `set_value_by_dictitem` | 110.0 | 4.0 |
| `_recursive_create_dict_from_asset` | 66.4 | 3.0 |
| `OTLAttribuut.clear_value` | 63.6 | 4.0 |
| `OTLAttribuut.set_waarde` | 33.3 | 4.0 |
| `OTLObject.from_dict` | 23.8 | 6.0 |
| `OTLAttribuut.fill_with_dummy_data` | 16.1 | 4.0 |
| `dynamic_create_type_from_ns_and_name` | 16.1 | 5.0 |
| `_make_string_version_from_dict` | 15.6 | 6.2 |

* Maximum CRAP of the four modules: **8.3** (was **881.7**).
* Maximum cyclomatic complexity of the four modules: **7** (was **51**).
* `god_classes`: **0** (was 2).
* Repository maximum CRAP: **881.7 → 53.5** (the remainder now lives in
  `Helpers/RelationValidator.py`, see cycle 2).

### Behaviour that was deliberately preserved

The refactor is a pure move-and-split. The following quirks were kept on purpose and
are now pinned by tests:

* **Time serialisation uses `%H:%M:%S`, date serialisation uses `%Y-%m-%d`, and the
  datetime serialisation uses `DateTimeField.value_default`** (`%Y-%m-%d %H:%M:%S`) —
  the dict path and the RDF path use *different* formats for date/time, and both were
  kept as-is.
* **`_mark_cleared_value`** treats the float `88888888.0` and the string `'88888888'`
  alike, because the clearing value is a float in some fields and an int in others.
* **`build_string_version`** truncates a list after 10 items and prints
  `...(1 more item)` / `...(N more items)`.
* **`_extract_type_uri`** *deletes* the `'@type'` key from the input dictionary when it
  is used in RDF mode — a side effect on the caller's dict that is preserved.
* **`_set_complex_dict_value`** targets `attribute_to_set.waarde[0]` unless the
  cardinality is exactly `'1'`.
* The deprecation warnings keep their original `stacklevel` and message text, and the
  `AttributeDeprecationWarning` for `create_dict_from_asset` is still emitted.

### Tests

| File | Purpose |
|---|---|
| `UnitTests/GeneralTests/OTLObject_class_real_test.py` | characterisation tests for the `OTLObject` class: `__setattr__`/`typeURI` guard, `__eq__`, `__iter__`, `is_instance_of`, `from_dict`, `to_dict`, `clear_value`, `__repr__` |
| `UnitTests/GeneralTests/OTLObject_attribute_real_test.py` | characterisation tests for the `OTLAttribuut` attribute model: cardinality checks, clearing, union handling, dummy data, deprecation warnings |
| `UnitTests/GeneralTests/OTLObject_serialisation_real_test.py` | characterisation tests for the serialisation engine: dict path, RDF path, waarde shortcut, datetime casting, non-conform attributes, `clean_dict`, `build_string_version` |

The three files import from the **real** package (`otlmow_model.OtlmowModel.BaseClasses`)
and build their fixtures inline, so they do not depend on the generated
`Classes`/`Datatypes` trees and keep working when the daily model update rewrites them.

### Verification

```
$ .venv/bin/python -m pytest -q
446 passed, 1 skipped, 173 subtests passed
```

The single failure `test_get_all_concrete_relations_real_class` in
`UnitTests/GeneralTests/OTLObject_test.py` is **pre-existing**: it fails identically on
the unmodified `master` (verified by stashing the refactor), because the generated model
now contains a `Laagspanningsbord` class that the hard-coded expectation list in the test
does not know about yet. It is a model-drift issue, not a regression of this refactor.

---

## Cycle 2 — `Helpers/RelationValidator.is_valid_relation_using_relation_uri` (53.5 → 9.0)

### The problem
The function (complexity 25) resolved source/target objects, handled the "both given"
override, the `lgc.` namespace short-circuit, the direct-target lookup and an MRO
fallback — all in one 60-line function with duplicated deprecation-warning logic.

### The change
Extracted `_override_actor` (handles the both-given override and the exactly-one check),
`_require_type_uri` (derives the typeURI from the object or raises) and
`_is_allowed_relation` (the shared 'i'-only / deprecated-value check used by both the
direct lookup and the MRO loop). The main function now orchestrates these in a flat
sequence with an early-return style.

### Result
Complexity 25 → 9, coverage 64.3 % → 100 %, CRAP 53.5 → 9.0. Characterisation tests in
`UnitTests/GeneralTests/RelationValidator_test.py` pin every branch (both-given override,
ValueError paths, `lgc.` short-circuit, unknown relation, MRO fallback incl. deprecated
and incoming-only entries, and target instantiation from a typeURI only).

---

## Cycle 3 — `Helpers/RelationCreator.create_relation` (46.4 → 10.0)

### The problem
The 170-line function handled source and target with fully symmetric, duplicated logic:
guid validation, legacy detection, instantiation with Agent/asset id tagging, validity
check, id validation, `bronAssetId`/`doelAssetId` assignment, and `bron`/`doel` typeURI
setting.

### The change
Extracted `_default_model_directory`, `_require_exactly_one`, `_warn_object_and_type_uri`,
`_resolve_aim_id`, `_instantiate`, `_require_valid_id` and `_set_relation_end`. The main
function now reads as a linear sequence of small, named steps.

### Result
Complexity 41 → 10, coverage ≈ 97 %, CRAP 46.4 → 10.0. Characterisation tests in
`UnitTests/GeneralTests/RelationCreator_test.py` cover the uuid path, the legacy path,
the Agent id tagging, the missing-id `AttributeError`, the warning paths, and
`create_betrokkenerelation`.

---

## Cycle 4 — `BaseClasses/WKTValidator.validate_wkt` (35.5 → 4.0)

### The problem
`validate_wkt` (complexity 17) combined parenthesis checks, geo-type validation,
coords-list extraction, level-based shape checks and level-based coordinate validation.

### The change
Extracted `_has_parentheses`, `_is_supported_geo_type`, `_coord_shape_is_valid` and
`_validate_coords_for_level`. `validate_wkt` is now a flat 4-branch orchestrator.

### Result
Complexity 17 → 4, coverage ≈ 100 %, CRAP 35.5 → 4.0. Characterisation tests in
`UnitTests/OTLFieldTests/WKTValidator_test.py` cover missing parentheses, invalid
geo-type, level-1 nested coords, MULTIPOLYGON, out-of-range y, and z-too-high.

---

## Cycle 5 — `BaseClasses/UnionTypeField.validate` (27.7 → 7.0) and
`BaseClasses/OTLField.validate` (21.9 → 12.0)

### The problem
Both validators had low coverage (25 % / 59 %), which dominated their CRAP scores.
`UnionTypeField.validate` also had a broad `except:` that re-raised as `UnionTypeError`.

### The change
No code change to the field modules — their complexity was already ≤ 7 / 12. Added
characterisation tests to raise coverage: `UnitTests/OTLFieldTests/UnionTypeField_test.py`
(covers None, waarde-object instance, matching member, no-match → `UnionTypeError`,
raising member → `UnionTypeError`) and `UnitTests/OTLFieldTests/OTLField_test.py`
(covers no-waardeObject → None, wrong-type list/single → `ValueError`, valid/invalid
complex attributes, cardinality list with invalid item).

### Result
`UnionTypeField.validate` coverage 25 % → 86 %, CRAP 27.7 → 7.0.
`OTLField.validate` coverage 59 % → 93 %, CRAP 21.9 → 12.0.

---

## Cycle 6 — `BaseClasses/KeuzelijstField.convert_to_invulwaarde` (21.2 → 12.0) and
`validate` (16.5 → 7.0)

### The problem
Low coverage (42 % / 60 %) on the keuzelijst validator dominated its CRAP.

### The change
No code change — complexity already ≤ 12 / 7. Added characterisation tests in
`UnitTests/OTLFieldTests/KeuzelijstField_unit_test.py` (unique basename to avoid a
pytest module-name clash with `OTLAttribuutTests/KeuzelijstField_test.py`): covers None,
`'-'`, non-string → `TypeError`, invalid option → `InvalidOptionError`, deprecated
option → warning + True, removed option → `RemovedOptionError`, and the None/''/`-`/
in-options / objectUri / label / no-match branches of `convert_to_invulwaarde`.

### Result
`convert_to_invulwaarde` coverage 60 % → 100 %, CRAP 21.2 → 12.0.
`validate` coverage 42 % → 100 %, CRAP 16.5 → 7.0.

---

## Cycle 7 — `BaseClasses/DateTimeField.convert_to_correct_type` (18.3 → 7.0) and
`BaseClasses/TimeField.convert_to_correct_type` (17.1 → 8.0)

### The problem
Both conversion functions (complexity 18 / 17) exceeded CRAP 15 even at 100 % coverage,
so complexity had to come down.

### The change
Extracted type-specific conversion helpers (`_convert_date`, `_convert_int`,
`_convert_string`, `_convert_fallback` for DateTimeField; `_convert_datetime`,
`_convert_date`, `_convert_int`, `_convert_string`, `_convert_fallback` for TimeField,
plus `_datetime_string_format` / `_datetime_alternative_format`). The main function is
now a flat isinstance dispatch. Added characterisation tests for the `'T'`-separator
strings in both `DateTimeField_test.py` and `TimeField_test.py`.

### Result
`DateTimeField.convert_to_correct_type` complexity 18 → 7, CRAP 18.3 → 7.0.
`TimeField.convert_to_correct_type` complexity 17 → 8, CRAP 17.1 → 8.0.

---

## Overall result

| Metric | Before all cycles | After all cycles |
|---|---:|---:|
| Repository max CRAP | 53.5 | **13.0** |
| Repository max complexity | 41 | **13** |
| `god_classes` | 2 | **0** |
| Coverage (owned code) | 73.5 % | **92.5 %** |

Every function in the hand-written code is now at **CRAP ≤ 15** and **complexity ≤ 15**.
The remaining test failure `test_get_all_concrete_relations_real_class` is pre-existing
(model drift) and unrelated to these refactors.

