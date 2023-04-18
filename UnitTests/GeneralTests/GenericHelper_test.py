import pytest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestClasses.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Helpers.GenericHelper import get_titlecase_from_ns
from otlmow_model.Helpers.OTLObjectHelper import count_assets_by_type, remove_duplicates_in_iterable_based_on_property


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


def test_get_titlecase_from_ns(subtests):
    for ns_input, expected_output in {
        'ABSTRACTEN': 'Abstracten',
        'abstracten': 'Abstracten',
        'implementatieelement': 'ImplementatieElement',
        'installatie': 'Installatie',
        'levenscyclus': 'Levenscyclus',
        'onderdeel': 'Onderdeel',
        'proefenmeting': 'ProefEnMeting'
    }.items():
        with subtests.test(msg=f'testing {ns_input}, expecting {expected_output}'):
            assert get_titlecase_from_ns(ns_input) == expected_output

    with subtests.test(msg=f'unknown value'):
        with pytest.raises(ValueError):
            get_titlecase_from_ns('wrong input')
