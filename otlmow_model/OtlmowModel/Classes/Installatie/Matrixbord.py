# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Matrixbord(AIMObject, PuntGeometrie):
    """De elektronische displays die in de wanden van een tunnel zijn ingebouwd en die belangrijke informatie aan weggebruikers tonen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Matrixbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.10.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat', 'i', '2.10.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK', 'i', '2.15.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS', 'i', '2.10.0'),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
