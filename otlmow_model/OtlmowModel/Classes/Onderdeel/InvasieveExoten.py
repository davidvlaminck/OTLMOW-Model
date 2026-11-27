# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.BegroeidVoorkomen import BegroeidVoorkomen
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class InvasieveExoten(BegroeidVoorkomen, PuntGeometrie, VlakGeometrie):
    """Invasieve exoten zijn planten die door menselijk handelen buiten hun natuurlijk verspreidingsgebied ('exoot') gebracht zijn en die in staat zijn zich op een natuurlijke wijze, al dan niet massaal, te verspreiden en hierbij schade (biodiversiteit, economisch, volksgezondheid) kunnen aanrichten ('invasief')."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InvasieveExoten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
