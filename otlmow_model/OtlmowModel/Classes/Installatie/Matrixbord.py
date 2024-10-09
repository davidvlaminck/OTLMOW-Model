# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Matrixbord(AIMObject, PuntGeometrie):
    """De elektronische displays die in de wanden van een tunnel zijn ingebouwd en die belangrijke informatie aan weggebruikers tonen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Matrixbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.10.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat', direction='i', deprecated='2.10.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK', direction='i', deprecated='2.10.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS', direction='i', deprecated='2.10.0')  # i = direction: incoming
