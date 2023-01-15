from datetime import date
from unittest import TestCase

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.Bevestiging import Bevestiging


class OTLObjectsTests(TestCase):
    def test_fill_with_dummy_data(self):
        instance = AllCasesTestClass()
        instance.fill_with_dummy_data()
        self.assertIsNotNone(instance.assetId)
        self.assertIsNotNone(instance.assetId.identificator)
        self.assertIsNotNone(instance.testKeuzelijst)
        self.assertIsNotNone(instance.testComplexTypeMetKard[0].testStringField)

    def test_fill_with_dummy_data_keuzelijsten(self):
        instance = AllCasesTestClass()

        with self.subTest("valid keuzelijst"):
            instance._testKeuzelijst.fill_with_dummy_data()
            self.assertTrue(instance.testKeuzelijst in instance._testKeuzelijst.field.options.keys())

        with self.subTest("empty keuzelijst"):
            previous_options = instance._testKeuzelijst.field.options
            instance._testKeuzelijst.field.options = {}
            instance._testKeuzelijst.fill_with_dummy_data()
            self.assertEqual(None, instance.testKeuzelijst)
            instance._testKeuzelijst.field.options = previous_options

    def test_fill_with_dummy_data_through_attributes(self):
        instance = AllCasesTestClass()

        with self.subTest("attribute 1 level deep"):
            instance._testDecimalField.fill_with_dummy_data()
            self.assertIsNotNone(instance.testDecimalField)

        with self.subTest("attribute 1 level deep with cardinality > 1"):
            instance._testStringFieldMetKard.fill_with_dummy_data()
            self.assertIsNotNone(instance.testStringFieldMetKard)

        with self.subTest("union attribute 1 level deep"):
            instance._testUnionType.fill_with_dummy_data()
            self.assertIsNotNone(instance.testUnionType)
            first = instance.testUnionType.unionKwantWrd.waarde is not None
            second = instance.testUnionType.unionString is not None
            self.assertTrue(first != second)  # either first or second is True, but not both
            self.assertIsNotNone(instance._testUnionType)

        with self.subTest("attribute 2 levels deep with waarde shortcut disabled top level"):
            instance._testKwantWrd.fill_with_dummy_data()
            self.assertIsNotNone(instance.testKwantWrd.waarde)

        with self.subTest("attribute 2 levels deep with waarde shortcut disabled bottom level"):
            instance.testKwantWrd._waarde.fill_with_dummy_data()
            self.assertIsNotNone(instance.testKwantWrd.waarde)

        with self.subTest("attribute 2 levels deep top level"):
            instance._testComplexType.fill_with_dummy_data()
            self.assertIsNotNone(instance.testComplexType.testStringField)

        with self.subTest("attribute 2 levels deep bottom level"):
            instance.testComplexType._testStringField.fill_with_dummy_data()
            self.assertIsNotNone(instance.testComplexType.testStringField)

        with self.subTest("attribute 2 levels deep with cardinality > 1 top level"):
            instance._testComplexTypeMetKard.fill_with_dummy_data()
            self.assertIsNotNone(instance.testComplexTypeMetKard[0].testStringFieldMetKard[0])

        with self.subTest("attribute 2 levels deep with cardinality > 1 bottom level"):
            instance.testComplexTypeMetKard[0]._testStringFieldMetKard.fill_with_dummy_data()
            self.assertIsNotNone(instance.testComplexTypeMetKard[0].testStringFieldMetKard[0])

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

    def test_build_string_version_empty_class(self):
        info_string = str(AllCasesTestClass())
        expected = '<AllCasesTestClass> object\n' \
                   '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'
        self.assertEqual(expected, info_string)

    def test_make_string_version_StringField(self):
        instance = AllCasesTestClass()
        instance.isActief = True
        info_string = str(instance)
        expected = '<AllCasesTestClass> object\n' \
                   '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
                   '    isActief : True'

        self.assertEqual(expected, info_string)

    def test_make_string_version_DtcIdentificator(self):
        instance = AllCasesTestClass()
        instance.assetId.identificator = 'eigen_id'
        instance.assetId.toegekendDoor = 'AWV'
        info_string = str(instance)
        expected = '<AllCasesTestClass> object\n' \
                   '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
                   '    assetId :\n' \
                   '        identificator : eigen_id\n' \
                   '        toegekendDoor : AWV'

        self.assertEqual(expected, info_string)

    def test_make_string_version_kardinaliteit(self):
        instance = AllCasesTestClass()
        instance.testIntegerFieldMetKard = [1, 2, 3]

        info_string = str(instance)
        expected = '<AllCasesTestClass> object\n' \
                   '    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass\n' \
                   '    testIntegerFieldMetKard :\n' \
                   '    [0] 1\n' \
                   '    [1] 2\n' \
                   '    [2] 3'

        self.assertEqual(expected, info_string)

    def test_make_string_version_kardinaliteit_one_too_many(self):
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

        self.assertEqual(expected, info_string)

    def test_make_string_version_kardinaliteit_two_too_many(self):
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

        self.assertEqual(expected, info_string)

    def test_make_string_version_complex_kardinaliteit(self):
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

        self.assertEqual(expected, info_string)

    def test_make_string_version_multiple_complex_(self):
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

        self.assertEqual(expected, info_string)

    def test_create_dict_from_asset_testclass(self):
        with self.subTest('Complex datatype: Dtc'):
            instance = AllCasesTestClass()
            instance.testComplexType.testStringField = 'string'
            instance.testComplexType.testBooleanField = True

            d = instance.create_dict_from_asset()
            expected = {'testComplexType': {
                'testBooleanField': True,
                'testStringField': 'string'}}
            self.assertDictEqual(expected, d)

        with self.subTest('simple attributes'):
            instance = AllCasesTestClass()
            instance.testStringField = 'string'
            instance.testBooleanField = True
            instance.testKeuzelijst = 'waarde-2'
            instance.testDecimalField = 1.5
            instance.testDateField = date(year=2022, month=2, day=2)

            d = instance.create_dict_from_asset()
            expected = {'testBooleanField': True,
                        'testDateField': '2022-02-02',
                        'testDecimalField': 1.5,
                        'testKeuzelijst': 'waarde-2',
                        'testStringField': 'string'}
            self.assertDictEqual(expected, d)

        with self.subTest('simple attributes with cardinality'):
            instance = AllCasesTestClass()
            instance._testStringFieldMetKard.add_value('string')
            instance._testStringFieldMetKard.add_value('string 2')
            instance._testKeuzelijstMetKard.add_value('waarde-1')
            instance._testKeuzelijstMetKard.add_value('waarde-2')
            instance._testDecimalFieldMetKard.add_value(1.5)
            instance._testDecimalFieldMetKard.add_value(2.5)

            d = instance.create_dict_from_asset()
            expected = {'testDecimalFieldMetKard': [1.5, 2.5],
                        'testKeuzelijstMetKard': ['waarde-1', 'waarde-2'],
                        'testStringFieldMetKard': ['string', 'string 2']}
            self.assertDictEqual(expected, d)

        with self.subTest('simple types with waarde_shortcuts'):
            instance = AllCasesTestClass()
            instance.testKwantWrd.waarde = 3.5
            instance._testKwantWrdMetKard.add_empty_value()
            instance.testKwantWrdMetKard[0].waarde = 4.5
            instance._testKwantWrdMetKard.add_empty_value()
            instance.testKwantWrdMetKard[1].waarde = 5.5

            d = instance.create_dict_from_asset(waarde_shortcut=True)
            expected = {'testKwantWrd': 3.5,
                        'testKwantWrdMetKard': [4.5, 5.5]}
            self.assertDictEqual(expected, d)

            d = instance.create_dict_from_asset(waarde_shortcut=False)
            expected = {'testKwantWrd': {'waarde': 3.5},
                        'testKwantWrdMetKard': [{'waarde': 4.5}, {'waarde': 5.5}]}
            self.assertDictEqual(expected, d)

        with self.subTest('complex attributes'):
            instance = AllCasesTestClass()
            instance.testComplexType.testStringField = 'string'
            instance.testComplexType.testBooleanField = True
            instance.testComplexType.testKwantWrd.waarde = 1.5
            instance.testComplexType.testComplexType2.testStringField = 'string in complex'
            instance.testComplexType._testStringFieldMetKard.add_value('string in complex')
            instance.testComplexType._testStringFieldMetKard.add_value('string 2 in complex')

            d = instance.create_dict_from_asset(waarde_shortcut=True)
            expected = {
                'testComplexType': {'testBooleanField': True,
                                    'testStringField': 'string',
                                    'testKwantWrd': 1.5,
                                    'testStringFieldMetKard': ['string in complex', 'string 2 in complex'],
                                    'testComplexType2': {'testStringField': 'string in complex'}}}
            self.assertDictEqual(expected, d)

        with self.subTest('complex attributes with cardinality'):
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
                'testComplexTypeMetKard': [
                    {'testBooleanField': True,
                     'testStringField': 'string 1'},
                    {'testBooleanField': False,
                     'testStringField': 'string 2',
                     'testComplexType2': {'testStringField': 'string in complex'},
                     'testComplexType2MetKard': [{'testStringField': 'first string in complex'},
                                                 {'testStringField': 'second string in complex'}]}]}
            self.assertDictEqual(expected, d)
