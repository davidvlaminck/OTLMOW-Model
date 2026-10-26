"""Characterisation tests for the real package's ``BaseClasses/LegacyObject.py``.

The name fields of a legacy object are only used by the legacy classes, so they
had no test at all: their coverage was 62.5 % and their CRAP score 6.3.
"""

from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import NaamField, NaampadField


class _Owner:
    def __init__(self, naam=None, naampad=None):
        self.naam = naam
        self.naampad = naampad


class _Attribuut:
    def __init__(self, owner):
        self.owner = owner
        self.naam = 'naam'


def test_naam_field_validates_a_valid_name():
    assert NaamField.validate('valid-name', _Attribuut(_Owner())) is True


def test_naam_field_rejects_an_invalid_name():
    assert NaamField.validate('invalid name', _Attribuut(_Owner())) is False


def test_naam_field_rejects_a_name_that_does_not_match_the_naampad():
    attribuut = _Attribuut(_Owner(naampad='some/path/different-name'))
    assert NaamField.validate('other-name', attribuut) is False


def test_naam_field_accepts_a_name_that_matches_the_naampad():
    attribuut = _Attribuut(_Owner(naampad='some/path/the-name'))
    assert NaamField.validate('the-name', attribuut) is True


def test_naam_field_accepts_a_name_without_a_naampad():
    attribuut = _Attribuut(_Owner())
    assert NaamField.validate('the-name', attribuut) is True


def test_naampad_field_validates_a_valid_naampad():
    assert NaampadField.validate('some/path', _Attribuut(_Owner(naam='path'))) is True


def test_naampad_field_rejects_an_invalid_naampad():
    assert NaampadField.validate('some path', _Attribuut(_Owner(naam='path'))) is False


def test_naampad_field_rejects_a_naampad_that_does_not_match_the_name():
    attribuut = _Attribuut(_Owner(naam='other-name'))
    assert NaampadField.validate('some/path', attribuut) is False


def test_naampad_field_accepts_a_naampad_without_a_name():
    assert NaampadField.validate('some/path', _Attribuut(_Owner())) is True
