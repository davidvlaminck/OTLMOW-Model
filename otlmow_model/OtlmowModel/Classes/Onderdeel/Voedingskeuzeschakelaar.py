# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedingskeuzeschakelaar(NaampadObject, PuntGeometrie):
    """Deze schakelaar biedt de mogelijkheid om handmatig over te schakelen tussen de twee voedingsbronnen om continuïteit van elektrische stroom te behouden,zelfs wanneer de reguliere stroomvoorziening tijdelijk niet beschikbaar is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskeuzeschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
