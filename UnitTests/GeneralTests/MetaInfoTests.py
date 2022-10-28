from unittest import TestCase

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.BaseClasses.MetaInfo import meta_info


class MetaInfoTests(TestCase):
    # TODO: test for deprecated class
    def test_meta_info_on_otl_object(self):
        instance = AnotherTestClass()
        result = meta_info(instance)
        expected = 'Showing metadata of AnotherTestClass:\n' \
                   'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass\n' \
                   'definition: Just another TestClass to test relations\n' \
                   'attributes:\n' \
                   '    assetId (type: DtcIdentificator)\n' \
                   '    bestekPostNummer (type: String)\n' \
                   '    datumOprichtingObject (type: Date)\n' \
                   '    deprecatedString (type: DtcTestComplexType) <deprecated since 2.0.0-RC3>\n' \
                   '    isActief (type: Boolean)\n' \
                   '    notitie (type: String)\n' \
                   '    standaardBestekPostNummer (type: String)\n' \
                   '    theoretischeLevensduur (type: KwantWrdInMaand)\n' \
                   '    toestand (type: KlAIMToestand)'
        self.assertEqual(expected, result)

    def test_meta_info_on_otl_attribute_invalid_string(self):
        instance = AnotherTestClass()
        with self.assertRaises(ValueError) as value_error:
            meta_info(instance.assetId, attribute='attribute_does_not_exists')
        self.assertEqual("'attribute_does_not_exists' does not exist, please check the spelling", str(value_error.exception))

    def test_meta_info_on_otl_attribute(self):
        instance = AnotherTestClass()

        result = meta_info(instance, attribute='toestand')
        expected = 'Showing metadata of toestand:\n' \
                   'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand\n' \
                   'definition: Geeft de actuele stand in de levenscyclus van het object.'

        self.assertEqual(expected, result)

    def test_meta_info_on_otl_attribute_Dtc(self):
        instance = AnotherTestClass()

        result = meta_info(instance, attribute='assetId')
        expected = 'Showing metadata of assetId:\n' \
                   'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId\n' \
                   'definition: Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.\n' \
                   'attributes:\n' \
                   '    identificator (type: String)\n' \
                   '    toegekendDoor (type: String)'
        self.assertEqual(expected, result)

        result2 = meta_info(instance._assetId)
        self.assertEqual(expected, result2)

    def test_meta_info_on_otl_attribute_Dtc_by_dotnotation(self):
        instance = AllCasesTestClass()

        result = meta_info(instance, attribute='testComplexType.testComplexType2')
        expected = 'Showing metadata of testComplexType2:\n' \
                   'typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testComplexType2\n' \
                   'definition: Test attribuut voor complexe waarde in een complex datatype.\n' \
                   'attributes:\n' \
                   '    testKwantWrd (type: KwantWrdTest)\n' \
                   '    testKwantWrdMetKard (type: KwantWrdTest, cardinality: 1-*)\n' \
                   '    testStringField (type: String)\n' \
                   '    testStringFieldMetKard (type: String, cardinality: 1-*)'
        self.assertEqual(expected, result)
