# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlAanvaarbeschermingType import KlAanvaarbeschermingType
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aanvaarbescherming(AIMNaamObject, PuntGeometrie, LijnGeometrie):
    """Constructie om schepen te geleiden en/of te verhinderen dat ze ergens tegenaan botsen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanvaarbescherming'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanvaarbescherming.lengte',
                                    definition='De lengte, in meter, van de aanvaarbescherming.',
                                    owner=self)

        self._typeAanvaarbescherming = OTLAttribuut(field=KlAanvaarbeschermingType,
                                                    naam='typeAanvaarbescherming',
                                                    label='Type aanvaarbescherming',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanvaarbescherming.typeAanvaarbescherming',
                                                    definition='De soort van aanvaarbescherming.',
                                                    owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte, in meter, van de aanvaarbescherming."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def typeAanvaarbescherming(self) -> str:
        """De soort van aanvaarbescherming."""
        return self._typeAanvaarbescherming.get_waarde()

    @typeAanvaarbescherming.setter
    def typeAanvaarbescherming(self, value):
        self._typeAanvaarbescherming.set_waarde(value, owner=self)
