# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ConstructiefObject import ConstructiefObject
from otlmow_model.Datatypes.KlZijdenType import KlZijdenType
from otlmow_model.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kolom(ConstructiefObject, PuntGeometrie):
    """Een verticale constructie die dient als drager en bestaat uit een zuil of pilaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        ConstructiefObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler')

        self._hellingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                          naam='hellingshoek',
                                          label='hellingshoek',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom.hellingshoek',
                                          definition='De hoek die het object maakt met het grondvlak, uitgedrukt in decimale graden.',
                                          owner=self)

        self._zijden = OTLAttribuut(field=KlZijdenType,
                                    naam='zijden',
                                    label='zijden',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom.zijden',
                                    definition='Het type van de zijden dat de kolom heeft (recht, rond, schuin,...)',
                                    owner=self)

    @property
    def hellingshoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """De hoek die het object maakt met het grondvlak, uitgedrukt in decimale graden."""
        return self._hellingshoek.get_waarde()

    @hellingshoek.setter
    def hellingshoek(self, value):
        self._hellingshoek.set_waarde(value, owner=self)

    @property
    def zijden(self) -> str:
        """Het type van de zijden dat de kolom heeft (recht, rond, schuin,...)"""
        return self._zijden.get_waarde()

    @zijden.setter
    def zijden(self, value):
        self._zijden.set_waarde(value, owner=self)
