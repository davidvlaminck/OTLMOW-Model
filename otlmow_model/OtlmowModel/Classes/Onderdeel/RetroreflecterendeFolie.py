# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlFolieType import KlFolieType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroreflecterendeFolie(AIMObject, PuntGeometrie):
    """Retroreflecterend bekledingsmateriaal, bijvoorbeeld van een divergentiepuntbebakeningselement, retroreflecterende koker, of het beeldvlak van een retroreflecterend verkeersbord."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._folietype = OTLAttribuut(field=KlFolieType,
                                       naam='folietype',
                                       label='folietype',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie.folietype',
                                       definition='Het type folie dat bevestigd is aan het retroreflecterend verkeersbord.',
                                       owner=self)

    @property
    def folietype(self) -> str:
        """Het type folie dat bevestigd is aan het retroreflecterend verkeersbord."""
        return self._folietype.get_waarde()

    @folietype.setter
    def folietype(self, value):
        self._folietype.set_waarde(value, owner=self)
