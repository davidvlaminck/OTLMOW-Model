import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.OtlmowModel.Helpers.OTLObjectHelper import count_assets_by_type, remove_duplicates_in_iterable_based_on_property, \
    compare_two_lists_of_objects_object_level, verify_asset_id_is_unique_within_list, compare_two_lists_of_objects_attribute_level, custom_dict_diff


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
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_get_diff_from_two_lists_one_one():
    instance = AllCasesTestClass()
    list_one = [instance]
    list_two = [instance]

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_get_diff_from_two_lists_one_one_using_dict():
    d = {'toestand': 'in-gebruik'}
    list_one = [AllCasesTestClass.from_dict(d, model_directory='UnitTests.TestClasses')]
    list_two = [AllCasesTestClass.from_dict(d, model_directory='UnitTests.TestClasses')]

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_get_diff_from_two_lists_one_two():
    instance = AllCasesTestClass()
    list_one = [instance]
    list_two = [instance, instance]

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_get_diff_from_two_lists_one_empty():
    instance = AllCasesTestClass()
    list_one = [instance]
    list_two = []

    expected = []
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_get_diff_from_two_lists_one_one_different():
    instance = AllCasesTestClass()
    list_one = [instance]
    instance2 = AllCasesTestClass()
    instance2.toestand = 'in-gebruik'
    list_two = [instance2]

    expected = [instance2]
    result = compare_two_lists_of_objects_object_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_verify_asset_id_is_unique_correct_dict_list():
    dict_list = [{'assetId': {'identificator': '1'}}, {'assetId': {'identificator': '2'}}]
    assert verify_asset_id_is_unique_within_list(dict_list)


def test_verify_asset_id_is_unique_incorrect_dict_lists(subtests):
    with subtests.test(msg='not unique ids'):
        with pytest.raises(ValueError):
            verify_asset_id_is_unique_within_list([{'assetId': {'identificator': '1'}}, {'assetId': {'identificator': '1'}}])
    with subtests.test(msg='None in asset id'):
        with pytest.raises(ValueError):
            verify_asset_id_is_unique_within_list([{'assetId': {'identificator': None}}])


def test_compare_two_lists_return_minimal_identical_objects():
    d = {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}}
    list_one = [AllCasesTestClass.from_dict(d, model_directory='UnitTests.TestClasses')]
    list_two = [AllCasesTestClass.from_dict(d, model_directory='UnitTests.TestClasses')]

    expected = []
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_compare_two_lists_return_minimal_missing_object():
    d = {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}}
    list_one = []
    list_two = [AllCasesTestClass.from_dict(d, model_directory='UnitTests.TestClasses')]

    expected = [AllCasesTestClass.from_dict(d, model_directory='UnitTests.TestClasses')]
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_compare_two_lists_return_minimal_changed_attribute():
    d1 = {'toestand': 'gepland', 'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_one = [AllCasesTestClass.from_dict(d1, model_directory='UnitTests.TestClasses')]
    d2 = {'toestand': 'in-gebruik', 'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_two = [AllCasesTestClass.from_dict(d2, model_directory='UnitTests.TestClasses')]

    expected = [AllCasesTestClass.from_dict(
        {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}},
        model_directory='UnitTests.TestClasses')]
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory='UnitTests.TestClasses')
    assert result == expected


def test_compare_two_lists_return_minimal_missing_attribute():
    d1 = {'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_one = [AllCasesTestClass.from_dict(d1, model_directory='UnitTests.TestClasses')]
    d2 = {'toestand': 'in-gebruik', 'geometry': 'POINT Z (200000 200000 0)', 'assetId': {'identificator': '1'}}
    list_two = [AllCasesTestClass.from_dict(d2, model_directory='UnitTests.TestClasses')]

    expected = [AllCasesTestClass.from_dict(
        {'toestand': 'in-gebruik', 'assetId': {'identificator': '1'}},
        model_directory='UnitTests.TestClasses')]
    result = compare_two_lists_of_objects_attribute_level(list_one, list_two, model_directory='UnitTests.TestClasses')
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


