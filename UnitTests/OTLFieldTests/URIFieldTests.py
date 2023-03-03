from unittest import TestCase

from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.URIField import URIField


class URIFieldTests(TestCase):
    def test_validate(self):
        uri_attribute = OTLAttribuut(naam='uri attribuut')
        self.assertFalse(URIField.validate('a', uri_attribute))
        self.assertTrue(URIField.validate("http://www.example.com", uri_attribute))
