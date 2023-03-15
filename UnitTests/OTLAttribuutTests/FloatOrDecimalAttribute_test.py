from unittest import TestCase

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError



class FloatOrDecimalAttributeTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        instance = AllCasesTestClass()
        with self.subTest('empty instance'):
            self.assertIsNone(instance.testDecimalField)

        with self.subTest('assign values to DecimalField with kard 1'):
            instance.testDecimalField = 1.0
            self.assertEqual(1.0, instance.testDecimalField)
            instance.testDecimalField = 2
            self.assertEqual(2, instance.testDecimalField)

    def test_full_test_on_testclass_kard_more(self):
        with self.subTest('empty instance'):
            instance = AllCasesTestClass()
            self.assertIsNone(instance.testDecimalFieldMetKard)

        with self.subTest('assign value to DecimalField with kard * by using add_value method'):
            instance = AllCasesTestClass()
            instance._testDecimalFieldMetKard.add_value(1.0)
            self.assertEqual(1.0, instance.testDecimalFieldMetKard[0])
            instance._testDecimalFieldMetKard.add_value(2)
            self.assertEqual(1.0, instance.testDecimalFieldMetKard[0])
            self.assertEqual(2, instance.testDecimalFieldMetKard[1])

        with self.subTest('assign bad value to DecimalField with kard * by using add_value method'):
            instance = AllCasesTestClass()
            with self.assertRaises(CouldNotConvertToCorrectTypeError):
                instance._testDecimalFieldMetKard.add_value('a')

        with self.subTest('assign values directly to DecimalField with kard *'):
            instance = AllCasesTestClass()
            instance.testDecimalFieldMetKard = [1.0]
            self.assertEqual(1.0, instance.testDecimalFieldMetKard[0])
            instance.testDecimalFieldMetKard = [2]
            self.assertEqual(2, instance.testDecimalFieldMetKard[0])
            instance.testDecimalFieldMetKard = [1.0, 2]
            self.assertEqual(1.0, instance.testDecimalFieldMetKard[0])
            self.assertEqual(2, instance.testDecimalFieldMetKard[1])

        with self.subTest('assign good and bad typed value directly to DecimalField with kard *'):
            with self.assertLogs() as captured:
                instance.testDecimalFieldMetKard = [1.0, '2']
                self.assertEqual(len(captured.records), 1)
            self.assertEqual(1.0, instance.testDecimalFieldMetKard[0])
            self.assertEqual(2, instance.testDecimalFieldMetKard[1])
