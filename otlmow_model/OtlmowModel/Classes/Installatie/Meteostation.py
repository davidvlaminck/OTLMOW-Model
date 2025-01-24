# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.MeetstationAbstract import MeetstationAbstract
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlLokaalTerreinType import KlLokaalTerreinType
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meteostation(MeetstationAbstract, NaampadObject):
    """Het geheel van meteorologische sensoren en andere infrastructuurelementen die samen een meteostation vormen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', direction='i')  # i = direction: incoming

        self._beoordelingLokaleTerrein = OTLAttribuut(field=KlLokaalTerreinType,
                                                      naam='beoordelingLokaleTerrein',
                                                      label='beoordeling lokale terrein',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation.beoordelingLokaleTerrein',
                                                      kardinaliteit_max='*',
                                                      definition='Het soort terrein waarin het meetstation staat met betrekking tot het reliëf en de vegetatie.',
                                                      owner=self)

        self._masterOfBridgeSensor = OTLAttribuut(field=BooleanField,
                                                  naam='masterOfBridgeSensor',
                                                  label='master of bridge sensor',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation.masterOfBridgeSensor',
                                                  definition='Geeft aan of het meetstation ingeplant is ter hoogte van een brug.',
                                                  owner=self)

        self._nabijheidVanHindernissen = OTLAttribuut(field=KwantWrdInMeter,
                                                      naam='nabijheidVanHindernissen',
                                                      label='nabijheid van hindernissen',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation.nabijheidVanHindernissen',
                                                      kardinaliteit_max='*',
                                                      definition='De afstand tot een hindernis in de nabijheid.',
                                                      owner=self)

        self._nabijheidVanWaterlopen = OTLAttribuut(field=KwantWrdInMeter,
                                                    naam='nabijheidVanWaterlopen',
                                                    label='nabijheid van waterlopen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation.nabijheidVanWaterlopen',
                                                    kardinaliteit_max='*',
                                                    definition='De afstand tot een waterloop in de nabijheid.',
                                                    owner=self)

        self._sitePhysicsRapport = OTLAttribuut(field=DtcDocument,
                                                naam='sitePhysicsRapport',
                                                label='site physics rapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation.sitePhysicsRapport',
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
    def sitePhysicsRapport(self) -> List[DtcDocumentWaarden]:
        """Beschrijvend overzichtsrapport van het meteostation."""
        return self._sitePhysicsRapport.get_waarde()

    @sitePhysicsRapport.setter
    def sitePhysicsRapport(self, value):
        self._sitePhysicsRapport.set_waarde(value, owner=self)
