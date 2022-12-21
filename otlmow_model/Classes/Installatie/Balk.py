# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ConstructiefObject import ConstructiefObject
from otlmow_model.Datatypes.KlTypeBalk import KlTypeBalk
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Balk(ConstructiefObject, LijnGeometrie):
    """Ruimteoverspannend enkelvoudig constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. De breedte is weer gelijk of kleiner dan de hoogte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        ConstructiefObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanvaarbescherming')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler')

        self._typeBalk = OTLAttribuut(field=KlTypeBalk,
                                      naam='typeBalk',
                                      label='type balk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk.typeBalk',
                                      definition='De soort van balk.',
                                      owner=self)

    @property
    def typeBalk(self) -> str:
        """De soort van balk."""
        return self._typeBalk.get_waarde()

    @typeBalk.setter
    def typeBalk(self, value):
        self._typeBalk.set_waarde(value, owner=self)
