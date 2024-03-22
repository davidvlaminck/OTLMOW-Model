from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.ImplementatieElement.AIMObject import AIMObject
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject, dynamic_create_instance_from_uri, \
    dynamic_create_type_from_uri

model_directory_path = Path(__file__).parent.parent / 'TestModel'


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
    assert instance.geometry is not None


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


def test_raise_value_errors_in_set_waarde_with_cardinality():
    instance = AllCasesTestClass()
    with pytest.raises(ValueError):
        instance.testKeuzelijstMetKard = ['1']


def test_isinstance_checks():
    instance = AllCasesTestClass()
    dynamically_created_instance = dynamic_create_instance_from_uri(
        AllCasesTestClass.typeURI, model_directory=model_directory_path)
    assert instance.is_instance_of(AllCasesTestClass)
    assert instance.typeURI == AllCasesTestClass.typeURI
    assert instance.is_instance_of(AIMObject)
    assert not instance.is_instance_of(AnotherTestClass)

    assert dynamically_created_instance.typeURI == AllCasesTestClass.typeURI
    assert dynamically_created_instance.is_instance_of(AllCasesTestClass)
    assert not dynamically_created_instance.is_instance_of(str)
    assert dynamically_created_instance.is_instance_of(OTLObject)

    dynamic_aim_object_type = dynamic_create_type_from_uri(
        AIMObject.typeURI, model_directory=model_directory_path)

    assert dynamically_created_instance.is_instance_of(dynamic_aim_object_type)

    assert dynamically_created_instance.is_instance_of(AIMObject, dynamic_created=True,
                                                       model_directory=model_directory_path)
