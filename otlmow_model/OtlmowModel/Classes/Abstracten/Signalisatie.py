# coding=utf-8
from abc import ABC, abstractmethod
from typing import ClassVar


# Generated with OTLClassCreator. To modify: extend, do not edit
class Signalisatie(ABC):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties van signalisatie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Signalisatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam', 'u', '2.11.0'),  # u = unidirectional
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
