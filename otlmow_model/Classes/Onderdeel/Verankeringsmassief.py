# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Betonfundering import Betonfundering
from otlmow_model.Classes.Abstracten.KlassiekeFundering import KlassiekeFundering
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verankeringsmassief(Betonfundering, KlassiekeFundering):
    """Een fundering waarin ankers zijn aangebracht en die zorgen voor bevestiging en stabilisatie van een object."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief'
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
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement', deprecated='2.5.0')

        self._isAfgedektMetBitumen = OTLAttribuut(field=BooleanField,
                                                  naam='isAfgedektMetBitumen',
                                                  label='is afgedekt met bitumen',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief.isAfgedektMetBitumen',
                                                  definition='Geeft aan of de fundering afgedekt is met een waterbestendige laag die regenwater en vuil wegvoert van de fundering.',
                                                  owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief.volume',
                                    definition='Het volume in kubieke meter van het verankeringsmassief.',
                                    owner=self)

    @property
    def isAfgedektMetBitumen(self) -> bool:
        """Geeft aan of de fundering afgedekt is met een waterbestendige laag die regenwater en vuil wegvoert van de fundering."""
        return self._isAfgedektMetBitumen.get_waarde()

    @isAfgedektMetBitumen.setter
    def isAfgedektMetBitumen(self, value):
        self._isAfgedektMetBitumen.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume in kubieke meter van het verankeringsmassief."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
