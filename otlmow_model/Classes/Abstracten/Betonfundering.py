# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Fundering import Fundering
from otlmow_model.Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM, DtcAfmetingBxlInMWaarden
from otlmow_model.Datatypes.KlFunderingBetonkwaliteit import KlFunderingBetonkwaliteit
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Betonfundering(Fundering, VlakGeometrie):
    """Abstracte voor funderingen in beton."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', deprecated='2.0.0')

        self._afmetingGrondvlak = OTLAttribuut(field=DtcAfmetingBxlInM,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.afmetingGrondvlak',
                                               usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                               deprecated_version='2.0.0',
                                               definition='De maximale lengte en breedte van bovenkant van de fundering.',
                                               owner=self)

        self._betonkwaliteit = OTLAttribuut(field=KlFunderingBetonkwaliteit,
                                            naam='betonkwaliteit',
                                            label='betonkwaliteit',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.betonkwaliteit',
                                            usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                            deprecated_version='2.0.0',
                                            definition='Kwaliteit van het beton gebruikt voor de fundering volgens een vaste lijst van mogelijke waarden.',
                                            owner=self)

    @property
    def afmetingGrondvlak(self) -> DtcAfmetingBxlInMWaarden:
        """De maximale lengte en breedte van bovenkant van de fundering."""
        return self._afmetingGrondvlak.get_waarde()

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)

    @property
    def betonkwaliteit(self) -> str:
        """Kwaliteit van het beton gebruikt voor de fundering volgens een vaste lijst van mogelijke waarden."""
        return self._betonkwaliteit.get_waarde()

    @betonkwaliteit.setter
    def betonkwaliteit(self, value):
        self._betonkwaliteit.set_waarde(value, owner=self)
