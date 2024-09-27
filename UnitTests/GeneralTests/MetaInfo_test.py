import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.DeprecatedTestClass import DeprecatedTestClass
from otlmow_model.OtlmowModel.BaseClasses.MetaInfo import meta_info
from otlmow_model.OtlmowModel.Exceptions.ClassDeprecationWarning import ClassDeprecationWarning


def test_meta_info_on_deprecated_attribute():
    instance = AnotherTestClass()
    result = meta_info(instance, attribute='deprecatedString')
    expected = """Showing metadata of deprecatedString:
typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass.deprecatedString
definition: Tekstveld dat niet meer gebruikt wordt
deprecated since 2.0.0-RC3"""
    assert result == expected


def test_meta_info_on_deprecated_class():
    with pytest.warns(ClassDeprecationWarning):
        instance = DeprecatedTestClass()
        result = meta_info(instance)
        expected = 'Showing metadata of DeprecatedTestClass:\n' \
                   'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass\n' \
                   'definition: Deprecated TestClass\n' \
                   'deprecated since 2.0.0\n' \
                   'attributes:\n' \
                   '    assetId (type: DtcIdentificator)\n' \
                   '    bestekPostNummer (type: String)\n' \
                   '    datumOprichtingObject (type: Date)\n' \
                   '    geometry (type: WKT)\n' \
                   '    isActief (type: Boolean)\n' \
                   '    notitie (type: String)\n' \
                   '    standaardBestekPostNummer (type: String)\n' \
                   '    theoretischeLevensduur (type: KwantWrdInMaand)\n' \
                   '    toestand (type: KlAIMToestand)'
        assert result == expected


def test_meta_info_on_otl_object():
    instance = AnotherTestClass()
    result = meta_info(instance)
    expected = 'Showing metadata of AnotherTestClass:\n' \
               'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass\n' \
               'definition: Just another TestClass to test relations\n' \
               'attributes:\n' \
               '    assetId (type: DtcIdentificator)\n' \
               '    bestekPostNummer (type: String)\n' \
               '    datumOprichtingObject (type: Date)\n' \
               '    deprecatedString (type: String) <deprecated since 2.0.0-RC3>\n' \
               '    geometry (type: WKT)\n' \
               '    isActief (type: Boolean)\n' \
               '    notitie (type: String)\n' \
               '    standaardBestekPostNummer (type: String)\n' \
               '    theoretischeLevensduur (type: KwantWrdInMaand)\n' \
               '    toestand (type: KlAIMToestand)'
    assert result == expected


def test_meta_info_on_otl_attribute_invalid_string():
    instance = AnotherTestClass()
    with pytest.raises(ValueError) as exc_info:
        meta_info(instance.assetId, attribute='attribute_does_not_exists')
    assert str(exc_info.value) == "'attribute_does_not_exists' does not exist, please check the spelling"


def test_meta_info_on_otl_attribute():
    instance = AnotherTestClass()

    result = meta_info(instance, attribute='toestand')
    expected = 'Showing metadata of toestand:\n' \
               'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand\n' \
               'definition: Geeft de actuele stand in de levenscyclus van het object.\n' \
               'valid values:\n' \
               '    geannuleerd\n' \
               '    gepland\n' \
               '    in-gebruik\n' \
               '    in-ontwerp\n' \
               '    in-opbouw\n' \
               '    overgedragen\n' \
               '    uit-gebruik\n' \
               '    verwijderd'

    assert result == expected


def test_meta_info_on_otl_attribute_Dtc():
    instance = AnotherTestClass()

    result = meta_info(instance, attribute='assetId')
    expected = 'Showing metadata of assetId:\n' \
               'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId\n' \
               'definition: Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.\n' \
               'attributes:\n' \
               '    identificator (type: String)\n' \
               '    toegekendDoor (type: String)'
    assert result == expected

    result2 = meta_info(instance._assetId)
    assert result2 == expected


def test_meta_info_on_otl_attribute_Dtc_by_dotnotation():
    instance = AllCasesTestClass()

    result = meta_info(instance, attribute='testComplexType')
    expected = """Showing metadata of testComplexType:
typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass.testComplexType
definition: Test attribuut voor een complexe waarde
attributes:
    testBooleanField (type: Boolean)
    testComplexType2 (type: DtcTestComplexType2)
    testComplexType2MetKard (type: DtcTestComplexType2, cardinality: 1-*)
    testKwantWrd (type: KwantWrdTest)
    testKwantWrdMetKard (type: KwantWrdTest, cardinality: 1-*)
    testStringField (type: String)
    testStringFieldMetKard (type: String, cardinality: 1-*)"""
    assert result == expected


def test_meta_info_on_otl_attribute_in_Dtc_by_dotnotation():
    instance = AllCasesTestClass()

    result = meta_info(instance, attribute='testComplexType.testStringField')
    expected = """Showing metadata of testStringField:
typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringField
definition: Test attribuut voor tekst in een complex datatype."""
    assert result == expected
