# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeBevestigingHijspunt import KlTypeBevestigingHijspunt
from ...Datatypes.KwantWrdInKiloNewton import (
    KwantWrdInKiloNewton,
    KwantWrdInKiloNewtonWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hijspunt(AIMNaamObject, PuntGeometrie):
    """Een vast bevestigingspunt, gemonteerd aan de bouwkundige constructie, waaraan een takel kan worden opgehangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijspunt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Portiek', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Takel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HijsEnHefwerktuig', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._maximaleWerklast = OTLAttribuut(field=KwantWrdInKiloNewton,
                                              naam='maximaleWerklast',
                                              label='maximale werklast',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijspunt.maximaleWerklast',
                                              definition='De maximaal toegelaten belasting die het hijspunt kan opnemen en overdragen in kilonewton.',
                                              owner=self)

        self._typeBevestiging = OTLAttribuut(field=KlTypeBevestigingHijspunt,
                                             naam='typeBevestiging',
                                             label='type bevestiging',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijspunt.typeBevestiging',
                                             definition='De wijze waarop het hijspunt aan het constructie-element is bevestigd.',
                                             owner=self)

    @property
    def maximaleWerklast(self) -> KwantWrdInKiloNewtonWaarden:
        """De maximaal toegelaten belasting die het hijspunt kan opnemen en overdragen in kilonewton."""
        return self._maximaleWerklast.get_waarde()

    @maximaleWerklast.setter
    def maximaleWerklast(self, value):
        self._maximaleWerklast.set_waarde(value, owner=self)

    @property
    def typeBevestiging(self) -> str:
        """De wijze waarop het hijspunt aan het constructie-element is bevestigd."""
        return self._typeBevestiging.get_waarde()

    @typeBevestiging.setter
    def typeBevestiging(self, value):
        self._typeBevestiging.set_waarde(value, owner=self)
