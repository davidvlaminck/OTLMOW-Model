# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trappentoren(AanhorigheidKoker, AIMNaamObject, VlakGeometrie):
    """Een trappentoren is een geïntegreerde constructie van trappen die kan dienen om 1 of meerdere niveaus te beklimmen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trappentoren'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.12.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', 'u', '2.12.0'),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
