# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Berlinerwand(Grondkeringen, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Een damwandconstructie, opgebouwd uit stalen H-profielen en (stalen)planken. De berlinerwand wordt vooral toegepast als grondkering bij bouwputten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeBerlinerwandTussenschot', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenPredal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenConstructieprofiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenPlaat', direction='i')  # i = direction: incoming

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
