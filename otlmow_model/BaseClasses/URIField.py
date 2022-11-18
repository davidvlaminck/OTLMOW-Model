from otlmow_model.BaseClasses.StringField import StringField


class URIField(StringField):
    """Een tekstwaarde die een verwijzing naar meer informatie van het element bevat volgens http://www.w3.org/2001/XMLSchema#anyURI ."""
    naam = 'AnyURI'
    objectUri = 'http://www.w3.org/2001/XMLSchema#anyURI'
    definition = 'Een tekstwaarde die een verwijzing naar meer informatie van het element bevat volgens http://www.w3.org/2001/XMLSchema#anyURI.'
    label = 'URI'
    usagenote = 'https://www.w3.org/TR/xmlschema-2/#anyURI'

    @staticmethod
    def validate(value, attribuut):
        return StringField.validate(value, attribuut)
        # TODO add URI validation

    def __str__(self):
        return StringField.__str__(self)

