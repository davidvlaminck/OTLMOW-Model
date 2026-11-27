# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlBouwputType import KlBouwputType
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bouwput(AIMObject, VlakGeometrie):
    """De ontgraving die nodig is voor het maken van een ondergrondse constructie zoals bv. een put of putten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand', 'u', '2.8.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._putdiepte = OTLAttribuut(field=KwantWrdInMeter,
                                       naam='putdiepte',
                                       label='putdiepte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.putdiepte',
                                       definition='Diepte tussen het maaiveld en onderkant bouwput in meter.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlBouwputType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.type',
                                  definition='Het type van bouwput.',
                                  owner=self)

    @property
    def putdiepte(self) -> KwantWrdInMeterWaarden:
        """Diepte tussen het maaiveld en onderkant bouwput in meter."""
        return self._putdiepte.get_waarde()

    @putdiepte.setter
    def putdiepte(self, value):
        self._putdiepte.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van bouwput."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
