# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.HoutenConstructieElement import HoutenConstructieElement
from otlmow_model.Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoutenHeipaal(HoutenConstructieElement, Funderingspaal):
    """De houten paal wordt in de grond gebracht door deze in een hei-installatie te plaatsen waarna men er een zwaar gewicht (heiblok) op laat vallen. De grond onder de paal wordt verdreven en verdicht waardoor de draagkracht groter wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenHeipaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')

        self._diameterPaalschacht = OTLAttribuut(field=KwantWrdInCentimeter,
                                                 naam='diameterPaalschacht',
                                                 label='diameter paalschacht',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenHeipaal.diameterPaalschacht',
                                                 definition='Diameter van de paalschacht in centimeter.',
                                                 owner=self)

    @property
    def diameterPaalschacht(self) -> KwantWrdInCentimeterWaarden:
        """Diameter van de paalschacht in centimeter."""
        return self._diameterPaalschacht.get_waarde()

    @diameterPaalschacht.setter
    def diameterPaalschacht(self, value):
        self._diameterPaalschacht.set_waarde(value, owner=self)
