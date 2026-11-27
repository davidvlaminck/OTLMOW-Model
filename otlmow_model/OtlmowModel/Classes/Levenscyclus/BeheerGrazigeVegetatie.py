# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcMaaien import DtcMaaien, DtcMaaienWaarden
from ...Datatypes.KlBeheerGrazigeVegetatie import KlBeheerGrazigeVegetatie
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import (
    KwantWrdInVierkanteMeter,
    KwantWrdInVierkanteMeterWaarden,
)
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerGrazigeVegetatie(AIMObject, VlakGeometrie):
    """Het beheerobject voor de grazige vegetatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasland', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasmat', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ruigte', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._beheeroptie = OTLAttribuut(field=KlBeheerGrazigeVegetatie,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.beheeroptie',
                                         kardinaliteit_max='*',
                                         definition='Aanduiding van welk beheer wordt toegepast op de grazige vegetatie.',
                                         owner=self)

        self._heeftBeheerplan = OTLAttribuut(field=BooleanField,
                                             naam='heeftBeheerplan',
                                             label='heeft beheerplan',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.heeftBeheerplan',
                                             definition='Aanduiding of er een beheerplan bestaat.',
                                             owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.lengte',
                                    definition='De lengte in meter van de te behandelen grazige vegetatie.',
                                    owner=self)

        self._maaien = OTLAttribuut(field=DtcMaaien,
                                    naam='maaien',
                                    label='maaien',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.maaien',
                                    definition='Complex datatype voor de eigenschappen van maaien.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen grazige vegetatie.',
                                         owner=self)

    @property
    def beheeroptie(self) -> list[str]:
        """Aanduiding van welk beheer wordt toegepast op de grazige vegetatie."""
        return self._beheeroptie.get_waarde()

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def heeftBeheerplan(self) -> bool:
        """Aanduiding of er een beheerplan bestaat."""
        return self._heeftBeheerplan.get_waarde()

    @heeftBeheerplan.setter
    def heeftBeheerplan(self, value):
        self._heeftBeheerplan.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte in meter van de te behandelen grazige vegetatie."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def maaien(self) -> DtcMaaienWaarden:
        """Complex datatype voor de eigenschappen van maaien."""
        return self._maaien.get_waarde()

    @maaien.setter
    def maaien(self, value):
        self._maaien.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte in vierkante meter van de te behandelen grazige vegetatie."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
