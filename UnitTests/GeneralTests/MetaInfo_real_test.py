"""Characterisation tests for the real package's ``BaseClasses/MetaInfo.py``.

The existing ``MetaInfo_test.py`` imports the *vendored copy* of the model
(``UnitTests/TestModel``), so the real module never ends up in the coverage
report and the quality gate cannot see it.

These tests import the real package, so the real module is measured from now on.
"""

from typing import ClassVar

import pytest
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde
from otlmow_model.OtlmowModel.BaseClasses.MetaInfo import meta_info
from otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject


class _Waarden(WaardenObject):
    def __init__(self):
        self._parent = None
        self._is_waarden_object = True
        self._nested = OTLAttribuut(
            field=StringField,
            naam='nested',
            label='nested',
            objectUri='https://example.com#T.nested',
            owner=self,
            kardinaliteit_min='0',
            kardinaliteit_max='*',
        )


class _Complex(ComplexField):
    waardeObject = _Waarden


class _Keuzelijst(KeuzelijstField):
    options: ClassVar[dict] = {
        f'opt{i}': KeuzelijstWaarde(
            invulwaarde=f'opt{i}',
            label=f'opt{i}',
            objectUri=f'https://example.com#{i}',
            status='uitgebruik' if i == 0 else '',
        )
        for i in range(12)
    }


class _Simple(OTLObject):
    """Docstring of the class."""

    typeURI = 'https://example.com#Simple'

    def __init__(self):
        super().__init__()
        self._naam = OTLAttribuut(
            field=StringField,
            naam='naam',
            label='naam',
            objectUri='https://example.com#T.naam',
            owner=self,
            definition='the name',
            deprecated_version='2.0.0',
        )
        self._k = OTLAttribuut(field=_Keuzelijst, naam='k', label='k', objectUri='https://example.com#T.k', owner=self)
        self._c = OTLAttribuut(field=_Complex, naam='c', label='c', objectUri='https://example.com#T.c', owner=self)


def test_meta_info_of_an_object():
    result = meta_info(_Simple())
    assert result == (
        'Showing metadata of _Simple:\n'
        'typeURI: https://example.com#Simple\n'
        'definition: Docstring of the class.\n'
        'attributes:\n'
        '    c (type: )\n'
        '    k (type: )\n'
        '    naam (type: String) <deprecated since 2.0.0>'
    )


def test_meta_info_of_an_attribute():
    result = meta_info(_Simple(), attribute='naam')
    assert result == (
        'Showing metadata of naam:\ntypeURI: https://example.com#T.naam\ndefinition: the name\ndeprecated since 2.0.0'
    )


def test_meta_info_of_a_keuzelijst_attribute():
    result = meta_info(_Simple(), attribute='k')
    assert result.startswith('Showing metadata of k:\ntypeURI: https://example.com#T.k\ndefinition: \nvalid values:\n')
    assert '    opt0 (waarde uit gebruik!)\n' in result
    assert '    opt9\n' in result
    assert '    ...\nFor the full list, review the class' in result
    assert 'opt10' not in result


def test_meta_info_of_a_complex_attribute():
    result = meta_info(_Simple(), attribute='c')
    assert result == (
        'Showing metadata of c:\n'
        'typeURI: https://example.com#T.c\n'
        'definition: \n'
        'attributes:\n'
        '    nested (type: String, cardinality: 0-*)'
    )


def test_meta_info_of_a_nested_attribute():
    result = meta_info(_Simple(), attribute='c.nested')
    assert result == ('Showing metadata of nested:\ntypeURI: https://example.com#T.nested\ndefinition: ')


def test_meta_info_of_an_unknown_attribute_raises():
    with pytest.raises(ValueError, match="'does_not_exist' does not exist"):
        meta_info(_Simple(), attribute='does_not_exist')


def test_meta_info_of_an_unknown_nested_attribute_raises():
    # the error names the part of the path that could not be resolved
    with pytest.raises(ValueError, match="'does_not_exist' does not exist"):
        meta_info(_Simple(), attribute='c.does_not_exist')


def test_meta_info_of_an_object_without_metadata_returns_none():
    assert meta_info(object()) is None
