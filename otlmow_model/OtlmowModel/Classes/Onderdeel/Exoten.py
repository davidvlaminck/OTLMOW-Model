# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.BegroeidVoorkomen import BegroeidVoorkomen
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Exoten(BegroeidVoorkomen, VlakGeometrie):
    """Exoten, in deze context, zijn planten die zich hebben gevestigd in België terwijl ze oorspronkelijk niet in België voorkwamen. Ze verdringen bovendien inheemse soorten uit hun normale groeiplaats."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Exoten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.1.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten', 'o', '2.1.0'),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
