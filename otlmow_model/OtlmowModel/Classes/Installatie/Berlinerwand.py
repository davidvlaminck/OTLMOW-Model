# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Berlinerwand(Grondkeringen, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Een damwandconstructie, opgebouwd uit stalen H-profielen en (stalen)planken. De berlinerwand wordt vooral toegepast als grondkering bij bouwputten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeBerlinerwandTussenschot', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenPredal', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenPlaat', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._totaleLengteWand = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='totaleLengteWand',
                                              label='totale lengte wand',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand.totaleLengteWand',
                                              definition='De totale horizontale lengte van de gehele berlinerwand in lopende meter.',
                                              owner=self)

        self._tussenafstandProfielen = OTLAttribuut(field=KwantWrdInMeter,
                                                    naam='tussenafstandProfielen',
                                                    label='tussenafstand profielen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand.tussenafstandProfielen',
                                                    definition='Afstand tussen verschillende profielen in meter.',
                                                    owner=self)

    @property
    def totaleLengteWand(self) -> KwantWrdInMeterWaarden:
        """De totale horizontale lengte van de gehele berlinerwand in lopende meter."""
        return self._totaleLengteWand.get_waarde()

    @totaleLengteWand.setter
    def totaleLengteWand(self, value):
        self._totaleLengteWand.set_waarde(value, owner=self)

    @property
    def tussenafstandProfielen(self) -> KwantWrdInMeterWaarden:
        """Afstand tussen verschillende profielen in meter."""
        return self._tussenafstandProfielen.get_waarde()

    @tussenafstandProfielen.setter
    def tussenafstandProfielen(self, value):
        self._tussenafstandProfielen.set_waarde(value, owner=self)
