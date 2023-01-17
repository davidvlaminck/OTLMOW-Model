# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.BevestigingGC import BevestigingGC
from otlmow_model.Classes.Abstracten.Voedingspunt import Voedingspunt
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlZonnepaneelMerk import KlZonnepaneelMerk
from otlmow_model.Datatypes.KlZonnepaneelModelnaam import KlZonnepaneelModelnaam
from otlmow_model.Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zonnepaneel(Voedingspunt, BevestigingGC):
    """Toestel om elektrische energie op te wekken uit zonlicht met als doel het voeden van een installatie. Ook wel fotovoltaïsche cellen of zonnecellen genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Voedingspunt.__init__(self)
        BevestigingGC.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnalogeHoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')

        self._merk = OTLAttribuut(field=KlZonnepaneelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.merk',
                                  definition='Het merk van het zonnepaneel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlZonnepaneelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.modelnaam',
                                       definition='De modelnaam van het zonnepaneel.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technsiche fiche als bijlage van het zonnepaneel.',
                                             owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.vermogen',
                                      definition='Het vermogen van het zonnepaneel.',
                                      owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het zonnepaneel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het zonnepaneel."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """De technsiche fiche als bijlage van het zonnepaneel."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInWattWaarden:
        """Het vermogen van het zonnepaneel."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
