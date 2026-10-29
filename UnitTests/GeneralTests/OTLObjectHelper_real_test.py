"""Characterisation tests for the real package's ``Helpers/OTLObjectHelper.py``.

The existing ``OTLObjectHelper_test.py`` imports the *vendored copy* of the
model (``UnitTests/TestModel``), so the real module never ends up in the
coverage report and the quality gate cannot see it
(``code_quality/README.md`` §7: "a file that is not measured is a hole in the
gate, not a clean file").

These tests import the real package, so the real module is measured from now on.
"""

import base64

import pytest
from otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.OtlmowModel.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.OtlmowModel.Helpers.GenericHelper import get_aim_id_from_uuid_and_typeURI
from otlmow_model.OtlmowModel.Helpers.OTLObjectHelper import (
    compare_two_lists_of_objects_attribute_level,
    compare_two_lists_of_objects_object_level,
    count_assets_by_type,
    custom_dict_diff,
    is_aim_id,
    is_directional_relation,
    is_relation,
    print_overview_assets,
    remove_duplicates_in_iterable_based_on_property,
    verify_asset_id_is_unique_within_list,
)

BEVESTIGING_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging'
UUID = '12345678-1234-1234-1234-123456789012'


class _Simple(OTLObject):
    typeURI = 'https://example.com#Simple'

    def __init__(self):
        super().__init__()
        self._naam = OTLAttribuut(
            field=StringField, naam='naam', label='naam', objectUri='https://example.com#T.naam', owner=self
        )

    @property
    def naam(self):
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)


class _WithList(OTLObject):
    typeURI = 'https://example.com#WithList'

    @property
    def items(self):
        return [1, 2]


def test_count_assets_by_type():
    assets = [Bevestiging(), Bevestiging(), Voedt()]
    result = count_assets_by_type(assets)
    assert result[BEVESTIGING_URI] == 2


def test_remove_duplicates_in_iterable_based_on_property():
    first = _Simple()
    first.naam = '1'
    second = _Simple()
    second.naam = '1'
    third = _Simple()
    third.naam = '2'

    result = remove_duplicates_in_iterable_based_on_property([first, second, third], 'naam')
    assert result == [first, third]


def test_remove_duplicates_in_iterable_based_on_property_ignores_unknown_properties():
    asset = _Simple()
    assert remove_duplicates_in_iterable_based_on_property([asset], 'does_not_exist') == []


def test_remove_duplicates_in_iterable_based_on_property_raises_on_a_list():
    with pytest.raises(NotImplementedError, match='when the property value is a list'):
        remove_duplicates_in_iterable_based_on_property([_WithList()], 'items.value')


def test_verify_asset_id_is_unique_within_list():
    dict_list = [{'assetId': {'identificator': '1'}}, {'assetId': {'identificator': '2'}}]
    assert verify_asset_id_is_unique_within_list(dict_list) is True


def test_verify_asset_id_is_unique_within_list_with_a_none_identificator():
    with pytest.raises(ValueError, match='This list has a None value for assetId'):
        verify_asset_id_is_unique_within_list([{'assetId': {'identificator': None}}])


def test_verify_asset_id_is_unique_within_list_with_duplicates():
    with pytest.raises(ValueError, match="non-unique assetId's"):
        verify_asset_id_is_unique_within_list(
            [{'assetId': {'identificator': '1'}}, {'assetId': {'identificator': '1'}}]
        )


def test_custom_dict_diff_of_new_and_changed_keys():
    assert custom_dict_diff({}, {'a': 1}) == {'a': 1}
    assert custom_dict_diff({'a': 1}, {}) == {}
    assert custom_dict_diff({'a': 1, 'c': 3}, {'a': 1, 'b': 2}) == {'b': 2}
    assert custom_dict_diff({'a': 1, 'b': 2}, {'a': 1, 'c': 3}) == {'c': 3}


def test_custom_dict_diff_of_nested_dicts():
    assert custom_dict_diff({'a': {'a1': 1}}, {'a': {'a1': 1, 'a2': 2}}) == {'a': {'a2': 2}}
    assert custom_dict_diff({'a': {'a1': 1, 'a2': 2}}, {'a': {'a1': 1}}) == {}


def test_custom_dict_diff_of_lists():
    assert custom_dict_diff({'a': [1, 2]}, {'a': [1]}) == {'a': [1]}
    assert custom_dict_diff({'a': [1]}, {'a': [1, 2]}) == {'a': [1, 2]}


def test_compare_two_lists_of_objects_attribute_level_with_identical_assets():
    first = Bevestiging()
    first.assetId.identificator = '1'
    second = Bevestiging()
    second.assetId.identificator = '1'

    result = compare_two_lists_of_objects_attribute_level([first], [second])
    assert result == []


def test_compare_two_lists_of_objects_attribute_level_with_a_missing_asset():
    first = Bevestiging()
    first.assetId.identificator = '1'
    second = Bevestiging()
    second.assetId.identificator = '2'

    result = compare_two_lists_of_objects_attribute_level([first], [second])
    assert len(result) == 1
    assert result[0].assetId.identificator == '2'


def test_is_relation():
    assert is_relation(Bevestiging()) is True
    assert is_relation(Voedt()) is True


def test_is_directional_relation():
    assert is_directional_relation(Voedt()) is True
    assert is_directional_relation(Bevestiging()) is False


def test_is_aim_id_of_a_known_class():
    aim_id = get_aim_id_from_uuid_and_typeURI(UUID, BEVESTIGING_URI)
    assert is_aim_id(aim_id) is True


def test_is_aim_id_of_the_agent():
    aim_id = get_aim_id_from_uuid_and_typeURI(UUID, 'http://purl.org/dc/terms/Agent')
    assert is_aim_id(aim_id) is True


def test_is_aim_id_of_an_unknown_class_warns():
    aim_id = get_aim_id_from_uuid_and_typeURI(
        UUID, 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DoesNotExistClass'
    )
    with pytest.warns(ImportWarning):
        assert is_aim_id(aim_id) is False


def test_is_aim_id_with_an_invalid_guid():
    encoded = base64.b64encode(b'onderdeel#Bevestiging').decode('ascii').rstrip('=')
    assert is_aim_id(f'X2345678-1234-1234-1234-123456789012-{encoded}') is False


def test_is_aim_id_with_a_short_uri_without_a_hash():
    encoded = base64.b64encode(b'noHashHere').decode('ascii').rstrip('=')
    assert is_aim_id(f'{UUID}-{encoded}') is False


@pytest.mark.parametrize(
    'aim_id',
    [
        '',
        '12345678-1234-1234-1234-123456789012',
        '12345678-1234-1234-1234-123456789012-',
        '1',
        '12345678-1234-1234-1234-123456789012-25kZXJkZWVsI1RMQ2ZpUG9vcnQ',
    ],
)
def test_is_aim_id_of_an_invalid_aim_id(aim_id):
    assert is_aim_id(aim_id) is False


def test_print_overview_assets(capsys):
    print_overview_assets([Bevestiging(), Bevestiging()])
    captured = capsys.readouterr()
    assert f'counting 2 assets of type {BEVESTIGING_URI}' in captured.out


def test_compare_two_lists_of_objects_object_level_returns_the_new_assets():
    first = Bevestiging()
    first.assetId.identificator = '1'
    second = Bevestiging()
    second.assetId.identificator = '2'

    result = compare_two_lists_of_objects_object_level([first], [second])
    assert len(result) == 1
    assert result[0].assetId.identificator == '2'


def test_compare_two_lists_of_objects_object_level_returns_nothing_for_equal_assets():
    first = Bevestiging()
    first.assetId.identificator = '1'
    second = Bevestiging()
    second.assetId.identificator = '1'

    assert compare_two_lists_of_objects_object_level([first], [second]) == []


def test_is_directional_relation_of_an_object_that_is_not_a_relation():
    assert is_directional_relation(_Simple()) is False
