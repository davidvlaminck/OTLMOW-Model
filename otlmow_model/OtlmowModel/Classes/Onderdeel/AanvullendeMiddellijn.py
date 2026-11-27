# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import (
    AbstracteAanvullendeGeometrie,
)
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanvullendeMiddellijn(AbstracteAanvullendeGeometrie, LijnGeometrie):
    """Een lijn die het midden of de centrale as van een object markeert, zoals bv. de centrale as van een gracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AanvullendeMiddellijn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
