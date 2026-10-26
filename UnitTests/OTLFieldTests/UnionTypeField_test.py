"""Characterisation tests for ``otlmow_model.OtlmowModel.BaseClasses.UnionTypeField.validate``.

These tests pin the existing behaviour of the union-type validator before any
refactor (see code_quality/REFACTOR_LOG.md cycle 5).
"""

import pytest

from otlmow_model.OtlmowModel.BaseClasses.OTLField import OTLField
from otlmow_model.OtlmowModel.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.OtlmowModel.Exceptions.UnionTypeError import UnionTypeError


class _LeafField(OTLField):
    """A field whose ``validate`` always accepts its value."""

    @classmethod
    def validate(cls, value, attribuut):
        return True


class _FailingLeafField(OTLField):
    """A field whose ``validate`` always rejects its value."""

    @classmethod
    def validate(cls, value, attribuut):
        return False


class _RaisingLeafField(OTLField):
    """A field whose ``validate`` raises instead of returning a boolean."""

    @classmethod
    def validate(cls, value, attribuut):
        raise ValueError('boom')


class _UnionMemberAttr:
    """Duck-typed stand-in for one member attribute of a union value."""

    def __init__(self, waarde, field):
        self.waarde = waarde
        self.field = field


def _union_waarden_class(member_field):
    """A waardeObject class whose instances expose ``_a`` and ``_b`` member attributes."""

    def init(self):
        self._a = _UnionMemberAttr('a-value', member_field)
        self._b = _UnionMemberAttr('b-value', member_field)

    return type('_UnionWaarden', (), {'__init__': init})


class _FieldAttribuut:
    """Duck-typed stand-in for an OTLAttribuut."""

    def __init__(self, field, object_uri='https://example.com#T', naam='test'):
        self.field = field
        self.objectUri = object_uri
        self.naam = naam


def _union_field(member_field):
    field = UnionTypeField()
    field.waardeObject = _union_waarden_class(member_field)
    return field


def test_validate_none_is_valid():
    attribute = _FieldAttribuut(_union_field(_LeafField()))
    assert UnionTypeField.validate(None, attribute) is True


def test_validate_waarde_object_instance_is_valid():
    attribute = _FieldAttribuut(_union_field(_LeafField()))
    instance = _union_field(_LeafField()).waardeObject()
    assert UnionTypeField.validate(instance, attribute) is True


def test_validate_matching_member_is_valid():
    attribute = _FieldAttribuut(_union_field(_LeafField()))
    assert UnionTypeField.validate('a-value', attribute) is True


def test_validate_no_matching_member_raises_union_type_error():
    attribute = _FieldAttribuut(_union_field(_FailingLeafField()))
    with pytest.raises(UnionTypeError):
        UnionTypeField.validate('nope', attribute)


def test_validate_raising_member_field_raises_union_type_error():
    attribute = _FieldAttribuut(_union_field(_RaisingLeafField()))
    with pytest.raises(UnionTypeError):
        UnionTypeField.validate('x', attribute)
