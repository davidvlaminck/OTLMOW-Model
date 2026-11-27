# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInCentimeter import (
    KwantWrdInCentimeter,
    KwantWrdInCentimeterWaarden,
)
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bodembescherming(AIMNaamObject, VlakGeometrie):
    """Een constructieve maatregel om de onderwaterbodem te beschermen tegen erosie en andere vormen van schade."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fuik', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Asfaltmat', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmat', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmatras', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiepenmat', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming.dikte',
                                   definition='De dikte van de bodembescherming uitgedrukt in cm',
                                   owner=self)

        self._heeftVoegen = OTLAttribuut(field=BooleanField,
                                         naam='heeftVoegen',
                                         label='heeft voegen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming.heeftVoegen',
                                         definition='Geeft aan of de bodembescherming al dan niet voegen heeft',
                                         owner=self)

        self._isWaterdoorlatend = OTLAttribuut(field=BooleanField,
                                               naam='isWaterdoorlatend',
                                               label='is waterdoorlatend',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming.isWaterdoorlatend',
                                               definition='Geeft aan of de bodembescherming al dan niet waterdoorlatend is.',
                                               owner=self)

    @property
    def dikte(self) -> KwantWrdInCentimeterWaarden:
        """De dikte van de bodembescherming uitgedrukt in cm"""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def heeftVoegen(self) -> bool:
        """Geeft aan of de bodembescherming al dan niet voegen heeft"""
        return self._heeftVoegen.get_waarde()

    @heeftVoegen.setter
    def heeftVoegen(self, value):
        self._heeftVoegen.set_waarde(value, owner=self)

    @property
    def isWaterdoorlatend(self) -> bool:
        """Geeft aan of de bodembescherming al dan niet waterdoorlatend is."""
        return self._isWaterdoorlatend.get_waarde()

    @isWaterdoorlatend.setter
    def isWaterdoorlatend(self, value):
        self._isWaterdoorlatend.set_waarde(value, owner=self)
