"""Characterisation tests for the real package's OTLObject class.

These tests import from the real ``otlmow_model.OtlmowModel.BaseClasses`` modules
(hand-written, stable) and construct minimal ``OTLObject`` subclasses inline, so
they do not depend on the generated ``Classes``/``Datatypes`` trees.

Purpose: pin the behaviour of the ``OTLObject`` class that stayed in
``BaseClasses/OTLObject.py`` after the serialisation, the attribute model and
the dynamic loader were split out (code_quality/REFACTOR_LOG.md).
"""

import pytest
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import (
    OTLObject,
    dynamic_create_instance_from_uri,
    dynamic_create_type_from_uri,
)
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from otlmow_model.OtlmowModel.Exceptions.CouldNotCreateInstanceError import CouldNotCreateInstanceError

KLIMATISATIE_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie'
AIM_OBJECT_TYPEURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI'


class _Simple(OTLObject):
    typeURI = 'https://example.com#Simple'

    def __init__(self):
        super().__init__()
        self._s = self._make_attribute('s')

    @staticmethod
    def _make_attribute(naam):
        from otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut import OTLAttribuut

        return OTLAttribuut(field=StringField, naam=naam, label=naam, objectUri=f'https://example.com#T.{naam}')


def test_setattr_typeuri_on_class_with_typeuri_raises():
    instance = _Simple()
    with pytest.raises(ValueError, match='The typeURI is an OSLOAttribute'):
        instance.typeURI = 'https://example.com#Other'


def test_setattr_typeuri_with_none_value_raises_type_error():
    class _NoTypeUri(OTLObject):
        typeURI = None

    instance = _NoTypeUri()
    with pytest.raises(TypeError):
        instance.typeURI = None


def test_setattr_other_attribute_is_allowed():
    instance = _Simple()
    instance.other = 'value'
    assert instance.other == 'value'


def test_from_dict_with_typeuri():
    instance = OTLObject.from_dict({'typeURI': KLIMATISATIE_URI})
    assert instance.typeURI == KLIMATISATIE_URI


def test_from_dict_with_rdf_typeuri():
    instance = OTLObject.from_dict({AIM_OBJECT_TYPEURI: KLIMATISATIE_URI}, rdf=True)
    assert instance.typeURI == KLIMATISATIE_URI


def test_from_dict_with_rdf_at_type_removes_at_type():
    input_dict = {'@type': KLIMATISATIE_URI}
    instance = OTLObject.from_dict(input_dict, rdf=True)
    assert instance.typeURI == KLIMATISATIE_URI
    assert '@type' not in input_dict


def test_from_dict_without_typeuri_uses_class_typeuri():
    klimatisatie = dynamic_create_type_from_uri(KLIMATISATIE_URI)
    instance = klimatisatie.from_dict({'naam': 'x'})
    assert instance.typeURI == KLIMATISATIE_URI


def test_from_dict_without_any_typeuri_raises():
    class _NoTypeUri(OTLObject):
        typeURI = None

    with pytest.raises(ValueError, match='typeURI is None'):
        _NoTypeUri.from_dict({'s': 'x'})


def test_from_dict_with_unknown_typeuri_raises():
    with pytest.raises(CouldNotCreateInstanceError):
        OTLObject.from_dict({'typeURI': 'https://example.com#Unknown'})


def test_to_dict_contains_typeuri():
    instance = _Simple()
    instance._s.waarde = 'x'
    assert instance.to_dict() == {'s': 'x', 'typeURI': 'https://example.com#Simple'}


def test_deprecated_create_dict_from_asset_warns():
    instance = _Simple()
    with pytest.warns(AttributeDeprecationWarning):
        instance.create_dict_from_asset()


def test_eq_compares_dicts():
    first = _Simple()
    second = _Simple()
    assert first == second


def test_iter_yields_attributes_sorted_by_name():
    instance = _Simple()
    assert [attr.naam for attr in instance] == ['s']


def test_repr_contains_typeuri():
    assert 'typeURI : https://example.com#Simple' in repr(_Simple())


def test_clear_value_clears_attribute():
    instance = _Simple()
    instance._s.waarde = 'x'
    instance.clear_value('s')
    assert instance._s.waarde is None


def test_clear_value_with_unknown_attribute_raises():
    with pytest.raises(ValueError, match='does not exist'):
        _Simple().clear_value('nope')


def test_clear_value_without_attribute_name_raises():
    with pytest.raises(ValueError, match='attribute_name is None'):
        _Simple().clear_value(None)


def test_fill_with_dummy_data_fills_attributes():
    instance = _Simple()
    instance.fill_with_dummy_data()
    assert instance._s.waarde is not None


def test_is_instance_of_own_class():
    assert _Simple().is_instance_of(_Simple)


def test_is_instance_of_other_class():
    assert _Simple().is_instance_of(OTLObject)


def test_is_instance_of_without_typeuri():
    class _NoTypeUri:
        pass

    assert not _Simple().is_instance_of(_NoTypeUri)


def test_return_is_otl_object():
    assert _Simple().return_is_otl_object() is True


def test_dynamic_create_instance_from_uri():
    instance = dynamic_create_instance_from_uri(KLIMATISATIE_URI)
    assert instance.typeURI == KLIMATISATIE_URI


def test_dynamic_create_instance_from_uri_unknown_raises():
    with pytest.raises(CouldNotCreateInstanceError):
        dynamic_create_instance_from_uri('https://example.com#Unknown')
