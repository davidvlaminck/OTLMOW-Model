# Ruff issues — generated trees (`Classes` + `Datatypes`)

Total: **4,895 errors** (3,439 auto-fixable with `--fix`).

Scope: `otlmow_model/OtlmowModel/Classes`, `otlmow_model/OtlmowModel/Datatypes`.

## Rule summary

| Rule | Count | Description |
|---|---|---|
| **UP009** | 2,557 | Remove unnecessary `# coding=utf-8` declaration |
| **RUF012** | 1,016 | Mutable default value for class attribute |
| **I001** | 651 | Import block is un-sorted or un-formatted |
| **A003** | 250 | Python builtin is shadowed by class method |
| **UP006** | 152 | Use `list` instead of `List` for type annotation |
| **UP035** | 104 | Import from `collections.abc` instead of `typing` |
| **Q003** | 39 | Change outer quotes to avoid escaping inner quotes |
| **PLR0915** | 35 | Too many statements in function |
| **RUF001** | 33 | String contains ambiguous `×` (MULTIPLICATION SIGN) |
| **PIE790** | 20 | Unnecessary `pass` statement |
| **Q004** | 13 | Unnecessary escape on inner quote character |
| **PLC2401** | 8 | Function name contains a non-ASCII character |
| **RUF002** | 7 | Docstring contains ambiguous `×` (MULTIPLICATION SIGN) |
| **F811** | 6 | Redefinition of unused name |
| **N801** | 3 | Class name should use CapWords convention |
| **F401** | 1 | Imported but unused |

## Per-rule examples

### UP009 — unnecessary UTF-8 encoding declaration

- `otlmow_model/OtlmowModel/Classes/Abstracten/AOWSType.py:1` — `# coding=utf-8`
- `otlmow_model/OtlmowModel/Classes/Abstracten/Aangrijping.py:1` — `# coding=utf-8`

### I001 — import block unsorted

- `otlmow_model/OtlmowModel/Classes/Abstracten/AOWSType.py:2` — `from ...BaseClasses.OTLObject import OTLAttribuut`
- `otlmow_model/OtlmowModel/Classes/Abstracten/Aangrijping.py:2` — `from abc import abstractmethod`

### RUF001 — ambiguous Unicode character in string

- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:102` — `definition='...lengte × totale breedte...'` (ambiguous `×` MULTIPLICATION SIGN)
- `otlmow_model/OtlmowModel/Datatypes/KlWetenschappelijkeSoortnaam.py:1080` — `label='Photinia × fraseri'` (ambiguous `×` MULTIPLICATION SIGN)

### PIE790 — unnecessary `pass`

- `otlmow_model/OtlmowModel/Classes/Abstracten/AanhorighedenBrug.py:22` — `pass`
- `otlmow_model/OtlmowModel/Classes/Abstracten/AanhorigheidKoker.py:20` — `pass`

### RUF002 — ambiguous Unicode character in docstring

- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:177` — `"""...lengte × totale breedte..."""` (ambiguous `×` MULTIPLICATION SIGN)
- `otlmow_model/OtlmowModel/Classes/Installatie/Zoutbijlaadplaats.py:11` — `"""Site in het beheer..."""` (ambiguous `'` RIGHT SINGLE QUOTATION MARK)

### N801 — class name should use CapWords

- `otlmow_model/OtlmowModel/Classes/Legacy/HY_CI.py:6` — `class HY_CI(LegacyObject):`
- `otlmow_model/OtlmowModel/Classes/Legacy/HY_GR.py:6` — `class HY_GR(LegacyObject):`

### F401 — imported but unused

- `otlmow_model/OtlmowModel/Classes/ImplementatieElement/NaampadObject.py:7` — `from ...BaseClasses.StringField import StringField`