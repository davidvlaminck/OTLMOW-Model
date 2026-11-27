# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.Verkeerslicht import Verkeerslicht


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeerslichtWit(Verkeerslicht):
    """Een witte lichtbron om het verkeer te regelen van voertuigen van personentransport."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtWit'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
