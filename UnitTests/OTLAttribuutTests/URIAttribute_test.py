import pytest

from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.URIField import URIField
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


class NonStringableObject(object):
    def __str__(self):
        pass


def test_full_test_on_testclass_kard_1(subtests):
    uri_attr = OTLAttribuut(naam='uriveld', field=URIField)
    with subtests.test(msg='assign values to URIfield with kard 1'):
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            uri_attr.set_waarde(NonStringableObject())
        with pytest.raises(ValueError):
            uri_attr.set_waarde('not_a_uri')
        uri_attr.set_waarde('http://www.google.com')
        assert uri_attr.waarde == 'http://www.google.com'
        uri_attr.set_waarde('/eminfra/core/api/otl/assets/0-0/documenten/0')
        assert uri_attr.waarde == 'https://apps.mow.vlaanderen.be/eminfra/core/api/otl/assets/0-0/documenten/0'
