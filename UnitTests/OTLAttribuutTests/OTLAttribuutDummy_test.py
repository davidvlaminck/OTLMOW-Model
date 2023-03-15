from datetime import date, datetime, time
from unittest import TestCase

from UnitTests.TestClasses.Datatypes.DtuTestUnionType import DtuTestUnionType
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.BaseClasses.IntegerField import IntegerField
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.BaseClasses.TimeField import TimeField
from UnitTests.TestClasses.Datatypes.DtcTestComplexType import DtcTestComplexType
from UnitTests.TestClasses.Datatypes.KwantWrdTest import KwantWrdTest
from UnitTests.TestClasses.Datatypes.KlTestKeuzelijst import KlTestKeuzelijst


class OTLAttribuutDummyTests(TestCase):
    def test_dummy_StringField(self):
        attr = OTLAttribuut(field=StringField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, str))
        self.assertTrue(5 <= len(generated_dummy_waarde) <= 15)

    def test_dummy_StringFieldMetKard(self):
        attr = OTLAttribuut(field=StringField, kardinaliteit_max='*')
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, list))
        self.assertTrue(len(generated_dummy_waarde) == 1)
        self.assertTrue(isinstance(generated_dummy_waarde[0], str))
        self.assertTrue(5 <= len(generated_dummy_waarde[0]) <= 15)

    def test_dummy_FloatOrDecimalField(self):
        attr = OTLAttribuut(field=FloatOrDecimalField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, float))

    def test_dummy_IntegerField(self):
        attr = OTLAttribuut(field=IntegerField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, int))

    def test_dummy_BooleanField(self):
        attr = OTLAttribuut(field=BooleanField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(generated_dummy_waarde in [False, True])

    def test_dummy_DateField(self):
        attr = OTLAttribuut(field=DateField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, date))

    def test_dummy_DateTimeField(self):
        attr = OTLAttribuut(field=DateTimeField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, datetime))

    def test_dummy_TimeField(self):
        attr = OTLAttribuut(field=TimeField)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, time))

    def test_dummy_KeuzelijstField(self):
        attr = OTLAttribuut(field=KlTestKeuzelijst)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertTrue(isinstance(generated_dummy_waarde, str))
        self.assertTrue(generated_dummy_waarde in attr.field.options.keys())

    def test_dummy_KwantWrdField(self):
        attr = OTLAttribuut(field=KwantWrdTest)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertIsNotNone(generated_dummy_waarde.waarde)
        self.assertEqual(generated_dummy_waarde.standaardEenheid, '%')

    def test_dummy_ComplexField(self):
        attr = OTLAttribuut(field=DtcTestComplexType)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        self.assertIsNotNone(generated_dummy_waarde.testStringFieldMetKard)
        self.assertIsNotNone(generated_dummy_waarde.testBooleanField)
        self.assertIsNotNone(generated_dummy_waarde.testComplexType2)
        self.assertIsNotNone(generated_dummy_waarde.testComplexType2MetKard[0].testKwantWrd.waarde)

    def test_dummy_UnionField(self):
        attr = OTLAttribuut(field=DtuTestUnionType)
        attr.fill_with_dummy_data()

        generated_dummy_waarde = attr.get_waarde()
        self.assertIsNotNone(generated_dummy_waarde)
        first = generated_dummy_waarde.unionKwantWrd.waarde is not None
        second = generated_dummy_waarde.unionString is not None
        self.assertTrue(first != second)  # either first or second is True, but not both


