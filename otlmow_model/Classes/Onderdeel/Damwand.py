# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.ConstructieElement import ConstructieElement
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlDamwandMateriaal import KlDamwandMateriaal
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Damwand(ConstructieElement, LijnGeometrie):
    """Een grond- en/of waterkerende constructie,die bestaat uit een verticaal in de grond geplaatste wand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.8.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', deprecated='2.8.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', deprecated='2.8.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', deprecated='2.8.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', deprecated='2.8.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', deprecated='2.8.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput', deprecated='2.8.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf', deprecated='2.8.0')

        self._isWaterdicht = OTLAttribuut(field=BooleanField,
                                          naam='isWaterdicht',
                                          label='is waterdicht',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.isWaterdicht',
                                          usagenote='Klasse uit gebruik sinds versie 2.8.0 ',
                                          deprecated_version='2.8.0',
                                          definition='Geeft aan of de damwand al dan niet waterdicht is.',
                                          owner=self)

        self._materiaal = OTLAttribuut(field=KlDamwandMateriaal,
                                       naam='materiaal',
                                       label='Damwand materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.materiaal',
                                       usagenote='Klasse uit gebruik sinds versie 2.8.0 ',
                                       deprecated_version='2.8.0',
                                       definition='Het materiaal waaruit de damwand bestaat.',
                                       owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.oppervlakte',
                                         usagenote='Klasse uit gebruik sinds versie 2.8.0 ',
                                         deprecated_version='2.8.0',
                                         definition='De totale oppervlakte van de damwandconstructie in vierkante meter.',
                                         owner=self)

        self._profiellengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='profiellengte',
                                           label='profiellengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.profiellengte',
                                           usagenote='Klasse uit gebruik sinds versie 2.8.0 ',
                                           deprecated_version='2.8.0',
                                           definition='De lengte van één damwandprofiel.',
                                           owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand.totaleLengte',
                                          usagenote='Klasse uit gebruik sinds versie 2.8.0 ',
                                          deprecated_version='2.8.0',
                                          definition='De totale lengte van de damwandconstructie in lopende meter.',
                                          owner=self)

    @property
    def isWaterdicht(self) -> bool:
        """Geeft aan of de damwand al dan niet waterdicht is."""
        return self._isWaterdicht.get_waarde()

    @isWaterdicht.setter
    def isWaterdicht(self, value):
        self._isWaterdicht.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de damwand bestaat."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De totale oppervlakte van de damwandconstructie in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def profiellengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van één damwandprofiel."""
        return self._profiellengte.get_waarde()

    @profiellengte.setter
    def profiellengte(self, value):
        self._profiellengte.set_waarde(value, owner=self)

    @property
    def totaleLengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van de damwandconstructie in lopende meter."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)
