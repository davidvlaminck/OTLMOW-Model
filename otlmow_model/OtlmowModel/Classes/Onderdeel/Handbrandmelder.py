# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Handbrandmelder(NaampadObject, PuntGeometrie):
    """Een handmatig te bedienen toestel waarmee iemand bij het vaststellen van brand een brandalarm kan activeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handbrandmelder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
