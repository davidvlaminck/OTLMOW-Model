# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Weegsensorgroep(NaampadObject):
    """Een groep om weegsensoren te groeperen binnen het thema DIZV."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Weegsensorgroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DIZV', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor', direction='i')  # i = direction: incoming
