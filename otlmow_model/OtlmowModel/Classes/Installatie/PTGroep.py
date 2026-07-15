# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTGroep(NaampadObject):
    """Groep voor het groeperen van objecten van het type personentransportmodules."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PTGroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar', direction='i')  # i = direction: incoming
