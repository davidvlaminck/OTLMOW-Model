# Ruff issues — generated trees (`Classes` + `Datatypes`)

Total: **4,895 errors** (3,439 auto-fixable with `--fix`).

Scope: `otlmow_model/OtlmowModel/Classes`, `otlmow_model/OtlmowModel/Datatypes`.

## Rule summary

| Rule | Count | Description |
|---|---|---|
| **UP009** | 2,557 | Remove unnecessary `object` base class |
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

### UP009 — unnecessary `object` base class

- `otlmow_model/OtlmowModel/Classes/Abstracten/AOWSType.py:1` — `# coding=utf-8`
- `otlmow_model/OtlmowModel/Classes/Abstracten/Aangrijping.py:1` — `# coding=utf-8`

### RUF012 — mutable class attribute

- `otlmow_model/OtlmowModel/Datatypes/AntiParkeerpaalType.py:15` — `options = {`
- `otlmow_model/OtlmowModel/Datatypes/KLLuidsprekerVormgeving.py:14` — `options = {`

### I001 — import block unsorted

- `otlmow_model/OtlmowModel/Classes/Abstracten/AOWSType.py:2` — `from ...BaseClasses.OTLObject import OTLAttribuut`
- `otlmow_model/OtlmowModel/Classes/Abstracten/Aangrijping.py:2` — `from abc import abstractmethod`

### A003 — builtin shadowed by class method

- `otlmow_model/OtlmowModel/Classes/ImplementatieElement/Bijlage.py:38` — `@type.setter`

### UP006 — use `list` instead of `List`

- `otlmow_model/OtlmowModel/Classes/Abstracten/AfschermendeConstructie.py:162` — `def testrapport(self) -> List[DtcDocumentWaarden]:`
- `otlmow_model/OtlmowModel/Classes/Abstracten/AfschermendeConstructie.py:180` — `def video(self) -> List[DtcDocumentWaarden]:`

### UP035 — import from `collections.abc`

- `otlmow_model/OtlmowModel/Classes/Abstracten/AfschermendeConstructie.py:2` — `from typing import List`
- `otlmow_model/OtlmowModel/Classes/Abstracten/AfwijkendeKantopsluiting.py:2` — `from typing import List`

### Q003 — quotes to avoid escaping

- `otlmow_model/OtlmowModel/Datatypes/KlFiguratieCode.py:126` — `'PL-A\'': KeuzelijstWaarde(invulwaarde='PL-A\'',`
- `otlmow_model/OtlmowModel/Datatypes/KlFiguratieCode.py:126` — `'PL-A\'': KeuzelijstWaarde(invulwaarde='PL-A\'',`

### PLR0915 — too many statements

- `otlmow_model/OtlmowModel/Classes/Abstracten/BegroeidVoorkomen.py:22` — `def __init__(self):`
- `otlmow_model/OtlmowModel/Classes/Abstracten/Behuizing.py:18` — `def __init__(self):`

### RUF001 — ambiguous multiplication sign in string

- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:102` — `definition='...lengte × totale breedte...'`
- `otlmow_model/OtlmowModel/Classes/Onderdeel/Bevestigingssteun.py:57` — `definition='De lengte van de bevestigingssteun in  millimeter.'`

### PIE790 — unnecessary `pass`

- `otlmow_model/OtlmowModel/Classes/Abstracten/AanhorighedenBrug.py:22` — `pass`
- `otlmow_model/OtlmowModel/Classes/Abstracten/AanhorigheidKoker.py:20` — `pass`

### Q004 — unnecessary escape on inner quote

- `otlmow_model/OtlmowModel/Datatypes/KlFiguratieCode.py:127` — `label="PL-A\'",`
- `otlmow_model/OtlmowModel/Datatypes/KlFiguratieCode.py:137` — `label="PL-B1\'",`

### PLC2401 — non-ASCII function name

- `otlmow_model/OtlmowModel/Classes/ProefEnMeting/ProefZichtbaarheidBijDagOfWV.py:31` — `def luminantiecoëfficiënt(self) -> float:`
- `otlmow_model/OtlmowModel/Classes/ProefEnMeting/ProefZichtbaarheidBijDagOfWV.py:36` — `def luminantiecoëfficiënt(self, value):`

### RUF002 — ambiguous multiplication sign in docstring

- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:177` — `"""...lengte × totale breedte..."""`
- `otlmow_model/OtlmowModel/Classes/Installatie/Zoutbijlaadplaats.py:11` — `"""Site in het beheer..."""`

### F811 — redefinition of unused name

- `otlmow_model/OtlmowModel/Classes/Abstracten/DNB.py:3` — `from datetime import date, date, date`
- `otlmow_model/OtlmowModel/Classes/Abstracten/DNB.py:3` — `from datetime import date, date, date`

### N801 — class name should use CapWords

- `otlmow_model/OtlmowModel/Classes/Legacy/HY_CI.py:6` — `class HY_CI(LegacyObject):`
- `otlmow_model/OtlmowModel/Classes/Legacy/HY_GR.py:6` — `class HY_GR(LegacyObject):`

### F401 — imported but unused

- `otlmow_model/OtlmowModel/Classes/ImplementatieElement/NaampadObject.py:7` — `from ...BaseClasses.StringField import StringField`