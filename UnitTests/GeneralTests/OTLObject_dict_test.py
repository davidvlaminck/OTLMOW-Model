from datetime import date, datetime, time
from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.ImplementatieElement.AIMObject import AIMObject
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject, create_dict_from_asset
from otlmow_model.OtlmowModel.Exceptions.NonStandardAttributeWarning import NonStandardAttributeWarning

model_directory_path = Path(__file__).parent.parent / 'TestModel'


def test_from_dict_typeURI_in_dict_without_model():
    input_dict = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller'}
    instance = OTLObject.from_dict(input_dict)
    assert instance is not None


def test_from_dict_typeURI_in_dict():
    input_dict = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}
    instance = OTLObject.from_dict(input_dict, model_directory=model_directory_path)
    assert instance is not None
    assert AllCasesTestClass.typeURI == instance.typeURI


def test_from_dict_rdf_typeURI_in_dict():
    input_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI':
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}
    instance = OTLObject.from_dict(input_dict, model_directory=model_directory_path, rdf=True)
    assert instance is not None
    assert AllCasesTestClass.typeURI == instance.typeURI


def test_from_dict_abstract_class_no_typeURI_in_dict():
    input_dict = {}
    with pytest.raises(ValueError):
        OTLObject.from_dict(input_dict, model_directory=model_directory_path)
    with pytest.raises(ValueError):
        AIMObject.from_dict(input_dict, model_directory=model_directory_path)


def test_from_dict_non_standard_attributes_default_func():
    with pytest.warns(NonStandardAttributeWarning):
        input_dict = {'testBooleanField': True,
                      'non_standard_attribute': True}
        instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path)
        assert instance is not None
        assert instance.is_instance_of(AllCasesTestClass)
        assert AllCasesTestClass.typeURI == instance.typeURI
        assert instance.testBooleanField
        assert instance.non_standard_attribute


def test_from_dict_non_standard_attributes_all_cases(subtests):
    input_dict = {'testBooleanField': True,
                  'non_standard_attribute': True}

    with subtests.test('allow_non_otl_conform_attributes = True and warn_for_non_otl_conform_attributes = True'):
        with pytest.warns(NonStandardAttributeWarning):
            instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path)
            assert instance is not None

    with subtests.test('allow_non_otl_conform_attributes = True and warn_for_non_otl_conform_attributes = False'):
        instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path,
                                               warn_for_non_otl_conform_attributes=False)
        assert instance is not None

    with subtests.test('allow_non_otl_conform_attributes = False'):
        with pytest.raises(ValueError):
            AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path,
                                        allow_non_otl_conform_attributes=False)


def test_from_dict_simple_single_attributes():
    input_dict = {'testBooleanField': True,
                  'testKeuzelijst': 'waarde-2',
                  'testDateField': date(2023, 1, 1),
                  'testDateTimeField': datetime(2023, 1, 1, 10, 11, 12),
                  'testTimeField': time(10, 11, 12),
                  'testDecimalField': 1.2,
                  'testIntegerField': 1,
                  'testStringField': 'test'}
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testBooleanField
    assert instance.testKeuzelijst == 'waarde-2'
    assert instance.testDateField == date(2023, 1, 1)
    assert instance.testDateTimeField == datetime(2023, 1, 1, 10, 11, 12)
    assert instance.testTimeField == time(10, 11, 12)
    assert instance.testDecimalField == 1.2
    assert instance.testIntegerField == 1
    assert instance.testStringField == 'test'


def test_from_dict_rdf_simple_single_attributes():
    input_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testBooleanField': True,
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKeuzelijst': 'waarde-2',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateField': date(2023, 1, 1),
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateTimeField': datetime(2023, 1,
                                                                                                               1, 10,
                                                                                                               11, 12),
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testTimeField': time(10, 11, 12),
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDecimalField': 1.2,
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testIntegerField': 1,
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField': 'test'}
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path, rdf=True)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testBooleanField
    assert instance.testKeuzelijst == 'waarde-2'
    assert instance.testDateField == date(2023, 1, 1)
    assert instance.testDateTimeField == datetime(2023, 1, 1, 10, 11, 12)
    assert instance.testTimeField == time(10, 11, 12)
    assert instance.testDecimalField == 1.2
    assert instance.testIntegerField == 1
    assert instance.testStringField == 'test'


def test_from_dict_simple_attributes_with_cardinality():
    input_dict = {'testDecimalFieldMetKard': [1.2, 2.3],
                  'testIntegerFieldMetKard': [1, 2],
                  'testKeuzelijstMetKard': ['waarde-1', 'waarde-2'],
                  'testStringFieldMetKard': ['1', '2']}
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testDecimalFieldMetKard[0] == 1.2
    assert instance.testDecimalFieldMetKard[1] == 2.3
    assert instance.testIntegerFieldMetKard[0] == 1
    assert instance.testIntegerFieldMetKard[1] == 2
    assert instance.testKeuzelijstMetKard[0] == 'waarde-1'
    assert instance.testKeuzelijstMetKard[1] == 'waarde-2'
    assert instance.testStringFieldMetKard[0] == '1'
    assert instance.testStringFieldMetKard[1] == '2'


def test_from_dict_rdf_simple_attributes_with_cardinality():
    input_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDecimalFieldMetKard': [1.2, 2.3],
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testIntegerFieldMetKard': [1, 2],
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKeuzelijstMetKard': ['waarde-1',
                                                                                                           'waarde-2'],
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringFieldMetKard': ['1', '2']}
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path, rdf=True)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testDecimalFieldMetKard[0] == 1.2
    assert instance.testDecimalFieldMetKard[1] == 2.3
    assert instance.testIntegerFieldMetKard[0] == 1
    assert instance.testIntegerFieldMetKard[1] == 2
    assert instance.testKeuzelijstMetKard[0] == 'waarde-1'
    assert instance.testKeuzelijstMetKard[1] == 'waarde-2'
    assert instance.testStringFieldMetKard[0] == '1'
    assert instance.testStringFieldMetKard[1] == '2'


def test_from_dict_attributes_with_waarde_shortcut(subtests):
    with subtests.test('waarde_shortcut = True'):
        input_dict = {'testEenvoudigType': '1',
                      'testEenvoudigTypeMetKard': ['1', '2'],
                      'testKwantWrd': 1.2,
                      'testKwantWrdMetKard': [1.2, 2.3]}
        instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path,
                                               waarde_shortcut=True)
        assert instance is not None
        assert instance.is_instance_of(AllCasesTestClass)
        assert AllCasesTestClass.typeURI == instance.typeURI
        assert instance.testEenvoudigType.waarde == '1'
        assert instance.testEenvoudigTypeMetKard[0].waarde == '1'
        assert instance.testEenvoudigTypeMetKard[1].waarde == '2'
        assert instance.testKwantWrd.waarde == 1.2
        assert instance.testKwantWrdMetKard[0].waarde == 1.2
        assert instance.testKwantWrdMetKard[1].waarde == 2.3

    with subtests.test('waarde_shortcut = False'):
        input_dict = {'testEenvoudigType': {'waarde': '1'},
                      'testEenvoudigTypeMetKard': [{'waarde': '1'}, {'waarde': '2'}],
                      'testKwantWrd': {'waarde': 1.2},
                      'testKwantWrdMetKard': [{'waarde': 1.2}, {'waarde': 2.3}]}
        instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path)
        assert instance is not None
        assert instance.is_instance_of(AllCasesTestClass)
        assert AllCasesTestClass.typeURI == instance.typeURI
        assert instance.testEenvoudigType.waarde == '1'
        assert instance.testEenvoudigTypeMetKard[0].waarde == '1'
        assert instance.testEenvoudigTypeMetKard[1].waarde == '2'
        assert instance.testKwantWrd.waarde == 1.2
        assert instance.testKwantWrdMetKard[0].waarde == 1.2
        assert instance.testKwantWrdMetKard[1].waarde == 2.3


def test_from_dict_rdf_attributes_with_waarde_shortcut(subtests):
    with subtests.test('waarde_shortcut = True'):
        input_dict = {'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType': '1',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigTypeMetKard': [
                          '1', '2'],
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd': 1.2,
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrdMetKard': [
                          1.2, 2.3]}
        instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path,
                                               waarde_shortcut=True, rdf=True)
        assert instance is not None
        assert instance.is_instance_of(AllCasesTestClass)
        assert AllCasesTestClass.typeURI == instance.typeURI
        assert instance.testEenvoudigType.waarde == '1'
        assert instance.testEenvoudigTypeMetKard[0].waarde == '1'
        assert instance.testEenvoudigTypeMetKard[1].waarde == '2'
        assert instance.testKwantWrd.waarde == 1.2
        assert instance.testKwantWrdMetKard[0].waarde == 1.2
        assert instance.testKwantWrdMetKard[1].waarde == 2.3

    with subtests.test('waarde_shortcut = False'):
        input_dict = {'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType': {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde': '1'},
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigTypeMetKard': [{
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde': '1'
            },{
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde': '2'}],
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd': {
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 1.2},
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrdMetKard': [{
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 1.2}, {
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 2.3}]}
        instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path, rdf=True)
        assert instance is not None
        assert instance.is_instance_of(AllCasesTestClass)
        assert AllCasesTestClass.typeURI == instance.typeURI
        assert instance.testEenvoudigType.waarde == '1'
        assert instance.testEenvoudigTypeMetKard[0].waarde == '1'
        assert instance.testEenvoudigTypeMetKard[1].waarde == '2'
        assert instance.testKwantWrd.waarde == 1.2
        assert instance.testKwantWrdMetKard[0].waarde == 1.2
        assert instance.testKwantWrdMetKard[1].waarde == 2.3


def test_from_dict_complex_single_attributes():
    input_dict = {'testComplexType': {'testBooleanField': True,
                                      'testComplexType2': {
                                          'testStringField': 'test'},
                                      'testKwantWrd': {'waarde': 1.2}},
                  'testUnionType': {'unionString': 'union_test'}}
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testComplexType.testBooleanField
    assert instance.testComplexType.testComplexType2.testStringField == 'test'
    assert instance.testComplexType.testKwantWrd.waarde == 1.2
    assert instance.testUnionType.unionString == 'union_test'


def test_from_dict_rdf_complex_single_attributes():
    input_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType':
            {
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testBooleanField': True,
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testComplexType2': {
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testStringField': 'test'},
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testKwantWrd': {
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 1.2}},
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionType': {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionString': 'union_test'}}
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path, rdf=True)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testComplexType.testBooleanField
    assert instance.testComplexType.testComplexType2.testStringField == 'test'
    assert instance.testComplexType.testKwantWrd.waarde == 1.2
    assert instance.testUnionType.unionString == 'union_test'


def test_from_dict_complex_attributes_with_cardinality():
    input_dict = {'testComplexTypeMetKard': [
        {'testBooleanField': True,
         'testComplexType2MetKard': [{
             'testStringField': 'test2.1'}, {
             'testStringField': 'test2.2'}],
         'testKwantWrdMetKard': [{'waarde': 1.2}, {'waarde': 2.3}],
         'testStringFieldMetKard': ['test3', 'test4']},
        {'testStringFieldMetKard': ['test5', 'test6']}],
        'testUnionTypeMetKard': [{'unionString': 'union_test'}, {'unionString': 'union_test2'}]
    }
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testComplexTypeMetKard[0].testBooleanField
    assert instance.testComplexTypeMetKard[0].testComplexType2MetKard[0].testStringField == 'test2.1'
    assert instance.testComplexTypeMetKard[0].testComplexType2MetKard[1].testStringField == 'test2.2'
    assert instance.testComplexTypeMetKard[0].testKwantWrdMetKard[0].waarde == 1.2
    assert instance.testComplexTypeMetKard[0].testKwantWrdMetKard[1].waarde == 2.3
    assert instance.testComplexTypeMetKard[0].testStringFieldMetKard[0] == 'test3'
    assert instance.testComplexTypeMetKard[0].testStringFieldMetKard[1] == 'test4'
    assert instance.testComplexTypeMetKard[1].testStringFieldMetKard[0] == 'test5'
    assert instance.testComplexTypeMetKard[1].testStringFieldMetKard[1] == 'test6'
    assert instance.testUnionTypeMetKard[0].unionString == 'union_test'
    assert instance.testUnionTypeMetKard[1].unionString == 'union_test2'


def test_from_dict_rdf_complex_attributes_with_cardinality():
    input_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexTypeMetKard':
            [{
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testBooleanField': True,
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testComplexType2MetKard':
                    [{
                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testStringField': 'test2.1'},
                     {
                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testStringField': 'test2.2'}],
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testKwantWrdMetKard':
                    [{'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 1.2},
                     {'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 2.3}],
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringFieldMetKard': [
                    'test3', 'test4']},
                {
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringFieldMetKard': [
                        'test5', 'test6']}],
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionTypeMetKard':
            [{
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionString': 'union_test'},
                {
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionString': 'union_test2'}]
    }
    instance = AllCasesTestClass.from_dict(input_dict, model_directory=model_directory_path, rdf=True)
    assert instance is not None
    assert instance.is_instance_of(AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testComplexTypeMetKard[0].testBooleanField
    assert instance.testComplexTypeMetKard[0].testComplexType2MetKard[0].testStringField == 'test2.1'
    assert instance.testComplexTypeMetKard[0].testComplexType2MetKard[1].testStringField == 'test2.2'
    assert instance.testComplexTypeMetKard[0].testKwantWrdMetKard[0].waarde == 1.2
    assert instance.testComplexTypeMetKard[0].testKwantWrdMetKard[1].waarde == 2.3
    assert instance.testComplexTypeMetKard[0].testStringFieldMetKard[0] == 'test3'
    assert instance.testComplexTypeMetKard[0].testStringFieldMetKard[1] == 'test4'
    assert instance.testComplexTypeMetKard[1].testStringFieldMetKard[0] == 'test5'
    assert instance.testComplexTypeMetKard[1].testStringFieldMetKard[1] == 'test6'
    assert instance.testUnionTypeMetKard[0].unionString == 'union_test'
    assert instance.testUnionTypeMetKard[1].unionString == 'union_test2'


def test_create_dict_from_asset_non_standard_attributes_warnings_suppressed(subtests, recwarn):
    with subtests.test(msg='non-standard simple attribute / warnings suppressed'):
        instance = AllCasesTestClass()
        instance.testStringField = 'string'
        instance.testBooleanField = True
        instance.non_standard_attribute_no_warning = 'waarde-2'

        d = instance.create_dict_from_asset(warn_for_non_otl_conform_attributes=False)
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testBooleanField': True,
                    'testStringField': 'string',
                    'non_standard_attribute_no_warning': 'waarde-2'}
        assert d == expected
        assert len(recwarn) == 0


def test_create_dict_from_asset_non_standard_attributes(subtests):
    with subtests.test(msg='non-standard simple attribute / warnings not suppressed'):
        instance = AllCasesTestClass()
        instance.testStringField = 'string'
        instance.testBooleanField = True
        instance.non_standard_attribute = 'waarde-2'

        with pytest.warns(NonStandardAttributeWarning):
            d = instance.create_dict_from_asset()
            expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                        'testBooleanField': True,
                        'testStringField': 'string',
                        'non_standard_attribute': 'waarde-2'}
            assert d == expected

    with subtests.test(msg='non-standard complex attribute / warnings not suppressed'):
        instance = AllCasesTestClass()
        instance.testStringField = 'string'
        instance.testBooleanField = True
        instance.non_standard_attribute = 'waarde-2'
        instance.non_standard_attribute_list = [1, 2]
        instance.testComplexType.testStringField = 'string'
        instance.testComplexType.non_standard_in_complex_attribute = 'waarde-3'

        with pytest.warns(NonStandardAttributeWarning):
            d = instance.create_dict_from_asset()
            expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                        'testBooleanField': True,
                        'testStringField': 'string',
                        'non_standard_attribute': 'waarde-2',
                        'non_standard_attribute_list': [1, 2],
                        'testComplexType': {
                            'non_standard_in_complex_attribute': 'waarde-3',
                            'testStringField': 'string'}
                        }
            assert d == expected


def test_create_dict_from_asset_testclass(subtests):
    with subtests.test(msg='Complex datatype: Dtc'):
        instance = AllCasesTestClass()
        instance.testComplexType.testStringField = 'string'
        instance.testComplexType.testBooleanField = True

        d = instance.create_dict_from_asset()
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testComplexType': {
                        'testBooleanField': True,
                        'testStringField': 'string'}}
        assert d == expected

    with subtests.test(msg='simple attributes'):
        instance = AllCasesTestClass()
        instance.testStringField = 'string'
        instance.testBooleanField = True
        instance.testKeuzelijst = 'waarde-2'
        instance.testDecimalField = 1.5
        instance.testDateField = date(year=2022, month=2, day=2)

        d = instance.create_dict_from_asset()
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testBooleanField': True,
                    'testDateField': date(year=2022, month=2, day=2),
                    'testDecimalField': 1.5,
                    'testKeuzelijst': 'waarde-2',
                    'testStringField': 'string'}
        assert d == expected

        d = instance.create_dict_from_asset(datetime_as_string=True)
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testBooleanField': True,
                    'testDateField': '2022-02-02',
                    'testDecimalField': 1.5,
                    'testKeuzelijst': 'waarde-2',
                    'testStringField': 'string'}
        assert d == expected

    with subtests.test(msg='simple attributes with cardinality'):
        instance = AllCasesTestClass()
        instance._testStringFieldMetKard.add_value('string')
        instance._testStringFieldMetKard.add_value('string 2')
        instance._testKeuzelijstMetKard.add_value('waarde-1')
        instance._testKeuzelijstMetKard.add_value('waarde-2')
        instance._testDecimalFieldMetKard.add_value(1.5)
        instance._testDecimalFieldMetKard.add_value(2.5)
        instance.testIntegerFieldMetKard = []

        d = instance.create_dict_from_asset()
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testDecimalFieldMetKard': [1.5, 2.5],
                    'testIntegerFieldMetKard' : [],
                    'testKeuzelijstMetKard': ['waarde-1', 'waarde-2'],
                    'testStringFieldMetKard': ['string', 'string 2']}
        assert d == expected

    with subtests.test(msg='simple types with waarde_shortcuts'):
        instance = AllCasesTestClass()
        instance.testKwantWrd.waarde = 3.5
        instance._testKwantWrdMetKard.add_empty_value()
        instance.testKwantWrdMetKard[0].waarde = 4.5
        instance._testKwantWrdMetKard.add_empty_value()
        instance.testKwantWrdMetKard[1].waarde = 5.5

        d = instance.create_dict_from_asset(waarde_shortcut=True)
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testKwantWrd': 3.5,
                    'testKwantWrdMetKard': [4.5, 5.5]}
        assert d == expected

        d = instance.create_dict_from_asset(waarde_shortcut=False)
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testKwantWrd': {'waarde': 3.5},
                    'testKwantWrdMetKard': [{'waarde': 4.5}, {'waarde': 5.5}]}
        assert d == expected

    with subtests.test(msg='complex attributes'):
        instance = AllCasesTestClass()
        instance.testComplexType.testStringField = 'string'
        instance.testComplexType.testBooleanField = True
        instance.testComplexType.testKwantWrd.waarde = 1.5
        instance.testComplexType.testComplexType2.testStringField = 'string in complex'
        instance.testComplexType._testStringFieldMetKard.add_value('string in complex')
        instance.testComplexType._testStringFieldMetKard.add_value('string 2 in complex')

        d = instance.create_dict_from_asset(waarde_shortcut=True)
        expected = {
            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
            'testComplexType': {'testBooleanField': True,
                                'testStringField': 'string',
                                'testKwantWrd': 1.5,
                                'testStringFieldMetKard': ['string in complex', 'string 2 in complex'],
                                'testComplexType2': {'testStringField': 'string in complex'}}}
        assert d == expected

    with subtests.test(msg='complex attributes with cardinality'):
        instance = AllCasesTestClass()
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[0].testStringField = 'string 1'
        instance.testComplexTypeMetKard[0].testBooleanField = True
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[1].testStringField = 'string 2'
        instance.testComplexTypeMetKard[1].testBooleanField = False
        instance.testComplexTypeMetKard[1].testComplexType2.testStringField = 'string in complex'
        instance.testComplexTypeMetKard[1]._testComplexType2MetKard.add_empty_value()
        instance.testComplexTypeMetKard[1]._testComplexType2MetKard.add_empty_value()
        instance.testComplexTypeMetKard[1].testComplexType2MetKard[0].testStringField = 'first string in complex'
        instance.testComplexTypeMetKard[1].testComplexType2MetKard[1].testStringField = 'second string in complex'

        d = instance.create_dict_from_asset(waarde_shortcut=True)
        expected = {
            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
            'testComplexTypeMetKard': [
                {'testBooleanField': True,
                 'testStringField': 'string 1'},
                {'testBooleanField': False,
                 'testStringField': 'string 2',
                 'testComplexType2': {'testStringField': 'string in complex'},
                 'testComplexType2MetKard': [{'testStringField': 'first string in complex'},
                                             {'testStringField': 'second string in complex'}]}]}
        assert d == expected


def test_from_dict_with_non_standardised_attributes(subtests, caplog):
    with subtests.test(msg='non-standard simple attribute, warnings suppressed and allowed'):
        instance = AllCasesTestClass()
        instance.testStringField = 'string'
        instance.non_standardized_attribute = 'random'
        d = create_dict_from_asset(instance, warn_for_non_otl_conform_attributes=False)
        assert len(caplog.records) == 0

    with subtests.test(msg='non-standard simple attribute, warnings not suppressed and not allowed'):
        with pytest.raises(ValueError):
            instance = AllCasesTestClass()
            instance.testStringField = 'string'
            instance.non_standardized_attribute = 'random'
            create_dict_from_asset(instance, allow_non_otl_conform_attributes=False)

    with subtests.test(msg='non-standard simple attribute, warnings not suppressed but allowed'):
        with pytest.warns(NonStandardAttributeWarning):
            instance = AllCasesTestClass()
            instance.testStringField = 'string'
            instance.non_standardized_attribute = 'random'
            create_dict_from_asset(instance)


def test_to_dict_with_non_standardised_attributes(subtests, caplog):
    with subtests.test(msg='non-standard simple attribute, not allowed'):
        with pytest.raises(ValueError):
            d = {'non_standardized_attribute': 'random', 'testStringField': 'string',
                 'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}

            OTLObject.from_dict(d, model_directory=model_directory_path, allow_non_otl_conform_attributes=False)

    with subtests.test(msg='non-standard simple attribute, warnings suppressed and allowed'):
        d = {'non_standardized_attribute': 'random', 'testStringField': 'string',
             'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}

        o = OTLObject.from_dict(d, model_directory=model_directory_path, warn_for_non_otl_conform_attributes=False)
        assert len(caplog.records) == 0
        assert o.non_standardized_attribute == 'random'
        assert o.testStringField == 'string'
        assert o.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'

    with subtests.test(msg='non-standard simple attribute, warnings not suppressed and allowed'):
        with pytest.warns(NonStandardAttributeWarning):
            d = {'non_standardized_attribute': 'random', 'testStringField': 'string',
                 'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}

            o = OTLObject.from_dict(d, model_directory=model_directory_path)
            assert o.non_standardized_attribute == 'random'
            assert o.testStringField == 'string'
            assert o.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'


def test_to_dict_and_from_dict():
    instance = AllCasesTestClass()
    instance.testStringField = 'string'
    instance.testBooleanField = True
    instance.testKeuzelijst = 'waarde-2'
    instance.testDecimalField = 1.5
    instance.testDateField = date(year=2022, month=2, day=2)
    instance._testStringFieldMetKard.add_value('string')
    instance._testStringFieldMetKard.add_value('string 2')
    instance._testKeuzelijstMetKard.add_value('waarde-1')
    instance._testKeuzelijstMetKard.add_value('waarde-2')
    instance._testDecimalFieldMetKard.add_value(1.5)
    instance._testDecimalFieldMetKard.add_value(2.5)
    instance.testKwantWrd.waarde = 3.5
    instance._testKwantWrdMetKard.add_empty_value()
    instance.testKwantWrdMetKard[0].waarde = 4.5
    instance._testKwantWrdMetKard.add_empty_value()
    instance.testKwantWrdMetKard[1].waarde = 5.5
    instance.testComplexType.testStringField = 'string'
    instance.testComplexType.testBooleanField = True
    instance.testComplexType.testKwantWrd.waarde = 1.5
    instance.testComplexType.testComplexType2.testStringField = 'string in complex'
    instance.testComplexType._testStringFieldMetKard.add_value('string in complex')
    instance.testComplexType._testStringFieldMetKard.add_value('string 2 in complex')
    instance._testComplexTypeMetKard.add_empty_value()
    instance.testComplexTypeMetKard[0].testStringField = 'string 1'
    instance.testComplexTypeMetKard[0].testBooleanField = True
    instance._testComplexTypeMetKard.add_empty_value()
    instance.testComplexTypeMetKard[1].testStringField = 'string 2'
    instance.testComplexTypeMetKard[1].testBooleanField = False
    instance.testComplexTypeMetKard[1].testComplexType2.testStringField = 'string in complex'
    instance.testComplexTypeMetKard[1]._testComplexType2MetKard.add_empty_value()
    instance.testComplexTypeMetKard[1]._testComplexType2MetKard.add_empty_value()
    instance.testComplexTypeMetKard[1].testComplexType2MetKard[0].testStringField = 'first string in complex'
    instance.testComplexTypeMetKard[1].testComplexType2MetKard[1].testStringField = 'second string in complex'

    created_dict = create_dict_from_asset(instance)
    created_instance = AllCasesTestClass.from_dict(created_dict, model_directory=model_directory_path)
    assert instance == created_instance


def test_create_ld_dict_from_asset_only_id():
    instance = AllCasesTestClass()
    instance.assetId.identificator = '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
    json_ld_dict = create_dict_from_asset(instance, rdf=True)
    expected = {
        '@type': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId': {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator':
                '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
        }
    }

    assert json_ld_dict == expected


def test_create_dict_from_asset_cardinality():
    instance = AllCasesTestClass()
    instance.toestand = 'in-gebruik'
    instance.assetId.identificator = '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
    instance.testKeuzelijstMetKard = ['waarde-1', 'waarde-2']

    asset_dict = create_dict_from_asset(instance)
    expected = {
        'assetId': {'identificator': '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'},
        'testKeuzelijstMetKard': ['waarde-1', 'waarde-2'],
        'toestand': 'in-gebruik',
        'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}

    assert asset_dict == expected


def test_create_ld_dict_from_asset_non_standard_attributes_simple_attributes(subtests, recwarn):
    with subtests.test(msg='non-standard simple attribute / warnings suppressed'):
        instance = AllCasesTestClass()
        instance.toestand = 'in-gebruik'
        instance.assetId.identificator = '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
        instance.non_standard_attribute = 'waarde-2'

        rdf_dict = create_dict_from_asset(instance, rdf=True, warn_for_non_otl_conform_attributes=False)
        expected = {
            '@type': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId': {
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator':
                    '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'},
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand':
                'https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik',
            'non_standard_attribute': 'waarde-2'
        }

        assert rdf_dict == expected
        assert len(recwarn) == 0

    with subtests.test(msg='non-standard simple attribute'):
        instance = AllCasesTestClass()
        instance.toestand = 'in-gebruik'
        instance.assetId.identificator = '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
        instance.non_standard_attribute = 'waarde-2'

        with pytest.warns(NonStandardAttributeWarning):
            rdf_dict = create_dict_from_asset(instance, rdf=True)
            expected = {
                '@type': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId': {
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator':
                        '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'},
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand':
                    'https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik',
                'non_standard_attribute': 'waarde-2'
            }

            assert rdf_dict == expected


def test_create_ld_dict_from_asset_cardinality():
    instance = AllCasesTestClass()
    instance.toestand = 'in-gebruik'
    instance.assetId.identificator = '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
    instance.testStringFieldMetKard = ['1', '2']

    rdf_dict = create_dict_from_asset(instance, rdf=True)
    expected = {
        '@type': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId': {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator':
                '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'},
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand':
            'https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringFieldMetKard': ['1', '2']
    }

    assert rdf_dict == expected


def test_create_dict_from_asset_datetimes(recwarn):
    instance = AllCasesTestClass()
    instance.testDateField = date(year=2022, month=2, day=2)
    instance.testDateTimeField = datetime(year=2022, month=2, day=2, hour=12, minute=30, second=30)
    instance.testTimeField = time(hour=12, minute=30, second=30)

    d = create_dict_from_asset(instance)
    expected = {
        'testDateField': date(year=2022, month=2, day=2),
        'testDateTimeField': datetime(year=2022, month=2, day=2, hour=12, minute=30, second=30),
        'testTimeField': time(hour=12, minute=30, second=30),
        'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}

    assert d == expected

    d = create_dict_from_asset(instance, datetime_as_string=True)
    expected = {
        'testDateField': '2022-02-02',
        'testDateTimeField': '2022-02-02 12:30:30',
        'testTimeField': '12:30:30',
        'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}

    assert d == expected

    assert len(recwarn) == 0


def test_from_dict_datetimes(recwarn):
    d = {
        'testDateField': date(year=2022, month=2, day=2),
        'testDateTimeField': datetime(year=2022, month=2, day=2, hour=12, minute=30, second=30),
        'testTimeField': time(hour=12, minute=30, second=30),
        'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}
    instance = AllCasesTestClass.from_dict(d, model_directory=model_directory_path)

    assert instance.typeURI == AllCasesTestClass.typeURI
    assert instance.testDateField == date(year=2022, month=2, day=2)
    assert instance.testDateTimeField == datetime(year=2022, month=2, day=2, hour=12, minute=30, second=30)
    assert instance.testTimeField == time(hour=12, minute=30, second=30)

    d = {
        'testDateField': '2022-02-02',
        'testDateTimeField': '2022-02-02 12:30:30',
        'testTimeField': '12:30:30',
        'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}
    instance = AllCasesTestClass.from_dict(d, model_directory=model_directory_path, datetime_as_string=True)

    assert instance.typeURI == AllCasesTestClass.typeURI
    assert instance.testDateField == date(year=2022, month=2, day=2)
    assert instance.testDateTimeField == datetime(year=2022, month=2, day=2, hour=12, minute=30, second=30)
    assert instance.testTimeField == time(hour=12, minute=30, second=30)

    assert len(recwarn) == 0


def test_create_ld_dict_from_asset_ComplexTypeMetKard():
    instance = AllCasesTestClass()
    instance.toestand = 'in-gebruik'
    instance.assetId.identificator = '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
    instance.testComplexTypeMetKard[0].testStringField = 'string'
    instance.testComplexTypeMetKard[0].testStringFieldMetKard = ['lijst', 'waardes']
    instance._testComplexTypeMetKard.add_empty_value()
    instance.testComplexTypeMetKard[1].testStringField = 'string 2'
    instance.testComplexTypeMetKard[1].testStringFieldMetKard = ['lijst2', 'waardes']
    instance.testKwantWrd.waarde = 1.1
    json_ld_dict = create_dict_from_asset(instance, rdf=True)
    expected = {
        '@type': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand':
            'https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd': {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 1.1
        },
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId': {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator':
                '0000-b25kZXJkZWVsI0FsbENhc2VzVGVzdENsYXNz'
        },
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexTypeMetKard': [{
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringField': 'string',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringFieldMetKard':
                ['lijst', 'waardes']
        }, {
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringField': 'string 2',
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringFieldMetKard':
                ['lijst2', 'waardes']
        }]
    }

    assert json_ld_dict == expected
