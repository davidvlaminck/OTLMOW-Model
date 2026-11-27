# coding=utf-8
from typing import ClassVar

from ...BaseClasses.IntegerField import IntegerField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Buis import Buis
from ...Classes.Abstracten.BVAfwateringKunstwerken import BVAfwateringKunstwerken
from ...Datatypes.KlRioleringsbuisFunctie import KlRioleringsbuisFunctie
from ...Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal
from ...Datatypes.KlSterktereeks import KlSterktereeks
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rioleringsbuis(BVAfwateringKunstwerken, Buis, PuntGeometrie):
    """Een kanaal of pijp voor gravitaire afvoer van water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecokoker', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WaterdoorvoerendeDuiker', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taludgoot', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', '2.8.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aantalAfgedichteAansluitingen = OTLAttribuut(field=IntegerField,
                                                           naam='aantalAfgedichteAansluitingen',
                                                           label='aantal afgedichte aansluitingen',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.aantalAfgedichteAansluitingen',
                                                           definition='De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis.',
                                                           owner=self)

        self._functie = OTLAttribuut(field=KlRioleringsbuisFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.functie',
                                     definition='Bepaalt de functie van de rioleringsbuis.',
                                     owner=self)

        self._materiaal = OTLAttribuut(field=KlRioleringsbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.materiaal',
                                       definition='Bepaalt het materiaal van de rioleringsbuis.',
                                       owner=self)

        self._sterktereeks = OTLAttribuut(field=KlSterktereeks,
                                          naam='sterktereeks',
                                          label='sterktereeks',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.sterktereeks',
                                          definition='De stabiliteitsklasse van de buis.',
                                          owner=self)

    @property
    def aantalAfgedichteAansluitingen(self) -> int:
        """De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis."""
        return self._aantalAfgedichteAansluitingen.get_waarde()

    @aantalAfgedichteAansluitingen.setter
    def aantalAfgedichteAansluitingen(self, value):
        self._aantalAfgedichteAansluitingen.set_waarde(value, owner=self)

    @property
    def functie(self) -> str:
        """Bepaalt de functie van de rioleringsbuis."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de rioleringsbuis."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sterktereeks(self) -> str:
        """De stabiliteitsklasse van de buis."""
        return self._sterktereeks.get_waarde()

    @sterktereeks.setter
    def sterktereeks(self, value):
        self._sterktereeks.set_waarde(value, owner=self)
