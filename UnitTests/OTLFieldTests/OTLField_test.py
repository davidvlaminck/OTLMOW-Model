"""Characterisation tests for ``otlmow_model.OtlmowModel.BaseClasses.OTLField.validate``.

These tests pin the existing behaviour of the complex-datatype validator before any
refactor (see code_quality/REFACTOR_LOG.md cycle 5).
"""

import pytest

from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField


class _LeafField(OTLField):
    """A field whose ``validate`` always accepts its value."""

    @classmethod
    def validate(cls, value, attribuut):
        return True


class _ComplexAttr:
    """Duck-typed stand-in for one attribute of a complex (waardeObject) value."""

    def __init__(self, waarde, kardinaliteit_max='1'):
        self.waarde = waarde
        self.kardinaliteit_max = kardinaliteit_max
        self.field = _LeafField()


class _ComplexField(OTLField):
    """A field that wraps a complex (waardeObject) datatype."""

    waardeObject = _ComplexAttr


class _FieldAttribuut:
    """Duck-typed stand-in for an OTLAttribuut."""

    def __init__(self, field, object_uri='https://example.com#T'):
        self.field = field
        self.objectUri = object_uri


def test_validate_returns_none_without_waarde_object():
    attribute = _FieldAttribuut(OTLField())
    assert OTLField.validate('whatever', attribute) is None


def test_validate_list_of_wrong_type_raises():
    attribute = _FieldAttribuut(_ComplexField())
    with pytest.raises(ValueError, match='is a complex datatype'):
        OTLField.validate(['not-a-complex-attr'], attribute)


def test_validate_single_wrong_type_raises():
    attribute = _FieldAttribuut(_ComplexField())
    with pytest.raises(ValueError, match='is a complex datatype'):
        OTLField.validate('not-a-complex-attr', attribute)


def test_validate_complex_list_of_valid_attributes():
    attribute = _FieldAttribuut(_ComplexField())
    assert OTLField.validate([_ComplexAttr('a'), _ComplexAttr('b')], attribute) is True


def test_validate_complex_list_with_invalid_attribute():
    attribute = _FieldAttribuut(_ComplexField())

    class _FailingLeafField(OTLField):
        @classmethod
        def validate(cls, value, attribuut):
            return False

    bad_attr = _ComplexAttr('a')
    bad_attr.field = _FailingLeafField()
    assert OTLField.validate([bad_attr], attribute) is False


def test_validate_list_item_none_is_skipped():
    attribute = _FieldAttribuut(_ComplexField())
    assert OTLField.validate([_ComplexAttr(None)], attribute) is True


def test_validate_cardinality_list_with_invalid_item():
    attribute = _FieldAttribuut(_ComplexField())

    class _FailingLeafField(OTLField):
        @classmethod
        def validate(cls, value, attribuut):
            return False

    bad_attr = _ComplexAttr('a', kardinaliteit_max='*')
    bad_attr.field = _FailingLeafField()
    bad_attr.waarde = ['x']
    assert OTLField.validate([bad_attr], attribute) is False
