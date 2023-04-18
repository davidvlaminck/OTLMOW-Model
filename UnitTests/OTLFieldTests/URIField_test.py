from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.BaseClasses.URIField import URIField


def test_validate():
    uri_attribute = OTLAttribuut(naam='uri attribuut')
    assert not URIField.validate('a', uri_attribute)
    assert URIField.validate("http://www.example.com", uri_attribute)
