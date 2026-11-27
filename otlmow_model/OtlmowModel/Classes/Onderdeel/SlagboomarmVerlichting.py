# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SlagboomarmVerlichting(AIMObject, LijnGeometrie):
    """Verlichting bevestigd aan de slagboomarm om de zichtbaarheid van die arm te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
