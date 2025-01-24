# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcMeteoFoto import DtcMeteoFoto, DtcMeteoFotoWaarden
from ...Datatypes.KlLokaalTerreinType import KlLokaalTerreinType
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetstation(NaampadObject, PuntGeometrie):
    """De plaats waar verschillende sensoren samen 1 meetstation vormen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.14.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='i', deprecated='2.14.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='i', deprecated='2.14.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', direction='i', deprecated='2.14.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='i', deprecated='2.14.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor', direction='i', deprecated='2.14.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', direction='i', deprecated='2.14.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', direction='i', deprecated='2.14.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt', direction='i', deprecated='2.14.0')  # i = direction: incoming

        self._beoordelingLokaleTerrein = OTLAttribuut(field=KlLokaalTerreinType,
                                                      naam='beoordelingLokaleTerrein',
                                                      label='beoordeling lokale terrein',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.beoordelingLokaleTerrein',
                                                      usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                                      deprecated_version='2.14.0',
                                                      kardinaliteit_max='*',
                                                      definition='Het soort terrein waarin het meetstation staat met betrekking tot het reliëf en de vegetatie.',
                                                      owner=self)

        self._foto = OTLAttribuut(field=DtcMeteoFoto,
                                  naam='foto',
                                  label='foto',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.foto',
                                  usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                  deprecated_version='2.14.0',
                                  kardinaliteit_max='*',
                                  definition="De verschillende foto's van het meetstation.",
                                  owner=self)

        self._keuringsrapport = OTLAttribuut(field=DtcDocument,
                                             naam='keuringsrapport',
                                             label='keuringsrapport',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.keuringsrapport',
                                             usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                             deprecated_version='2.14.0',
                                             kardinaliteit_max='*',
                                             definition='Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation.',
                                             owner=self)

        self._masterOfBridgeSensor = OTLAttribuut(field=BooleanField,
                                                  naam='masterOfBridgeSensor',
                                                  label='master of bridge sensor',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.masterOfBridgeSensor',
                                                  usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                                  deprecated_version='2.14.0',
                                                  definition='Geeft aan of het meetstation ingeplant is ter hoogte van een brug.',
                                                  owner=self)

        self._nabijheidVanHindernissen = OTLAttribuut(field=KwantWrdInMeter,
                                                      naam='nabijheidVanHindernissen',
                                                      label='nabijheid van hindernissen',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.nabijheidVanHindernissen',
                                                      usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                                      deprecated_version='2.14.0',
                                                      kardinaliteit_max='*',
                                                      definition='De afstand tot een hindernis in de nabijheid.',
                                                      owner=self)

        self._nabijheidVanWaterlopen = OTLAttribuut(field=KwantWrdInMeter,
                                                    naam='nabijheidVanWaterlopen',
                                                    label='nabijheid van waterlopen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.nabijheidVanWaterlopen',
                                                    usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                                    deprecated_version='2.14.0',
                                                    kardinaliteit_max='*',
                                                    definition='De afstand tot een waterloop in de nabijheid.',
                                                    owner=self)

        self._onderhoudsrapport = OTLAttribuut(field=DtcDocument,
                                               naam='onderhoudsrapport',
                                               label='onderhoudsrapport',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.onderhoudsrapport',
                                               usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                               deprecated_version='2.14.0',
                                               kardinaliteit_max='*',
                                               definition='Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation.',
                                               owner=self)

        self._sitePhysicsRapport = OTLAttribuut(field=DtcDocument,
                                                naam='sitePhysicsRapport',
                                                label='site physics rapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.sitePhysicsRapport',
                                                usagenote='Klasse uit gebruik sinds versie 2.14.0 ',
                                                deprecated_version='2.14.0',
                                                kardinaliteit_max='*',
                                                definition='Beschrijvend overzichtsrapport van het meteostation.',
                                                owner=self)

    @property
    def beoordelingLokaleTerrein(self) -> List[str]:
        """Het soort terrein waarin het meetstation staat met betrekking tot het reliëf en de vegetatie."""
        return self._beoordelingLokaleTerrein.get_waarde()

    @beoordelingLokaleTerrein.setter
    def beoordelingLokaleTerrein(self, value):
        self._beoordelingLokaleTerrein.set_waarde(value, owner=self)

    @property
    def foto(self) -> List[DtcMeteoFotoWaarden]:
        """De verschillende foto's van het meetstation."""
        return self._foto.get_waarde()

    @foto.setter
    def foto(self, value):
        self._foto.set_waarde(value, owner=self)

    @property
    def keuringsrapport(self) -> List[DtcDocumentWaarden]:
        """Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation."""
        return self._keuringsrapport.get_waarde()

    @keuringsrapport.setter
    def keuringsrapport(self, value):
        self._keuringsrapport.set_waarde(value, owner=self)

    @property
    def masterOfBridgeSensor(self) -> bool:
        """Geeft aan of het meetstation ingeplant is ter hoogte van een brug."""
        return self._masterOfBridgeSensor.get_waarde()

    @masterOfBridgeSensor.setter
    def masterOfBridgeSensor(self, value):
        self._masterOfBridgeSensor.set_waarde(value, owner=self)

    @property
    def nabijheidVanHindernissen(self) -> List[KwantWrdInMeterWaarden]:
        """De afstand tot een hindernis in de nabijheid."""
        return self._nabijheidVanHindernissen.get_waarde()

    @nabijheidVanHindernissen.setter
    def nabijheidVanHindernissen(self, value):
        self._nabijheidVanHindernissen.set_waarde(value, owner=self)

    @property
    def nabijheidVanWaterlopen(self) -> List[KwantWrdInMeterWaarden]:
        """De afstand tot een waterloop in de nabijheid."""
        return self._nabijheidVanWaterlopen.get_waarde()

    @nabijheidVanWaterlopen.setter
    def nabijheidVanWaterlopen(self, value):
        self._nabijheidVanWaterlopen.set_waarde(value, owner=self)

    @property
    def onderhoudsrapport(self) -> List[DtcDocumentWaarden]:
        """Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation."""
        return self._onderhoudsrapport.get_waarde()

    @onderhoudsrapport.setter
    def onderhoudsrapport(self, value):
        self._onderhoudsrapport.set_waarde(value, owner=self)

    @property
    def sitePhysicsRapport(self) -> List[DtcDocumentWaarden]:
        """Beschrijvend overzichtsrapport van het meteostation."""
        return self._sitePhysicsRapport.get_waarde()

    @sitePhysicsRapport.setter
    def sitePhysicsRapport(self, value):
        self._sitePhysicsRapport.set_waarde(value, owner=self)
