# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class EMAfbakening(AIMNaamObject):
    """Een abstracte klasse voor de Voedt- en Sturing-relaties van allerlei types elektromechansiche afbakening (anders dan de gewone openbare verlichting) in en langs de weg"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMAfbakening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
