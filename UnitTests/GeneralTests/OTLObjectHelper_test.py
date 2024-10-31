from pathlib import Path

import pytest
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import create_dict_from_asset

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.OtlmowModel.Helpers.OTLObjectHelper import count_assets_by_type, \
    remove_duplicates_in_iterable_based_on_property, \
    compare_two_lists_of_objects_object_level, verify_asset_id_is_unique_within_list, \
    compare_two_lists_of_objects_attribute_level, custom_dict_diff, is_relation, is_directional_relation, \
    combine_two_asset_instances, combine_assets

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
    assert result[0].create_dict_from_asset() == expected[0].create_dict_from_asset()


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


def test_combine_two_asset_instances(subtests):
    empty = AllCasesTestClass()
    minimum = AllCasesTestClass()
    minimum.assetId.identificator = '1'
    minimum_2 = AllCasesTestClass()
    minimum_2.assetId.identificator = '1'
    minimum_3 = AllCasesTestClass()
    minimum_3.assetId.identificator = '2'
    one_attribute = AllCasesTestClass()
    one_attribute.assetId.identificator = '1'
    one_attribute.toestand = 'in-gebruik'
    two_attributes = AllCasesTestClass()
    two_attributes.assetId.identificator = '1'
    two_attributes.toestand = 'in-gebruik'
    two_attributes.testStringField = 'naam'
    two_attributes_2 = AllCasesTestClass()
    two_attributes_2.assetId.identificator = '1'
    two_attributes_2.isActief = True
    two_attributes_2.testStringField = 'naam_2'
    other_type = AnotherTestClass()
    other_type.assetId.identificator = '1'
    other_type.deprecatedString = 'deprecated'
    other_type_2 = AnotherTestClass()
    other_type_2.assetId.identificator = '1'
    other_type_2.deprecatedString = 'deprecated'

    with subtests.test(msg='empty arguments'):
        with pytest.raises(ValueError):
            combine_two_asset_instances(asset1=None, asset2=None)
        with pytest.raises(ValueError):
            combine_two_asset_instances(asset1=empty, asset2=None)

    with subtests.test(msg='empty asset identificator'):
        with pytest.raises(ValueError):
            combine_two_asset_instances(asset1=empty, asset2=minimum)
        with pytest.raises(ValueError):
            combine_two_asset_instances(asset1=minimum, asset2=empty)

    with subtests.test(msg='assets with different identificators'):
        with pytest.raises(ValueError):
            combine_two_asset_instances(asset1=minimum, asset2=minimum_3)

    with subtests.test(msg='assets that are not the same type'):
        with pytest.raises(ValueError):
            combine_two_asset_instances(asset1=minimum, asset2=other_type)

    with subtests.test(msg='assets with no attributes'):
        result = combine_two_asset_instances(asset1=minimum, asset2=minimum_2)
        assert result == minimum

    with subtests.test(msg='assets with one attribute'):
        result = combine_two_asset_instances(asset1=minimum, asset2=one_attribute)
        assert result == one_attribute

    with subtests.test(msg='assets with two attributes'):
        result = combine_two_asset_instances(asset1=two_attributes_2, asset2=two_attributes)
        assert create_dict_from_asset(result) == {
            'toestand': 'in-gebruik',
            'testStringField': 'naam',
            'isActief': True,
            'assetId': {'identificator': '1'},
            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        }

    with subtests.test(msg='assets with identical attributes'):
        result = combine_two_asset_instances(asset1=other_type, asset2=other_type_2, allow_attribute_overrides=False)

    with subtests.test(msg='assets with different attributes'):
        with pytest.raises(ValueError):
            combine_two_asset_instances(asset1=two_attributes_2, asset2=two_attributes, allow_attribute_overrides=False)

def test_combine_assets(subtests):
    asset1_1 = AllCasesTestClass()
    asset1_1.assetId.identificator = '1'
    asset1_1.testStringField = 'string 2'

    asset1_2 = AllCasesTestClass()
    asset1_2.assetId.identificator = '1'
    asset1_2.testStringField = 'string 1'

    asset1_3 = AllCasesTestClass()
    asset1_3.assetId.identificator = '1'
    asset1_3.testBooleanField = True

    asset2_1 = AllCasesTestClass()
    asset2_1.assetId.identificator = '2'
    asset2_1.testStringField = 'string 2'

    with subtests.test(msg='assets with different attribute values'):
        with pytest.raises(ValueError):
            combine_assets(asset_list=[asset1_1, asset1_2], allow_attribute_overrides=False)

    with subtests.test(msg='assets with different attribute values  without changing order 2'):
        result = combine_assets(asset_list=[asset1_1, asset1_2])
        assert result[0] == asset1_2

    with subtests.test(msg='assets with different attribute values without changing order 2'):
        result = combine_assets(asset_list=[asset1_2, asset1_1])
        assert result[0] == asset1_1

    with subtests.test(msg='three assets with different attribute values'):
        result = combine_assets(asset_list=[asset1_1, asset1_2, asset1_3])
        assert create_dict_from_asset(result[0]) == {
            'testStringField': 'string 1',
            'testBooleanField': True,
            'assetId': {'identificator': '1'},
            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        }

    with subtests.test(msg='all test assets'):
        result = combine_assets(asset_list=[asset1_1, asset1_2, asset1_3, asset2_1])
        assert create_dict_from_asset(result[0]) == {
            'testStringField': 'string 1',
            'testBooleanField': True,
            'assetId': {'identificator': '1'},
            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        }
        assert result[1] == asset2_1
