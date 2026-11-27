# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.GrazigeVegetatie import GrazigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grasmat(GrazigeVegetatie):
    """Grasvegetatie die een uniforme zode vormt met veel grassen en zeer regelmatig wordt gemaaid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasmat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
