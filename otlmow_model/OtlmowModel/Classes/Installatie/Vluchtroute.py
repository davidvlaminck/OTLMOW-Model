# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vluchtroute(AIMNaamObject, VlakGeometrie):
    """Verzameling van technieken die de routes waarlangs de weggebruiker het kunstwerk kan verlaten aanduiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtroute'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtdeurindicatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtgeleiding', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
