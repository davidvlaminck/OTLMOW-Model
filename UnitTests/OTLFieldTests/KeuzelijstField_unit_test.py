"""Characterisation tests for ``otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField``.

These tests pin the existing behaviour of ``validate`` and
``convert_to_invulwaarde`` before any refactor (see code_quality/REFACTOR_LOG.md
cycle 6). Kept under a unique basename to avoid clashing with the module of the
same name in ``UnitTests/OTLAttribuutTests``.
"""

import pytest

from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde
from otlmow_model.OtlmowModel.Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from otlmow_model.OtlmowModel.Exceptions.InvalidOptionError import InvalidOptionError
from otlmow_model.OtlmowModel.Exceptions.RemovedOptionError import RemovedOptionError


class _Option:
    def __init__(self, invulwaarde, label, object_uri, status):
        self.invulwaarde = invulwaarde
        self.label = label
        self.objectUri = object_uri
        self.status = status


class _Field:
    def __init__(self, options):
        self.options = options


class _Attribuut:
    def __init__(self, field, naam='test'):
        self.field = field
        self.naam = naam


def _options():
    return {
        'a': KeuzelijstWaarde('a', 'label A', '', 'https://example.com#a', 'ingebruik'),
        'b': KeuzelijstWaarde('b', 'label B', '', 'https://example.com#b', 'uitgebruik'),
        'c': KeuzelijstWaarde('c', 'label C', '', 'https://example.com#c', 'verwijderd'),
    }


def test_validate_none_is_valid():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.validate(None, _Attribuut(field)) is True


def test_validate_dash_is_valid():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.validate('-', _Attribuut(field)) is True


def test_validate_non_string_raises():
    field = KeuzelijstField()
    field.options = _options()
    with pytest.raises(TypeError, match='not the correct type'):
        KeuzelijstField.validate(123, _Attribuut(field))


def test_validate_invalid_option_raises():
    field = KeuzelijstField()
    field.options = _options()
    with pytest.raises(InvalidOptionError, match='is not a valid option'):
        KeuzelijstField.validate('nope', _Attribuut(field))


def test_validate_deprecated_option_warns_and_returns_true():
    field = KeuzelijstField()
    field.options = _options()
    with pytest.warns(AttributeDeprecationWarning, match='is a deprecated value'):
        assert KeuzelijstField.validate('b', _Attribuut(field)) is True


def test_validate_removed_option_raises():
    field = KeuzelijstField()
    field.options = _options()
    with pytest.raises(RemovedOptionError, match='is no longer a valid value'):
        KeuzelijstField.validate('c', _Attribuut(field))


def test_validate_valid_option_returns_true():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.validate('a', _Attribuut(field)) is True


def test_convert_to_invulwaarde_none():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.convert_to_invulwaarde(None, field) is None


def test_convert_to_invulwaarde_empty_string():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.convert_to_invulwaarde('', field) == ''


def test_convert_to_invulwaarde_dash():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.convert_to_invulwaarde('-', field) is None


def test_convert_to_invulwaarde_in_options():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.convert_to_invulwaarde('a', field) == 'a'


def test_convert_to_invulwaarde_by_object_uri():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.convert_to_invulwaarde('https://example.com#a', field) == 'a'


def test_convert_to_invulwaarde_by_label():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.convert_to_invulwaarde('label A', field) == 'a'


def test_convert_to_invulwaarde_no_match_returns_value():
    field = KeuzelijstField()
    field.options = _options()
    assert KeuzelijstField.convert_to_invulwaarde('unknown', field) == 'unknown'
