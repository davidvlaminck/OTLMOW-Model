# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Put import Put
from ...Classes.Abstracten.PutRelatie import PutRelatie
from ...Datatypes.DtcAfmetingBxlInCm import (
    DtcAfmetingBxlInCm,
    DtcAfmetingBxlInCmWaarden,
)
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aswegerput(Put, PutRelatie, VlakGeometrie):
    """Een ondergrondse constructie die de elektronica van een asweger bevat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afmetingGrondvlak = OTLAttribuut(field=DtcAfmetingBxlInCm,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput.afmetingGrondvlak',
                                               definition='De binnenafmeting, breedte en lengte in cm van de aswegerput ter hoogte van het maaiveld.',
                                               owner=self)

    @property
    def afmetingGrondvlak(self) -> DtcAfmetingBxlInCmWaarden:
        """De binnenafmeting, breedte en lengte in cm van de aswegerput ter hoogte van het maaiveld."""
        return self._afmetingGrondvlak.get_waarde()

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)
