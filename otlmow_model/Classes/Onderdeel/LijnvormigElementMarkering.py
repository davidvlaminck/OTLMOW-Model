# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.AOWSType import AOWSType
from otlmow_model.Classes.Abstracten.Markering import Markering
from otlmow_model.Datatypes.KlLEMarkeringCode import KlLEMarkeringCode
from otlmow_model.Datatypes.KlLEMarkeringSoort import KlLEMarkeringSoort
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LijnvormigElementMarkering(Markering, AOWSType, LijnGeometrie):
    """Een markering van een lijnvormig element om de zichtbaarheid te verhogen om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Markering.__init__(self)
        AOWSType.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering')

        self._code = OTLAttribuut(field=KlLEMarkeringCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.code',
                                  definition='De (COPRO/BENOR) code van de lijnvormig element markering.',
                                  owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.lengte',
                                    definition='De lengte van de markering in meter.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.oppervlakte',
                                         definition='De oppervlakte van de markering op het lijnvormig element in vierkante meter.',
                                         owner=self)

        self._soortOmschrijving = OTLAttribuut(field=KlLEMarkeringSoort,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van de lijnvormige elementen markering.',
                                               owner=self)

    @property
    def code(self) -> str:
        """De (COPRO/BENOR) code van de lijnvormig element markering."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de markering in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de markering op het lijnvormig element in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self) -> str:
        """De soort en tevens de omschrijving van de lijnvormige elementen markering."""
        return self._soortOmschrijving.get_waarde()

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)
