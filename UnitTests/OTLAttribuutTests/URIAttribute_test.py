from unittest import TestCase

from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut

from otlmow_model.BaseClasses.URIField import URIField

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


class NonStringableObject(object):
    def __str__(self):
        pass


class StringAttributeTests(TestCase):
    def test_full_test_on_testclass_kard_1(self):
        uri_attr = OTLAttribuut(naam='uriveld', field=URIField)

        with self.subTest('assign values to URIfield with kard 1'):
            with self.assertRaises(CouldNotConvertToCorrectTypeError):
                uri_attr.set_waarde(NonStringableObject())
            uri_attr.set_waarde('http://www.google.com')
            self.assertEqual('http://www.google.com', uri_attr.waarde)
            uri_attr.set_waarde('/eminfra/core/api/otl/assets/0-0/documenten/0')
            self.assertEqual('https://apps.mow.vlaanderen.be/eminfra/core/api/otl/assets/0-0/documenten/0', uri_attr.waarde)
