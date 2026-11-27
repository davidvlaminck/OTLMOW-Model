# coding=utf-8
from abc import ABC, abstractmethod
from typing import ClassVar


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanhorigheidKoker(ABC):
    """Een abstracte klasse die de aanhorigheden bundelt die in een koker kunnen voorkomen zodat de overerving van de bevestigingsrelatie kan plaatsvinden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidKoker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie', 'u', None),  # u = unidirectional
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
