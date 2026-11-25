# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Smeernippel(AIMNaamObject, PuntGeometrie):
    """Een koppelstuk dat een verbinding vormt met de binnenkant van het te smeren systeem. Dit aansluitingspunt laat toe om bijvoorbeeld manueel vet toe te dienen met een vetpomp."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Smeernippel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lagerblok', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
