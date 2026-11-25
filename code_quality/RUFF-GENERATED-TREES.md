# Ruff issues — generated trees (`Classes` + `Datatypes`)

Total: **2,634 errors** (2,561 auto-fixable with `--fix`).

Scope: `otlmow_model/OtlmowModel/Classes`, `otlmow_model/OtlmowModel/Datatypes`.

## Rule summary

| Rule | Count | Description |
|---|---|---|
| **UP009** | 2,557 | Remove unnecessary `# coding=utf-8` declaration |
| **I001** | 2 | Import block is un-sorted or un-formatted |
| **PLR0915** | 33 | Too many statements in function |
| **RUF001** | 30 | String contains ambiguous `×` (MULTIPLICATION SIGN) |
| **RUF002** | 6 | Docstring contains ambiguous `×` (MULTIPLICATION SIGN) |
| **N801** | 3 | Class name should use CapWords convention |
| **F401** | 1 | Imported but unused |
| **RUF100** | 1 | Unused `# noqa` directive |

## Per-rule examples

### UP009 — unnecessary UTF-8 encoding declaration

- `otlmow_model/OtlmowModel/Classes/Abstracten/AOWSType.py:1` — `# coding=utf-8`
- `otlmow_model/OtlmowModel/Classes/Abstracten/Aangrijping.py:1` — `# coding=utf-8`

### I001 — import block unsorted

- `otlmow_model/OtlmowModel/Classes/Abstracten/AOWSType.py:2` — `from ...BaseClasses.OTLObject import OTLAttribuut`
- `otlmow_model/OtlmowModel/Classes/Abstracten/Aangrijping.py:2` — `from abc import abstractmethod`

### RUF001 — ambiguous Unicode character in string

- `otlmow_model/OtlmowModel/Classes/Onderdeel/Bevestigingssteun.py:57` — `definition='...in  millimeter.'` (ambiguous NO-BREAK SPACE)
- `otlmow_model/OtlmowModel/Datatypes/KlWetenschappelijkeSoortnaam.py:1080` — `label='Photinia × fraseri'` (ambiguous `×` MULTIPLICATION SIGN)

### RUF002 — ambiguous Unicode character in docstring

- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:177` — `"""...lengte × totale breedte..."""` (ambiguous `×` MULTIPLICATION SIGN)
- `otlmow_model/OtlmowModel/Classes/Installatie/Zoutbijlaadplaats.py:11` — `"""Site in het beheer..."""` (ambiguous `'` RIGHT SINGLE QUOTATION MARK)

### N801 — class name should use CapWords

- `otlmow_model/OtlmowModel/Classes/Legacy/HY_CI.py:6` — `class HY_CI(LegacyObject):`
- `otlmow_model/OtlmowModel/Classes/Legacy/HY_GR.py:6` — `class HY_GR(LegacyObject):`

### F401 — imported but unused

- `otlmow_model/OtlmowModel/Classes/ImplementatieElement/NaampadObject.py:7` — `from ...BaseClasses.StringField import StringField`
" filePath">
/home/davidlinux/PycharmProjects/OTLMOW-Model/code_quality/RUFF-GENERATED-TREES.md

## RUF001/RUF002 locations

- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:182` — `×` (MULTIPLICATION SIGN)
- `otlmow_model/OtlmowModel/Classes/Onderdeel/Bevestigingssteun.py:123` — ` ` (NO-BREAK SPACE)
- `otlmow_model/OtlmowModel/Classes/Onderdeel/Bevestigingssteun.py:63` — ` ` (NO-BREAK SPACE)
- `otlmow_model/OtlmowModel/Classes/Onderdeel/Debietmeter.py:13` — ` ` (NO-BREAK SPACE)
- `otlmow_model/OtlmowModel/Classes/Onderdeel/UitleesapparatuurFlitscamera.py:8` — `’` (RIGHT SINGLE QUOTATION MARK)
- `otlmow_model/OtlmowModel/Datatypes/DtcAanlegBoomvorm.py:170` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/DtcAanlegBoomvorm.py:66` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/DtcHoutigeAanleg.py:150` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/DtcHoutigeAanleg.py:55` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlBatterijModelnaam.py:34` — `‐` (HYPHEN)
- `otlmow_model/OtlmowModel/Datatypes/KlBatterijModelnaam.py:36` — `‐` (HYPHEN)
- `otlmow_model/OtlmowModel/Datatypes/KlBoomGroeifase.py:26` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlBoomGroeifase.py:31` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlBoomGroeifase.py:41` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlConstructiestaalsoort.py:296` — `‘` (LEFT SINGLE QUOTATION MARK)
- `otlmow_model/OtlmowModel/Datatypes/KlDetectiecameraModelnaam.py:39` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlDetectiecameraModelnaam.py:41` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:24` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:26` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:29` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:31` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:54` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:56` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:59` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlLampTypeIVSB.py:61` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlPlooibakenType.py:21` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlPlooibakenType.py:26` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlPlooibakenType.py:31` — `–` (EN DASH)
- `otlmow_model/OtlmowModel/Datatypes/KlTypeBrugligger.py:26` — `’` (RIGHT SINGLE QUOTATION MARK)


### PLR0915 — too many statements in function

- `otlmow_model/OtlmowModel/Classes/Abstracten/BekledingComponent.py:18` — function with too many statements
- `otlmow_model/OtlmowModel/Classes/Abstracten/Buis.py:34` — function with too many statements

### RUF100 — unused `# noqa` directive

- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:107` — unused `# noqa`
- `otlmow_model/OtlmowModel/Classes/Installatie/Koker.py:182` — unused `# noqa`
