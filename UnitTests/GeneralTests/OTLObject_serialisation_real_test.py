"""Characterisation tests for the real package's OTLObject serialisation.

These tests import from the real ``otlmow_model.OtlmowModel.BaseClasses`` modules
(hand-written, stable) and construct minimal ``OTLObject`` subclasses inline, so
they do not depend on the generated ``Classes``/``Datatypes`` trees.

Purpose: cover the four serialisation functions of ``OTLObject.py`` that are
almost untested on the real package (``_recursive_create_dict_from_asset``,
``_recursive_create_rdf_dict_from_asset``, ``set_value_by_dictitem``,
``_make_string_version_from_dict``) before that file is refactored in iteration 3
(code_quality/HANDOFF.md §7, refactor needs a characterisation test first).
"""

from datetime import date, datetime, time
from typing import ClassVar

import pytest
from otlmow_model.OtlmowModel.BaseClasses.AssetSerialisation import _make_string_version_from_dict
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from otlmow_model.OtlmowModel.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import (
    OTLAttribuut,
    OTLObject,
    clean_dict,
    create_dict_from_asset,
    set_value_by_dictitem,
)
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.BaseClasses.TimeField import TimeField
from otlmow_model.OtlmowModel.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.Exceptions.NonStandardAttributeWarning import NonStandardAttributeWarning


def _attr(field, naam, object_uri=None, owner=None, clearing_value=None, **kwargs):
    if object_uri is None:
        object_uri = 'https://example.com#T.' + naam
    if clearing_value is not None:
        field.clearing_value = clearing_value
    return OTLAttribuut(field=field, naam=naam, label=naam, objectUri=object_uri, owner=owner, **kwargs)


class _Simple(OTLObject):
    typeURI = 'https://example.com#Simple'

    def __init__(self):
        super().__init__()
        self._dt = _attr(DateTimeField, 'dt', owner=self)
        self._d = _attr(DateField, 'd', owner=self)
        self._tm = _attr(TimeField, 'tm', owner=self)
        self._dec = _attr(FloatOrDecimalField, 'dec', owner=self)
        self._i = _attr(IntegerField, 'i', owner=self)
        self._b = _attr(BooleanField, 'b', owner=self)
        self._s = _attr(StringField, 's', owner=self)


class _DocWaarden(WaardenObject):
    def __init__(self):
        self._parent = None
        self._is_waarden_object = True
        self._bestandsnaam = _attr(StringField, 'bestandsnaam', owner=self)


class _DtcDoc(ComplexField):
    waardeObject = _DocWaarden


class _Complex(OTLObject):
    typeURI = 'https://example.com#Complex'

    def __init__(self):
        super().__init__()
        self._doc = _attr(_DtcDoc, 'doc', owner=self)
        self._docs = _attr(_DtcDoc, 'docs', owner=self, kardinaliteit_max='*')


class _Union(OTLObject):
    typeURI = 'https://example.com#Union'

    def __init__(self):
        super().__init__()
        self._u = _attr(UnionTypeField, 'u', owner=self)
        self._u.options = {
            'a': KeuzelijstWaarde(invulwaarde='a', objectUri='https://example.com#a'),
            'b': KeuzelijstWaarde(invulwaarde='b', objectUri='https://example.com#b'),
        }


class _KwantWrdWaarden(WaardenObject):
    def __init__(self):
        self._parent = None
        self._is_waarden_object = True
        self._waarde = _attr(StringField, 'waarde', owner=self)

    @property
    def waarde(self):
        return self._waarde.get_waarde()


class _KwantWrdField(ComplexField):
    waarde_shortcut_applicable = True
    waardeObject = _KwantWrdWaarden


class _Keuzelijst(KeuzelijstField):
    options: ClassVar[dict] = {'a': KeuzelijstWaarde(invulwaarde='a', objectUri='https://example.com#a')}


class _Shortcut(OTLObject):
    typeURI = 'https://example.com#Shortcut'

    def __init__(self):
        super().__init__()
        self._kw = _attr(_KwantWrdField, 'kw', owner=self)
        self._kws = _attr(_KwantWrdField, 'kws', owner=self, kardinaliteit_max='*')


def test_create_dict_simple_native_types():
    instance = _Simple()
    instance._dt.waarde = datetime(2022, 2, 2, 12, 30, 30)
    instance._d.waarde = date(2022, 2, 2)
    instance._tm.waarde = time(12, 30, 30)
    instance._dec.waarde = 1.5
    instance._i.waarde = 1
    instance._b.waarde = True
    instance._s.waarde = 'hi'

    d = create_dict_from_asset(instance)
    assert d == {
        'dt': datetime(2022, 2, 2, 12, 30, 30),
        'd': date(2022, 2, 2),
        'tm': time(12, 30, 30),
        'dec': 1.5,
        'i': 1,
        'b': True,
        's': 'hi',
        'typeURI': 'https://example.com#Simple',
    }

    d = create_dict_from_asset(instance, cast_datetime=True)
    assert d['dt'] == '2022-02-02T12:30:30'
    assert d['d'] == '2022-02-02'
    assert d['tm'] == '12:30:30'


def test_create_dict_complex_waardeobject_single():
    instance = _Complex()
    instance._doc.waarde = _DocWaarden()
    instance._doc.waarde._bestandsnaam.waarde = 'report.pdf'

    d = create_dict_from_asset(instance)
    assert d == {'doc': {'bestandsnaam': 'report.pdf'}, 'typeURI': 'https://example.com#Complex'}


def test_create_dict_complex_waardeobject_cardinality():
    instance = _Complex()
    instance._docs.waarde = []
    instance._docs.add_empty_value()
    instance._docs.waarde[0]._bestandsnaam.waarde = 'a.pdf'
    instance._docs.add_empty_value()
    instance._docs.waarde[1]._bestandsnaam.waarde = 'b.pdf'

    d = create_dict_from_asset(instance)
    assert d == {
        'docs': [{'bestandsnaam': 'a.pdf'}, {'bestandsnaam': 'b.pdf'}],
        'typeURI': 'https://example.com#Complex',
    }


def test_create_dict_union_options_rdf():
    instance = _Union()
    instance._u.field.options = {
        'a': KeuzelijstWaarde(invulwaarde='a', objectUri='https://example.com#a'),
        'b': KeuzelijstWaarde(invulwaarde='b', objectUri='https://example.com#b'),
    }
    instance._u.waarde = 'a'

    d = create_dict_from_asset(instance, rdf=True)
    assert d == {'https://example.com#T.u': 'https://example.com#a', '@type': 'https://example.com#Union'}


def test_create_dict_cleared_value():
    instance = _Simple()
    field = IntegerField()
    field.clearing_value = 88888888
    instance._i = _attr(IntegerField, 'i', owner=instance, clearing_value=88888888)
    instance._i.waarde = 1
    instance._i.mark_to_be_cleared = True

    d = create_dict_from_asset(instance)
    assert d['i'] == 88888888


def test_create_dict_empty_list_and_none():
    instance = _Simple()
    instance._s.waarde = []
    instance._i.waarde = None

    d = create_dict_from_asset(instance)
    assert d == {'s': [], 'typeURI': 'https://example.com#Simple'}


def test_create_dict_non_standard_attribute_warns():
    instance = _Simple()
    instance.non_standard_attribute = 'waarde-2'

    with pytest.warns(NonStandardAttributeWarning):
        d = create_dict_from_asset(instance)
    assert d['non_standard_attribute'] == 'waarde-2'


def test_create_dict_non_standard_attribute_not_allowed():
    instance = _Simple()
    instance.non_standard_attribute = 'waarde-2'

    with pytest.raises(ValueError):
        create_dict_from_asset(instance, allow_non_otl_conform_attributes=False)


def test_create_dict_empty_object_returns_typeuri_only():
    instance = _Simple()
    d = create_dict_from_asset(instance)
    assert d == {'typeURI': 'https://example.com#Simple'}


def test_rdf_dict_complex_and_simple():
    instance = _Complex()
    instance._doc.waarde = _DocWaarden()
    instance._doc.waarde._bestandsnaam.waarde = 'report.pdf'

    d = create_dict_from_asset(instance, rdf=True)
    assert d == {
        'https://example.com#T.doc': {'https://example.com#T.bestandsnaam': 'report.pdf'},
        '@type': 'https://example.com#Complex',
    }


def test_set_value_by_dictitem_simple():
    instance = _Simple()
    set_value_by_dictitem(instance, 's', 'new string')
    assert instance._s.waarde == 'new string'

    set_value_by_dictitem(instance, 'i', 7)
    assert instance._i.waarde == 7


def test_set_value_by_dictitem_cast_datetime():
    instance = _Simple()
    set_value_by_dictitem(instance, 'dt', '2022-02-02 12:30:30', cast_datetime=True)
    assert instance._dt.waarde == datetime(2022, 2, 2, 12, 30, 30)


def test_set_value_by_dictitem_complex_recursive():
    instance = _Complex()
    set_value_by_dictitem(instance, 'doc', {'bestandsnaam': 'nested.pdf'})
    assert instance._doc.waarde is not None
    assert instance._doc.waarde._bestandsnaam.waarde == 'nested.pdf'


def test_set_value_by_dictitem_none_instance_raises():
    with pytest.raises(ValueError, match='cannot be None'):
        set_value_by_dictitem(None, 's', 'x')  # type: ignore[arg-type]


def test_set_value_by_dictitem_empty_key_raises():
    instance = _Simple()
    with pytest.raises(ValueError, match='cannot be empty'):
        set_value_by_dictitem(instance, '', 'x')


def test_set_value_by_dictitem_non_standard_attribute_warns():
    instance = _Simple()
    with pytest.warns(NonStandardAttributeWarning):
        set_value_by_dictitem(instance, 'brand_new_attr', 'value')
    assert instance.brand_new_attr == 'value'  # type: ignore[attr-defined]


def test_set_value_by_dictitem_non_standard_attribute_not_allowed():
    instance = _Simple()
    with pytest.raises(ValueError):
        set_value_by_dictitem(instance, 'brand_new_attr', 'value', allow_non_otl_conform_attributes=False)


def test_build_string_version():
    instance = _Simple()
    instance._s.waarde = 'hi'
    instance._i.waarde = 1
    info = str(instance)
    assert info.startswith('<_Simple> object\n    typeURI : https://example.com#Simple')
    assert '    s : hi' in info
    assert '    i : 1' in info


def test_make_string_version_cleared_value_marker():
    instance = _Simple()
    field = IntegerField()
    field.clearing_value = 88888888
    instance._i = _attr(IntegerField, 'i', owner=instance, clearing_value=88888888)
    instance._i.waarde = 1
    instance._i.mark_to_be_cleared = True

    d = create_dict_from_asset(instance)
    lines = _make_string_version_from_dict(d, level=1, indent=4, prefix='    ')
    text = '\n'.join(lines)
    assert '88888888 <value_marked_to_be_cleared>' in text


def test_make_string_version_list_truncation():
    d = {'typeURI': 'https://example.com#T', 'items': [str(n) for n in range(12)]}
    lines = _make_string_version_from_dict(d, level=1, indent=4, prefix='    ')
    text = '\n'.join(lines)
    assert '(2 more items)' in text


def test_clean_dict_removes_none_and_empty():
    d = {'a': 1, 'b': None, 'c': {}, 'd': {'e': None, 'f': 2}}
    result = clean_dict(d)
    assert result == {'a': 1, 'd': {'f': 2}}


def test_create_dict_complex_list_with_cardinality():
    instance = _Complex()
    instance._docs.waarde = []
    instance._docs.add_empty_value()
    instance._docs.waarde[0]._bestandsnaam.waarde = 'a.pdf'
    instance._docs.add_empty_value()
    instance._docs.waarde[1]._bestandsnaam.waarde = 'b.pdf'

    d = create_dict_from_asset(instance)
    assert d == {
        'docs': [{'bestandsnaam': 'a.pdf'}, {'bestandsnaam': 'b.pdf'}],
        'typeURI': 'https://example.com#Complex',
    }


def test_create_dict_complex_list_rdf():
    instance = _Complex()
    instance._docs.waarde = []
    instance._docs.add_empty_value()
    instance._docs.waarde[0]._bestandsnaam.waarde = 'a.pdf'

    d = create_dict_from_asset(instance, rdf=True)
    assert d == {
        'https://example.com#T.docs': [{'https://example.com#T.bestandsnaam': 'a.pdf'}],
        '@type': 'https://example.com#Complex',
    }


def test_create_dict_complex_list_rdf_empty_is_omitted():
    instance = _Complex()
    instance._docs.waarde = []
    instance._docs.add_empty_value()

    d = create_dict_from_asset(instance, rdf=True)
    assert d == {'@type': 'https://example.com#Complex'}


def test_create_dict_shortcut_without_waarde_shortcut():
    instance = _Shortcut()
    instance._kw.add_empty_value()
    instance._kw.waarde._waarde.waarde = '12.5'

    d = create_dict_from_asset(instance)
    assert d == {'kw': {'waarde': '12.5'}, 'typeURI': 'https://example.com#Shortcut'}


def test_create_dict_shortcut_with_waarde_shortcut():
    instance = _Shortcut()
    instance._kw.add_empty_value()
    instance._kw.waarde._waarde.waarde = '12.5'

    d = create_dict_from_asset(instance, waarde_shortcut=True)
    assert d == {'kw': '12.5', 'typeURI': 'https://example.com#Shortcut'}


def test_create_dict_shortcut_list_with_waarde_shortcut():
    instance = _Shortcut()
    instance._kws.waarde = []
    instance._kws.add_empty_value()
    instance._kws.waarde[0]._waarde.waarde = '12.5'

    d = create_dict_from_asset(instance, waarde_shortcut=True)
    assert d == {'kws': ['12.5'], 'typeURI': 'https://example.com#Shortcut'}


def test_create_dict_shortcut_cleared_value():
    instance = _Shortcut()
    instance._kw.add_empty_value()
    instance._kw.waarde._waarde.mark_to_be_cleared = True

    d = create_dict_from_asset(instance, waarde_shortcut=True)
    assert d == {'kw': '88888888', 'typeURI': 'https://example.com#Shortcut'}


def test_create_dict_rdf_keuzelijst_uses_option_uri():
    instance = _Simple()
    instance._k = _attr(_Keuzelijst, 'k', owner=instance)
    instance._k.waarde = 'a'

    d = create_dict_from_asset(instance, rdf=True)
    assert d == {'https://example.com#T.k': 'https://example.com#a', '@type': 'https://example.com#Simple'}


def test_create_dict_rdf_formats_datetime_but_not_date_and_time():
    instance = _Simple()
    instance._dt.waarde = datetime(2022, 2, 2, 12, 30, 30)
    instance._d.waarde = date(2022, 2, 2)
    instance._tm.waarde = time(12, 30, 30)

    d = create_dict_from_asset(instance, rdf=True, cast_datetime=True)
    assert d['https://example.com#T.dt'] == '2022-02-02 12:30:30'
    assert d['https://example.com#T.d'] == date(2022, 2, 2)
    assert d['https://example.com#T.tm'] == time(12, 30, 30)


def test_set_value_by_dictitem_complex_list_value():
    instance = _Complex()
    set_value_by_dictitem(instance, 'docs', [{'bestandsnaam': 'a.pdf'}, {'bestandsnaam': 'b.pdf'}])
    assert instance._docs.waarde[0]._bestandsnaam.waarde == 'a.pdf'
    assert instance._docs.waarde[1]._bestandsnaam.waarde == 'b.pdf'


def test_set_value_by_dictitem_complex_dict_value_on_list():
    instance = _Complex()
    set_value_by_dictitem(instance, 'docs', {'bestandsnaam': 'a.pdf'})
    assert instance._docs.waarde[0]._bestandsnaam.waarde == 'a.pdf'


def test_set_value_by_dictitem_complex_single_dict_value():
    instance = _Complex()
    set_value_by_dictitem(instance, 'doc', {'bestandsnaam': 'a.pdf'})
    assert instance._doc.waarde._bestandsnaam.waarde == 'a.pdf'


def test_set_value_by_dictitem_shortcut_value():
    instance = _Shortcut()
    set_value_by_dictitem(instance, 'kw', '12.5', waarde_shortcut=True)
    assert instance._kw.waarde._waarde.waarde == '12.5'


def test_set_value_by_dictitem_shortcut_clearing_value():
    instance = _Shortcut()
    instance._kw.add_empty_value()
    set_value_by_dictitem(instance, 'kw', '88888888', waarde_shortcut=True)
    assert instance._kw.waarde._waarde.mark_to_be_cleared is True


def test_set_value_by_dictitem_clearing_value_clears_attribute():
    instance = _Simple()
    instance._i.waarde = 3
    set_value_by_dictitem(instance, 'i', 88888888)
    assert instance._i.waarde is None
    assert instance._i.mark_to_be_cleared is True


def test_set_value_by_dictitem_rdf_by_uri():
    instance = _Simple()
    set_value_by_dictitem(instance, 'https://example.com#T.s', 'new string', rdf=True)
    assert instance._s.waarde == 'new string'
