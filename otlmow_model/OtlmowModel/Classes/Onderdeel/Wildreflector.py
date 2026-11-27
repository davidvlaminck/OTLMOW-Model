# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Bebakening import Bebakening
from ...Datatypes.KlWildreflectorDrager import KlWildreflectorDrager
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wildreflector(Bebakening, PuntGeometrie):
    """Een wildreflector is een reflecterend afschrikkingssysteem voor groot en klein wild nabij een weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Reflectorpaal', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._drager = OTLAttribuut(field=KlWildreflectorDrager,
                                    naam='drager',
                                    label='drager',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector.drager',
                                    definition='De constructie waar de wildreflector is aan bevestigd.',
                                    owner=self)

    @property
    def drager(self) -> str:
        """De constructie waar de wildreflector is aan bevestigd."""
        return self._drager.get_waarde()

    @drager.setter
    def drager(self, value):
        self._drager.set_waarde(value, owner=self)
