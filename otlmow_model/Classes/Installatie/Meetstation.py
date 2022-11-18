# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlLokaalTerreinType import KlLokaalTerreinType
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetstation(AIMNaamObject, PuntGeometrie):
    """De plaats waar verschillende sensoren samen 1 meetstation vormen. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._beoordelingLokaleTerrein = OTLAttribuut(field=KlLokaalTerreinType,
                                                      naam='beoordelingLokaleTerrein',
                                                      label='Beoordeling lokale terrein',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.beoordelingLokaleTerrein',
                                                      kardinaliteit_max='*',
                                                      definition='Het soort terrein waarin het meetstation staat met betrekking tot het reliëf en de vegetatie.',
                                                      owner=self)

        self._keuringsrapport = OTLAttribuut(field=DtcDocument,
                                             naam='keuringsrapport',
                                             label='keuringsrapport',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.keuringsrapport',
                                             kardinaliteit_max='*',
                                             definition='Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation.',
                                             owner=self)

        self._masterOfBridgeSensor = OTLAttribuut(field=BooleanField,
                                                  naam='masterOfBridgeSensor',
                                                  label='Master of bridge sensor',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.masterOfBridgeSensor',
                                                  definition='Geeft aan of het meetstation ingeplant is ter hoogte van een brug.',
                                                  owner=self)

        self._nabijheidVanHindernissen = OTLAttribuut(field=KwantWrdInMeter,
                                                      naam='nabijheidVanHindernissen',
                                                      label='Nabijheid van hindernissen',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.nabijheidVanHindernissen',
                                                      kardinaliteit_max='*',
                                                      definition='De afstand tot een hindernis in de nabijheid.',
                                                      owner=self)

        self._nabijheidVanWaterlopen = OTLAttribuut(field=KwantWrdInMeter,
                                                    naam='nabijheidVanWaterlopen',
                                                    label='Nabijheid van waterlopen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.nabijheidVanWaterlopen',
                                                    kardinaliteit_max='*',
                                                    definition='De afstand tot een waterloop in de nabijheid.',
                                                    owner=self)

        self._onderhoudsrapport = OTLAttribuut(field=DtcDocument,
                                               naam='onderhoudsrapport',
                                               label='onderhoudsrapport',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.onderhoudsrapport',
                                               kardinaliteit_max='*',
                                               definition='Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation.',
                                               owner=self)

        self._sitePhysicsRapport = OTLAttribuut(field=DtcDocument,
                                                naam='sitePhysicsRapport',
                                                label='site physics rapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.sitePhysicsRapport',
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
