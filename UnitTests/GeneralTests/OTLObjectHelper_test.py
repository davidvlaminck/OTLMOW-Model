import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pathlib import Path

import pytest
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import create_dict_from_asset

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Voedt import Voedt
from UnitTests.TestModel.OtlmowModel.Helpers.OTLObjectHelper import count_assets_by_type, \
    remove_duplicates_in_iterable_based_on_property, \
    compare_two_lists_of_objects_object_level, verify_asset_id_is_unique_within_list, \
    compare_two_lists_of_objects_attribute_level, custom_dict_diff, is_relation, is_directional_relation, is_aim_id

model_directory_path = Path(__file__).parent.parent / 'TestModel'


def test_count_assets_by_type():
    assets = [Bevestiging(), AllCasesTestClass(), AllCasesTestClass(), AnotherTestClass()]
    expected_dict = {'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging': 1,
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass': 2,
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass': 1}
    assert count_assets_by_type(assets) == expected_dict


def test_remove_duplicates_in_iterable_based_on_property():
    t = AllCasesTestClass()
    t.naam = '1'
    u = AllCasesTestClass()
    u.naam = '1'
    v = AllCasesTestClass()
    v.naam = '2'
    w = AllCasesTestClass()
    testset = [t, u, v, w]
    expected_result = [t, v]
    result = remove_duplicates_in_iterable_based_on_property(testset, 'naam')

    assert result == expected_result


def test_remove_duplicates_in_iterable_based_on_complex_property():
    t = AllCasesTestClass()
    t.testComplexType.testComplexType2.testStringField = '1'
    u = AllCasesTestClass()
    u.testComplexType.testComplexType2.testStringField = '1'
    v = AllCasesTestClass()
    v.testComplexType.testComplexType2.testStringField = '2'
    testset = [t, u, v]
    expected_result = [t, v]
    result = remove_duplicates_in_iterable_based_on_property(testset,
                                                             'testComplexType.testComplexType2.testStringField')

    assert result == expected_result


def test_remove_duplicates_in_iterable_based_on_complex_property_list():
    t = AllCasesTestClass()
    t.testComplexType._testComplexType2MetKard.add_empty_value()
    t.testComplexType.testComplexType2MetKard[0].testStringField = '1'
    testset = [t]

    with pytest.raises(NotImplementedError):
        remove_duplicates_in_iterable_based_on_property(testset,
                                                        'testComplexType.testComplexType2MetKard.testStringField')


def test_get_diff_from_two_lists_empty_one():
    instance = AllCasesTestClass()
    list_one = []
    list_two = [instance]

    expected = [instance]
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_get_diff_from_two_lists_one_one():
    instance = AllCasesTestClass()
    list_one = [instance]
    list_two = [instance]

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_get_diff_from_two_lists_one_one_using_dict():
    d = {'toestand': 'in-gebruik'}
    list_one = [AllCasesTestClass.from_dict(d, model_directory=model_directory_path)]
    list_two = [AllCasesTestClass.from_dict(d, model_directory=model_directory_path)]

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_get_diff_from_two_lists_one_two():
    instance = AllCasesTestClass()
    list_one = [instance]
    list_two = [instance, instance]

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_get_diff_from_two_lists_one_empty():
    instance = AllCasesTestClass()
    list_one = [instance]
    list_two = []

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_get_diff_from_two_lists_one_one_different():
    instance = AllCasesTestClass()
    list_one = [instance]
    instance2 = AllCasesTestClass()
    instance2.toestand = 'in-gebruik'
    list_two = [instance2]

    expected = [instance2]
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory=model_directory_path)
    assert result[0].to_dict() == expected[0].to_dict()


def test_verify_asset_id_is_unique_correct_dict_list():
    dict_list = [{'assetId': {'identificator': '1'}}, {'assetId': {'identificator': '2'}}]
    assert verify_asset_id_is_unique_within_list(dict_list)


def test_verify_asset_id_is_unique_incorrect_dict_lists(subtests):
    with subtests.test(msg='not unique ids'):
        with pytest.raises(ValueError):
            verify_asset_id_is_unique_within_list(
                [{'assetId': {'identificator': '1'}}, {'assetId': {'identificator': '1'}}])
    with subtests.test(msg='None in asset id'):
        with pytest.raises(ValueError):
            verify_asset_id_is_unique_within_list([{'assetId': {'identificator': None}}])


def test_compare_two_lists_return_minimal_identical_objects():
    d = {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}}
    list_one = [AllCasesTestClass.from_dict(d, model_directory=model_directory_path)]
    list_two = [AllCasesTestClass.from_dict(d, model_directory=model_directory_path)]

    expected = []
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_compare_two_lists_return_minimal_missing_object():
    d = {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}}
    list_one = []
    list_two = [AllCasesTestClass.from_dict(d, model_directory=model_directory_path)]

    expected = [AllCasesTestClass.from_dict(d, model_directory=model_directory_path)]
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_compare_two_lists_return_minimal_changed_attribute():
    d1 = {'toestand': 'gepland', 'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_one = [AllCasesTestClass.from_dict(d1, model_directory=model_directory_path)]
    d2 = {'toestand': 'in-gebruik', 'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_two = [AllCasesTestClass.from_dict(d2, model_directory=model_directory_path)]

    expected = [AllCasesTestClass.from_dict(
        {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}},
        model_directory=model_directory_path)]
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_compare_two_lists_return_minimal_missing_attribute():
    d1 = {'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_one = [AllCasesTestClass.from_dict(d1, model_directory=model_directory_path)]
    d2 = {'toestand': 'in-gebruik', 'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_two = [AllCasesTestClass.from_dict(d2, model_directory=model_directory_path)]

    expected = [AllCasesTestClass.from_dict(
        {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}},
        model_directory=model_directory_path)]
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory=model_directory_path)
    assert result == expected


def test_custom_dict_diff():
    d1 = {}
    d2 = {'a': 1}
    result1 = custom_dict_diff(d1, d2)
    expected1 = {'a': 1}
    result2 = custom_dict_diff(d2, d1)
    expected2 = {}
    assert result1 == expected1
    assert result2 == expected2

    d1 = {'a': 1, 'c': 3}
    d2 = {'a': 1, 'b': 2}
    result1 = custom_dict_diff(d1, d2)
    expected1 = {'b': 2}
    result2 = custom_dict_diff(d2, d1)
    expected2 = {'c': 3}
    assert result1 == expected1
    assert result2 == expected2

    d1 = {'a': [1, 2]}
    d2 = {'a': [1]}
    result1 = custom_dict_diff(d1, d2)
    expected1 = {'a': [1]}
    result2 = custom_dict_diff(d2, d1)
    expected2 = {'a': [1, 2]}
    assert result1 == expected1
    assert result2 == expected2

    d1 = {'a': {'a1': 1}}
    d2 = {'a': {'a1': 1, 'a2': 2}}
    result1 = custom_dict_diff(d1, d2)
    expected1 = {'a': {'a2': 2}}
    result2 = custom_dict_diff(d2, d1)
    expected2 = {}
    assert result1 == expected1
    assert result2 == expected2

    d1 = {'a': [{'a1': 1}, {'b': 1}]}
    d2 = {'a': [{'a1': 1, 'a2': 2}, {'b': 1}, {'c': 3}]}
    result1 = custom_dict_diff(d1, d2)
    expected1 = {'a': [{'a1': 1, 'a2': 2}, {'b': 1}, {'c': 3}]}
    result2 = custom_dict_diff(d2, d1)
    expected2 = {'a': [{'a1': 1}, {'b': 1}]}
    assert result1 == expected1
    assert result2 == expected2


def test_is_relation():
    assert not is_relation(AllCasesTestClass(), model_directory=model_directory_path)
    assert is_relation(Bevestiging(), model_directory=model_directory_path)


def test_is_directional_relation():
    assert not is_directional_relation(AllCasesTestClass(), model_directory=model_directory_path)
    assert not is_directional_relation(Bevestiging(), model_directory=model_directory_path)
    assert is_directional_relation(Voedt(), model_directory=model_directory_path)


@pytest.mark.skip(reason='This test fails when run together with other tests because of '
                         'dynamic_create_asset_from_ns_and_name using sys.path')
def test_is_aim_id_invalid_warning():
    aim_id = '12345678-1234-1234-1234-123456789012-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'  # AllCasesTestClass
    with pytest.warns(ImportWarning):
        assert not is_aim_id(aim_id)


def test_is_aim_id_valid_model_directory():
    model_path = Path(__file__).parent.parent / 'TestModel'
    aim_id = '12345678-1234-1234-1234-123456789012-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'  # AllCasesTestClass
    assert is_aim_id(aim_id, model_path)


def test_is_aim_id_valid():
    aim_id = '12345678-1234-1234-1234-123456789012-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'  # AllCasesTestClass
    assert is_aim_id(aim_id)

    aim_id = '12345678-1234-1234-1234-123456789012-cHVybDpBZ2VudA' # Agent
    assert is_aim_id(aim_id)


@pytest.mark.parametrize('aim_id', [
    '12345678-1234-1234-1234-123456789012',
    '12345678-1234-1234-1234-123456789012-',
    '12345678-1234-1234-1234-123456789012--',
    '1',
    '12345678-1234-1234-1234-123456789012-25kZXJkZWVsI1RMQ2ZpUG9vcnQ' # removed one char from valid encoded typeURI
])
def test_is_aim_id_invalid(aim_id):
    assert not is_aim_id(aim_id)
