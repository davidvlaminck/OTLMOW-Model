# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlRetroreflecterendeKokerFolieType import (
    KlRetroreflecterendeKokerFolieType,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroReflecterendeKoker(AIMObject, PuntGeometrie):
    """Een kunststoffen koker bevestigd rond een steun om de zichtbaarheid van verkeerseilanden te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._folieType = OTLAttribuut(field=KlRetroreflecterendeKokerFolieType,
                                       naam='folieType',
                                       label='folie type',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker.folieType',
                                       definition='Een keuzelijst het folietype van reflecterende koker te bepalen.',
                                       owner=self)

    @property
    def folieType(self) -> str:
        """Een keuzelijst het folietype van reflecterende koker te bepalen."""
        return self._folieType.get_waarde()

    @folieType.setter
    def folieType(self, value):
        self._folieType.set_waarde(value, owner=self)
