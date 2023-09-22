import datetime
import time
import warnings
from datetime import date

import pytest

from UnitTests.TestClasses.Classes.ImplementatieElement.AIMObject import AIMObject
from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.BaseClasses.OTLObject import OTLObject, create_dict_from_asset
from otlmow_model.Exceptions.NonStandardAttributeWarning import NonStandardAttributeWarning


def test_from_dict_typeURI_in_dict():
    input_dict = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}
    instance = OTLObject.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
    assert instance is not None
    assert AllCasesTestClass.typeURI == instance.typeURI


def test_from_dict_rdf_typeURI_in_dict():
    input_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI':
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'}
    instance = OTLObject.from_dict(input_dict, directory='UnitTests.TestClasses.Classes', rdf=True)
    assert instance is not None
    assert AllCasesTestClass.typeURI == instance.typeURI


def test_from_dict_abstract_class_no_typeURI_in_dict():
    input_dict = {}
    with pytest.raises(ValueError):
        OTLObject.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
    with pytest.raises(ValueError):
        AIMObject.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')


def test_from_dict_non_standard_attributes():
    with pytest.warns(NonStandardAttributeWarning):
        input_dict = {'testBooleanField': True,
                      'non_standard_attribute': True }
        instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
        assert instance is not None
        assert isinstance(instance, AllCasesTestClass)
        assert AllCasesTestClass.typeURI == instance.typeURI
        assert instance.testBooleanField
        assert instance.non_standard_attribute


def test_from_dict_simple_single_attributes():
    input_dict = {'testBooleanField': True,
                  'testKeuzelijst': 'waarde-2',
                  'testDateField': '2023-01-01',
                  'testDateTimeField': '2023-01-01 10:11:12',
                  'testTimeField': '10:11:12',
                  'testDecimalField': 1.2,
                  'testIntegerField': 1,
                  'testStringField': 'test'}
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testBooleanField
    assert instance.testKeuzelijst == 'waarde-2'
    assert instance.testDateField == datetime.date(2023, 1, 1)
    assert instance.testDateTimeField == datetime.datetime(2023, 1, 1, 10, 11, 12)
    assert instance.testTimeField == datetime.time(10, 11, 12)
    assert instance.testDecimalField == 1.2
    assert instance.testIntegerField == 1
    assert instance.testStringField == 'test'


def test_from_dict_rdf_simple_single_attributes():
    input_dict = {
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testBooleanField': True,
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKeuzelijst': 'waarde-2',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateField': '2023-01-01',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateTimeField': '2023-01-01 10:11:12',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testTimeField': '10:11:12',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDecimalField': 1.2,
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testIntegerField': 1,
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField': 'test'}
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes', rdf=True)
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.testBooleanField
    assert instance.testKeuzelijst == 'waarde-2'
    assert instance.testDateField == datetime.date(2023, 1, 1)
    assert instance.testDateTimeField == datetime.datetime(2023, 1, 1, 10, 11, 12)
    assert instance.testTimeField == datetime.time(10, 11, 12)
    assert instance.testDecimalField == 1.2
    assert instance.testIntegerField == 1
    assert instance.testStringField == 'test'


def test_from_dict_simple_attributes_with_cardinality():
    input_dict = {'testDecimalFieldMetKard': [1.2, 2.3],
                  'testIntegerFieldMetKard': [1, 2],
                  'testKeuzelijstMetKard': ['waarde-1', 'waarde-2'],
                  'testStringFieldMetKard': ['1', '2']}
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
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
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes', rdf=True)
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
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
        instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes',
                                               waarde_shortcut=True)
        assert instance is not None
        assert isinstance(instance, AllCasesTestClass)
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
        instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
        assert instance is not None
        assert isinstance(instance, AllCasesTestClass)
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
        instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes',
                                               waarde_shortcut=True, rdf=True)
        assert instance is not None
        assert isinstance(instance, AllCasesTestClass)
        assert AllCasesTestClass.typeURI == instance.typeURI
        assert instance.testEenvoudigType.waarde == '1'
        assert instance.testEenvoudigTypeMetKard[0].waarde == '1'
        assert instance.testEenvoudigTypeMetKard[1].waarde == '2'
        assert instance.testKwantWrd.waarde == 1.2
        assert instance.testKwantWrdMetKard[0].waarde == 1.2
        assert instance.testKwantWrdMetKard[1].waarde == 2.3

    with subtests.test('waarde_shortcut = False'):
        input_dict = {'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType':
            {
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde': '1'},
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigTypeMetKard':
                [{
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde': '1'},
                    {
                        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde': '2'}],
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd':
                {
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 1.2},
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrdMetKard':
                [{
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 1.2},
                    {
                        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde': 2.3}]}
        instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes', rdf=True)
        assert instance is not None
        assert isinstance(instance, AllCasesTestClass)
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
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
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
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes', rdf=True)
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
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
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes')
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
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
                     [{'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testStringField': 'test2.1'},
                      {'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType2.testStringField': 'test2.2'}],
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
    instance = AllCasesTestClass.from_dict(input_dict, directory='UnitTests.TestClasses.Classes', rdf=True)
    assert instance is not None
    assert isinstance(instance, AllCasesTestClass)
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


def test_change_typeURI():
    instance = AllCasesTestClass()
    assert AllCasesTestClass.typeURI == instance.typeURI
    assert instance.typeURI is not None

    with pytest.raises(ValueError):
        instance.typeURI = 'https://www.new-uri.com/'

    with pytest.raises(ValueError):
        instance.typeURI = None


def test_fill_with_dummy_data():
    instance = AllCasesTestClass()
    instance.fill_with_dummy_data()
    assert instance.assetId is not None
    assert instance.assetId.identificator is not None
    assert instance.testKeuzelijst is not None
    assert instance.testComplexTypeMetKard[0].testStringField is not None


def test_fill_with_dummy_data_keuzelijsten(subtests):
    instance = AllCasesTestClass()

    with subtests.test(msg='valid keuzelijst'):
        instance._testKeuzelijst.fill_with_dummy_data()
        assert instance.testKeuzelijst in instance._testKeuzelijst.field.options.keys()

    with subtests.test(msg='empty keuzelijst'):
        previous_options = instance._testKeuzelijst.field.options
        instance._testKeuzelijst.field.options = {}
        instance._testKeuzelijst.fill_with_dummy_data()
        assert instance.testKeuzelijst is None
        instance._testKeuzelijst.field.options = previous_options


def test_fill_with_dummy_data_through_attributes(subtests):
    instance = AllCasesTestClass()

    with subtests.test(msg='attribute 1 level deep'):
        instance._testDecimalField.fill_with_dummy_data()
        assert instance.testDecimalField is not None

    with subtests.test(msg='attribute 1 level deep with cardinality > 1'):
        instance._testStringFieldMetKard.fill_with_dummy_data()
        assert instance.testStringFieldMetKard is not None

    with subtests.test(msg='union attribute 1 level deep'):
        instance._testUnionType.fill_with_dummy_data()
        assert instance.testUnionType is not None
        first = instance.testUnionType.unionKwantWrd.waarde is not None
        second = instance.testUnionType.unionString is not None
        assert first != second  # either first or second is True, but not both
        assert instance._testUnionType is not None

    with subtests.test(msg='attribute 2 levels deep with waarde shortcut disabled top level'):
        instance._testKwantWrd.fill_with_dummy_data()
        assert instance.testKwantWrd.waarde is not None

    with subtests.test(msg='attribute 2 levels deep with waarde shortcut disabled bottom level'):
        instance.testKwantWrd._waarde.fill_with_dummy_data()
        assert instance.testKwantWrd.waarde is not None

    with subtests.test(msg='attribute 2 levels deep top level'):
        instance._testComplexType.fill_with_dummy_data()
        assert instance.testComplexType.testStringField is not None

    with subtests.test(msg='attribute 2 levels deep bottom level'):
        instance.testComplexType._testStringField.fill_with_dummy_data()
        assert instance.testComplexType.testStringField is not None

    with subtests.test(msg='attribute 2 levels deep with cardinality > 1 top level'):
        instance._testComplexTypeMetKard.fill_with_dummy_data()
        assert instance.testComplexTypeMetKard[0].testStringFieldMetKard[0] is not None

    with subtests.test(msg='attribute 2 levels deep with cardinality > 1 bottom level'):
        instance.testComplexTypeMetKard[0]._testStringFieldMetKard.fill_with_dummy_data()
        assert instance.testComplexTypeMetKard[0].testStringFieldMetKard[0] is not None

    # with self.subTest("attribute 3 levels deep"):
    #     dotnotation = DotnotationHelper().get_dotnotation(instance.testComplexType.testComplexType2._testStringField)
    #     self.assertEqual('testComplexType.testComplexType2.testStringField', dotnotation)
    #
    # with self.subTest("attribute 3 levels deep with cardinality > 1"):
    #     dotnotation = DotnotationHelper().get_dotnotation(instance.testComplexTypeMetKard[0].testComplexType2MetKard[0]._testStringFieldMetKard)
    #     self.assertEqual('testComplexTypeMetKard[].testComplexType2MetKard[].testStringFieldMetKard[]', dotnotation)
    #
    # with self.subTest("attribute 4 levels deep with waarde shortcut disabled"):
    #     dotnotation = DotnotationHelper().get_dotnotation(instance.testComplexType.testComplexType2.testKwantWrd._waarde)
    #     self.assertEqual('testComplexType.testComplexType2.testKwantWrd.waarde', dotnotation)


def test_build_string_version_empty_class():
    info_string = str(AllCasesTestClass())
    expected = '<AllCasesTestClass> object\n' \
               '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
    assert info_string == expected


def test_make_string_version_StringField():
    instance = AllCasesTestClass()
    instance.isActief = True
    info_string = str(instance)
    expected = '<AllCasesTestClass> object\n' \
               '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
               '    isActief : True'

    assert info_string == expected


def test_make_string_version_DtcIdentificator():
    instance = AllCasesTestClass()
    instance.assetId.identificator = 'eigen_id'
    instance.assetId.toegekendDoor = 'AWV'
    info_string = str(instance)
    expected = '<AllCasesTestClass> object\n' \
               '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
               '    assetId :\n' \
               '        identificator : eigen_id\n' \
               '        toegekendDoor : AWV'

    assert info_string == expected


def test_make_string_version_kardinaliteit():
    instance = AllCasesTestClass()
    instance.testIntegerFieldMetKard = [1, 2, 3]

    info_string = str(instance)
    expected = '<AllCasesTestClass> object\n' \
               '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
               '    testIntegerFieldMetKard :\n' \
               '    [0] 1\n' \
               '    [1] 2\n' \
               '    [2] 3'

    assert info_string == expected


def test_make_string_version_kardinaliteit_one_too_many():
    instance = AllCasesTestClass()
    instance.testIntegerFieldMetKard = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    info_string = str(instance)
    expected = '<AllCasesTestClass> object\n' \
               '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
               '    testIntegerFieldMetKard :\n' \
               '    [0] 1\n' \
               '    [1] 2\n' \
               '    [2] 3\n' \
               '    [3] 4\n' \
               '    [4] 5\n' \
               '    [5] 6\n' \
               '    [6] 7\n' \
               '    [7] 8\n' \
               '    [8] 9\n' \
               '    [9] 10\n' \
               '    ...(1 more item)'

    assert info_string == expected


def test_make_string_version_kardinaliteit_two_too_many():
    instance = AllCasesTestClass()
    instance.testIntegerFieldMetKard = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    info_string = str(instance)
    expected = '<AllCasesTestClass> object\n' \
               '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
               '    testIntegerFieldMetKard :\n' \
               '    [0] 1\n' \
               '    [1] 2\n' \
               '    [2] 3\n' \
               '    [3] 4\n' \
               '    [4] 5\n' \
               '    [5] 6\n' \
               '    [6] 7\n' \
               '    [7] 8\n' \
               '    [8] 9\n' \
               '    [9] 10\n' \
               '    ...(2 more items)'

    assert info_string == expected


def test_make_string_version_complex_kardinaliteit():
    instance = AllCasesTestClass()
    instance._testComplexTypeMetKard.add_empty_value()
    instance.testComplexTypeMetKard[0].testBooleanField = True
    instance.testComplexTypeMetKard[0].testKwantWrd.waarde = 10.0
    instance._testComplexTypeMetKard.add_empty_value()
    instance.testComplexTypeMetKard[1].testBooleanField = False
    instance.testComplexTypeMetKard[1].testKwantWrd.waarde = 5.0

    info_string = str(instance)
    expected = '<AllCasesTestClass> object\n' \
               '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
               '    testComplexTypeMetKard :\n' \
               '    [0] testBooleanField : True\n' \
               '    [0] testKwantWrd :\n' \
               '    [0]     waarde : 10.0\n' \
               '    [1] testBooleanField : False\n' \
               '    [1] testKwantWrd :\n' \
               '    [1]     waarde : 5.0'

    assert info_string == expected


def test_make_string_version_multiple_complex_():
    instance = Bevestiging()
    instance.assetId.identificator = 'camera0001_-_paal12345'
    instance.bronAssetId.identificator = 'camera0001'
    instance.doelAssetId.identificator = 'paal12345'

    info_string = str(instance)
    expected = """<Bevestiging> object
    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging
    assetId :
        identificator : camera0001_-_paal12345
    bronAssetId :
        identificator : camera0001
    doelAssetId :
        identificator : paal12345"""

    assert info_string == expected

def test_create_dict_from_asset_non_standard_attributes_warnings_suppressed(subtests):
    with subtests.test(msg='non-standard simple attribute / warnings suppressed'):
        instance = AllCasesTestClass()
        instance.testStringField = 'string'
        instance.testBooleanField = True
        instance.non_standard_attribute_no_warning = 'waarde-2'

        with warnings.catch_warnings():
            d = instance.create_dict_from_asset(suppress_warnings_non_standardised_attributes=True)
            expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                        'testBooleanField': True,
                        'testStringField': 'string',
                        'non_standard_attribute_no_warning': 'waarde-2'}
            assert d == expected


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

        d = instance.create_dict_from_asset()
        expected = {'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                    'testDecimalFieldMetKard': [1.5, 2.5],
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


def test__iter__():
    instance = AllCasesTestClass()
    attribute_list = list(instance)
    assert attribute_list[
               0].objectUri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId'
    assert [attr.objectUri for attr in instance] == [
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.bestekPostNummer',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.datumOprichtingObject',
        'https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus.isActief',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.standaardBestekPostNummer',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testBooleanField',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexTypeMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateField',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDateTimeField',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDecimalField',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testDecimalFieldMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigType',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testEenvoudigTypeMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testIntegerField',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testIntegerFieldMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKeuzelijst',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKeuzelijstMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrd',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testKwantWrdMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringField',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testStringFieldMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testTimeField',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionType',
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testUnionTypeMetKard',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.theoretischeLevensduur',
        'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand']


def test__eq__(subtests):
    with subtests.test(msg='equal'):
        instance = AllCasesTestClass()
        instance.testIntegerFieldMetKard = [1, 2, 3]
        instance.testComplexType.testStringField = 'string'
        instance.testComplexType.testBooleanField = True
        instance.testComplexType.testKwantWrd.waarde = 1.5
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[0].testStringField = 'string 1'
        instance.testComplexTypeMetKard[0].testBooleanField = True
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[1].testStringField = 'string 2'
        instance.testComplexTypeMetKard[1].testBooleanField = False

        instance2 = AllCasesTestClass()
        instance2.testIntegerFieldMetKard = [1, 2, 3]
        instance2.testComplexType.testStringField = 'string'
        instance2.testComplexType.testBooleanField = True
        instance2.testComplexType.testKwantWrd.waarde = 1.5
        instance2._testComplexTypeMetKard.add_empty_value()
        instance2.testComplexTypeMetKard[0].testStringField = 'string 1'
        instance2.testComplexTypeMetKard[0].testBooleanField = True
        instance2._testComplexTypeMetKard.add_empty_value()
        instance2.testComplexTypeMetKard[1].testStringField = 'string 2'
        instance2.testComplexTypeMetKard[1].testBooleanField = False

        assert instance == instance2

    with subtests.test(msg='not equal'):
        instance = AllCasesTestClass()
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[0].testStringField = 'string 1'
        instance.testComplexTypeMetKard[0].testBooleanField = True
        instance._testComplexTypeMetKard.add_empty_value()
        instance.testComplexTypeMetKard[1].testStringField = 'string 2'
        instance.testComplexTypeMetKard[1].testBooleanField = False

        instance2 = AllCasesTestClass()
        instance2.testComplexTypeMetKard[0].testStringField = 'string 1'
        instance2.testComplexTypeMetKard[0].testBooleanField = True
        instance2._testComplexTypeMetKard.add_empty_value()
        instance2.testComplexTypeMetKard[1].testStringField = 'string 3'
        instance2.testComplexTypeMetKard[1].testBooleanField = False

        assert not instance == instance2


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
    created_instance = AllCasesTestClass.from_dict(created_dict, directory='UnitTests.TestClasses.Classes')
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


def test_raise_value_errors_in_set_waarde_with_cardinality():
    instance = AllCasesTestClass()
    with pytest.raises(ValueError):
        instance.testKeuzelijstMetKard = ['1']
