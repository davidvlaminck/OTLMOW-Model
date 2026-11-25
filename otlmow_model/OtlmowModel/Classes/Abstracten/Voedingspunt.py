# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedingspunt(AIMNaamObject):
    """Abstracte voor het aansluitpunt van de voeding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Voedingspunt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
