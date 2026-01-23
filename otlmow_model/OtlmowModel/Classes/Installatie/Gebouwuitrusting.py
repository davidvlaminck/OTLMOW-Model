# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Gebouwuitrusting(NaampadObject, PuntGeometrie):
    """Een generiek type dat alle zaken omvat waarmee een gebouw kan worden uitgerust (bijvoorbeeld meubilair,verwarming...)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouwuitrusting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', direction='o')  # o = direction: outgoing
